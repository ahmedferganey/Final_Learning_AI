from __future__ import annotations

from typing import List, Optional

import anyio
from uuid import UUID

from models.db_schemes import RetrievedDocument
from stores.vectordb.VectorStoreInterface import VectorStoreInterface
from stores.vectordb.providers.QdrantDBProvider import QdrantDBProvider


class QdrantVectorStore(VectorStoreInterface):
    """
    Adapter that exposes the provider-neutral VectorStoreInterface on top of the
    existing QdrantDBProvider implementation.
    """

    def __init__(self, provider: QdrantDBProvider):
        self._provider = provider

    async def connect(self) -> None:
        await anyio.to_thread.run_sync(self._provider.connect)

    async def disconnect(self) -> None:
        await anyio.to_thread.run_sync(self._provider.disconnect)

    async def index_exists(self, index_name: str, project_uuid: Optional[UUID] = None) -> bool:
        return await anyio.to_thread.run_sync(self._provider.collection_exists, index_name)

    async def get_index_info(self, index_name: str, project_uuid: Optional[UUID] = None) -> dict:
        return await anyio.to_thread.run_sync(self._provider.get_collection_info, index_name)

    async def delete(self, index_name: str, project_uuid: Optional[UUID] = None) -> bool:
        return bool(await anyio.to_thread.run_sync(self._provider.delete_collection, index_name))

    async def ensure_index(
        self,
        index_name: str,
        embedding_size: int,
        do_reset: bool = False,
        project_uuid: Optional[UUID] = None,
    ) -> bool:
        def _create() -> bool:
            return bool(
                self._provider.create_collection(
                    collection_name=index_name,
                    embedding_size=embedding_size,
                    do_reset=do_reset,
                )
            )

        return await anyio.to_thread.run_sync(_create)

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
        def _insert() -> bool:
            return bool(
                self._provider.insert_many(
                    collection_name=index_name,
                    texts=texts,
                    vectors=vectors,
                    metadata=metadata,
                    record_ids=record_ids,
                    batch_size=batch_size,
                )
            )

        return await anyio.to_thread.run_sync(_insert)

    async def similarity_search(
        self,
        index_name: str,
        project_uuid: Optional[UUID],
        query_vector: List[float],
        top_k: int = 5,
        limit: int = 5,
    ) -> List[RetrievedDocument] | None:
        def _search() -> List[RetrievedDocument] | None:
            return self._provider.search_by_vector(
                collection_name=index_name,
                query_vector=query_vector,
                top_k=top_k,
                limit=limit,
            )

        return await anyio.to_thread.run_sync(_search)
