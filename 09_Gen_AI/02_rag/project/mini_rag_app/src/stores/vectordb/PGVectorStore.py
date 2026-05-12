from __future__ import annotations

from typing import List, Optional
from uuid import UUID

from models.db_schemes import RetrievedDocument
from stores.vectordb.VectorStoreInterface import VectorStoreInterface
from stores.vectordb.providers.PGVectorDBProvider import PGVectorDBProvider


class PGVectorStore(VectorStoreInterface):
    """
    Adapter that exposes VectorStoreInterface on top of PGVectorDBProvider.
    Kept for symmetry with QdrantVectorStore/QdrantDBProvider.
    """

    def __init__(self, provider: PGVectorDBProvider):
        self._provider = provider

    async def connect(self) -> None:
        await self._provider.connect()

    async def disconnect(self) -> None:
        await self._provider.disconnect()

    async def index_exists(self, index_name: str, project_uuid: Optional[UUID] = None) -> bool:
        return await self._provider.index_exists(index_name, project_uuid=project_uuid)

    async def get_index_info(self, index_name: str, project_uuid: Optional[UUID] = None) -> dict:
        return await self._provider.get_index_info(index_name, project_uuid=project_uuid)

    async def delete(self, index_name: str, project_uuid: Optional[UUID] = None) -> bool:
        return await self._provider.delete(index_name, project_uuid=project_uuid)

    async def ensure_index(
        self,
        index_name: str,
        embedding_size: int,
        do_reset: bool = False,
        project_uuid: Optional[UUID] = None,
    ) -> bool:
        return await self._provider.ensure_index(
            index_name,
            embedding_size=embedding_size,
            do_reset=do_reset,
            project_uuid=project_uuid,
        )

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
        return await self._provider.add_documents(
            index_name,
            project_uuid=project_uuid,
            texts=texts,
            vectors=vectors,
            metadata=metadata,
            record_ids=record_ids,
            batch_size=batch_size,
        )

    async def similarity_search(
        self,
        index_name: str,
        project_uuid: Optional[UUID],
        query_vector: List[float],
        top_k: int = 5,
        limit: int = 5,
    ) -> List[RetrievedDocument] | None:
        return await self._provider.similarity_search(
            index_name,
            project_uuid=project_uuid,
            query_vector=query_vector,
            top_k=top_k,
            limit=limit,
        )
