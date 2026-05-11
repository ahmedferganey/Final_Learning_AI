from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.db_schemes import RetrievedDocument


class VectorStoreInterface(ABC):
    """
    Provider-neutral vector store contract used by application services/controllers.

    Notes:
    - Keep this interface small and focused on RAG needs.
    - Provider-specific configuration/clients must be hidden behind implementations.
    """

    @abstractmethod
    async def connect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def index_exists(self, index_name: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_index_info(self, index_name: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, index_name: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def ensure_index(self, index_name: str, embedding_size: int, do_reset: bool = False) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def add_documents(
        self,
        index_name: str,
        texts: List[str],
        vectors: List[List[float]],
        metadata: Optional[List[dict]] = None,
        record_ids: Optional[List[str]] = None,
        batch_size: int = 50,
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def similarity_search(
        self,
        index_name: str,
        query_vector: List[float],
        top_k: int = 5,
        limit: int = 5,
    ) -> "List[RetrievedDocument] | None":
        raise NotImplementedError
