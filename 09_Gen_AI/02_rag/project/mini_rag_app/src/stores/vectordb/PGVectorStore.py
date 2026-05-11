from __future__ import annotations

import uuid
from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

from sqlalchemy import delete, func, select, text as sql_text
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from models.db_schemes import RetrievedDocument
from models.db_schemes.minirag.schemes import VectorDocumentORM
from stores.vectordb.VectorStoreInterface import VectorStoreInterface


@dataclass(frozen=True)
class PGVectorStoreConfig:
    embedding_dim: int = 384


class PGVectorStore(VectorStoreInterface):
    """
    PGVector-backed implementation.

    Design choices:
    - One shared table (`vector_documents`) for all projects.
    - `index_name` acts like the Qdrant collection name (project namespace).
    - No schema/table creation at runtime; Alembic owns schema.
    """

    def __init__(self, session_factory: async_sessionmaker, config: PGVectorStoreConfig):
        self._session_factory = session_factory
        self._config = config

    async def connect(self) -> None:
        # Fail fast if migrations weren't applied.
        async with self._session_factory() as session:
            try:
                await session.execute(sql_text("SELECT 1 FROM vector_documents LIMIT 1"))
            except Exception as exc:  # pragma: no cover
                raise RuntimeError(
                    "PGVectorStore is configured but `vector_documents` is missing. "
                    "Run Alembic migrations for src/models/db_schemes/minirag."
                ) from exc

    async def disconnect(self) -> None:
        # Connection lifecycle is owned by SQLAlchemy engine/session factory.
        return None

    async def index_exists(self, index_name: str, project_uuid: Optional[UUID] = None) -> bool:
        async with self._session_factory() as session:
            stmt = select(VectorDocumentORM.id).limit(1)
            if project_uuid is not None:
                stmt = stmt.where(VectorDocumentORM.project_uuid == project_uuid)
            else:
                stmt = stmt.where(VectorDocumentORM.index_name == index_name)
            row = await session.scalar(stmt)
            return row is not None

    async def get_index_info(self, index_name: str, project_uuid: Optional[UUID] = None) -> dict:
        async with self._session_factory() as session:
            stmt = select(func.count()).select_from(VectorDocumentORM)
            if project_uuid is not None:
                stmt = stmt.where(VectorDocumentORM.project_uuid == project_uuid)
            else:
                stmt = stmt.where(VectorDocumentORM.index_name == index_name)
            count = await session.scalar(stmt)
            return {
                "provider": "PGVECTOR",
                "index_name": index_name,
                "points_count": int(count or 0),
                "embedding_dim": int(self._config.embedding_dim),
            }

    async def delete(self, index_name: str, project_uuid: Optional[UUID] = None) -> bool:
        async with self._session_factory() as session:
            stmt = delete(VectorDocumentORM)
            if project_uuid is not None:
                stmt = stmt.where(VectorDocumentORM.project_uuid == project_uuid)
            else:
                stmt = stmt.where(VectorDocumentORM.index_name == index_name)
            await session.execute(stmt)
            await session.commit()
        return True

    async def ensure_index(
        self,
        index_name: str,
        embedding_size: int,
        do_reset: bool = False,
        project_uuid: Optional[UUID] = None,
    ) -> bool:
        # Table is global; `index_name` is only a namespace.
        if int(embedding_size) != int(self._config.embedding_dim):
            raise ValueError(
                f"Embedding size mismatch: store expects {self._config.embedding_dim}, got {embedding_size}."
            )
        if do_reset:
            await self.delete(index_name, project_uuid=project_uuid)
        return True

    async def add_documents(
        self,
        index_name: str,
        project_uuid: Optional[UUID],
        texts: List[str],
        vectors: List[List[float]],
        metadata: Optional[List[dict]] = None,
        record_ids: Optional[List[str]] = None,
        batch_size: int = 50,
    ) -> bool:
        if len(texts) != len(vectors):
            raise ValueError("texts and vectors must have the same length")

        if metadata is None:
            metadata = [{} for _ in texts]
        if len(metadata) != len(texts):
            raise ValueError("metadata must be the same length as texts")

        resolved_ids: List[uuid.UUID] = []
        if record_ids is None:
            resolved_ids = [uuid.uuid4() for _ in texts]
        else:
            if len(record_ids) != len(texts):
                raise ValueError("record_ids must be the same length as texts")
            for rid in record_ids:
                try:
                    resolved_ids.append(uuid.UUID(str(rid)))
                except Exception:
                    resolved_ids.append(uuid.uuid5(uuid.NAMESPACE_URL, str(rid)))

        if project_uuid is None:
            raise ValueError("PGVectorStore requires project_uuid for add_documents()")

        async with self._session_factory() as session:
            table = VectorDocumentORM.__table__
            for i in range(0, len(texts), batch_size):
                end = i + batch_size
                rows = [
                    {
                        "id": resolved_ids[j],
                        "project_uuid": project_uuid,
                        "index_name": index_name,
                        "text": texts[j],
                        "metadata": metadata[j] or {},
                        "embedding": vectors[j],
                    }
                    for j in range(i, min(end, len(texts)))
                ]

                # Use table insert (not ORM insert) to avoid reserved-name collisions
                # with SQLAlchemy's declarative `metadata` attribute.
                stmt = pg_insert(table).values(rows)
                stmt = stmt.on_conflict_do_update(
                    index_elements=[table.c.id],
                    set_={
                        "index_name": stmt.excluded.index_name,
                        "text": stmt.excluded.text,
                        "metadata": stmt.excluded.metadata,
                        "embedding": stmt.excluded.embedding,
                        "updated_at": func.now(),
                    },
                )
                await session.execute(stmt)
            await session.commit()

        return True

    async def similarity_search(
        self,
        index_name: str,
        project_uuid: Optional[UUID],
        query_vector: List[float],
        top_k: int = 5,
        limit: int = 5,
    ) -> List[RetrievedDocument] | None:
        # Cosine distance; smaller is better.
        distance = VectorDocumentORM.embedding.cosine_distance(query_vector).label("distance")
        stmt = (
            select(VectorDocumentORM.id, VectorDocumentORM.text, VectorDocumentORM.metadata_, distance)
            .order_by(distance.asc())
            .limit(limit or top_k)
        )
        if project_uuid is not None:
            stmt = stmt.where(VectorDocumentORM.project_uuid == project_uuid)
        else:
            stmt = stmt.where(VectorDocumentORM.index_name == index_name)

        async with self._session_factory() as session:
            rows = (await session.execute(stmt)).all()

        if not rows:
            return None

        docs: List[RetrievedDocument] = []
        for row in rows:
            doc_id, doc_text, doc_meta, dist = row
            score = None
            if dist is not None:
                try:
                    score = float(1.0 - float(dist))
                except Exception:
                    score = None
            docs.append(
                RetrievedDocument(
                    id=str(doc_id) if doc_id is not None else None,
                    score=score,
                    text=doc_text,
                    metadata=doc_meta or {},
                )
            )

        return docs
