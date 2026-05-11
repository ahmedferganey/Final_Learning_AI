from __future__ import annotations

from typing import List, Optional

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

    def connect(self) -> None:
        self._provider.connect()

    def disconnect(self) -> None:
        self._provider.disconnect()

    def index_exists(self, index_name: str) -> bool:
        return self._provider.collection_exists(index_name)

    def get_index_info(self, index_name: str) -> dict:
        return self._provider.get_collection_info(index_name)

    def delete(self, index_name: str) -> bool:
        return bool(self._provider.delete_collection(index_name))

    def ensure_index(self, index_name: str, embedding_size: int, do_reset: bool = False) -> bool:
        return bool(
            self._provider.create_collection(
                collection_name=index_name,
                embedding_size=embedding_size,
                do_reset=do_reset,
            )
        )

    def add_documents(
        self,
        index_name: str,
        texts: List[str],
        vectors: List[List[float]],
        metadata: Optional[List[dict]] = None,
        record_ids: Optional[List[str]] = None,
        batch_size: int = 50,
    ) -> bool:
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

    def similarity_search(
        self,
        index_name: str,
        query_vector: List[float],
        top_k: int = 5,
        limit: int = 5,
    ) -> List[RetrievedDocument] | None:
        return self._provider.search_by_vector(
            collection_name=index_name,
            query_vector=query_vector,
            top_k=top_k,
            limit=limit,
        )

