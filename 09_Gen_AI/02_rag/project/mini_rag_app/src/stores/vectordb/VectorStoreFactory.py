from __future__ import annotations

from sqlalchemy.ext.asyncio import async_sessionmaker

from stores.vectordb.QdrantVectorStore import QdrantVectorStore
from stores.vectordb.PGVectorStore import PGVectorStore
from stores.vectordb.VectorDBEnums import (
    PGVectorDistanceMethodEnums,
    PGVectorIndexTypeEnums,
    VectorDBEnums,
)
from stores.vectordb.VectorStoreInterface import VectorStoreInterface
from stores.vectordb.providers.QdrantDBProvider import QdrantDBProvider
from stores.vectordb.providers.PGVectorDBProvider import PGVectorDBProvider, PGVectorDBProviderConfig
from controllers.BaseController import BaseController


class VectorStoreFactory:
    """
    Selects and constructs the configured vector store implementation.

    Migration strategy:
    - Qdrant remains default via existing VECTOR_DB_BACKEND setting.
    - PGVector can be enabled by setting VECTOR_DB_BACKEND=PGVECTOR after migrations.
    """

    def __init__(self, settings, db_session_factory: async_sessionmaker):
        self._settings = settings
        self._db_session_factory = db_session_factory

    def create(self) -> VectorStoreInterface:
        backend = getattr(self._settings, "VECTOR_DB_BACKEND", None)
        if backend == VectorDBEnums.QDRANT.value:
            settings_payload = self._settings.model_dump()
            base_controller = BaseController()
            db_path = base_controller.get_database_path(settings_payload.get("VECTOR_DB_PATH"))
            provider = QdrantDBProvider(
                db_path=db_path,
                distance_method=settings_payload.get("VECTOR_DB_DISTANCE_METHOD"),
            )
            return QdrantVectorStore(provider)

        if backend == VectorDBEnums.PGVECTOR.value:
            embedding_dim = int(getattr(self._settings, "EMBEDDING_MODEL_SIZE", 384) or 384)
            distance_method = str(getattr(self._settings, "PGVECTOR_DISTANCE_METHOD", "cosine") or "cosine").lower()
            index_type = str(getattr(self._settings, "PGVECTOR_INDEX_TYPE", "hnsw") or "hnsw").lower()

            if distance_method not in {e.value for e in PGVectorDistanceMethodEnums}:
                raise ValueError(f"Unsupported PGVECTOR_DISTANCE_METHOD={distance_method!r}")
            if index_type not in {e.value for e in PGVectorIndexTypeEnums}:
                raise ValueError(f"Unsupported PGVECTOR_INDEX_TYPE={index_type!r}")

            provider = PGVectorDBProvider(
                session_factory=self._db_session_factory,
                config=PGVectorDBProviderConfig(
                    embedding_dim=embedding_dim,
                    distance_method=distance_method,
                    index_type=index_type,
                ),
            )
            return PGVectorStore(provider)

        raise ValueError(f"Unsupported VECTOR_DB_BACKEND={backend!r}")
