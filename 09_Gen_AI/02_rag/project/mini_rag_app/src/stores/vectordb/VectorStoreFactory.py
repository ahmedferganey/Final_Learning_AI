from __future__ import annotations

from sqlalchemy.ext.asyncio import async_sessionmaker

from stores.vectordb.QdrantVectorStore import QdrantVectorStore
from stores.vectordb.PGVectorStore import PGVectorStore, PGVectorStoreConfig
from stores.vectordb.VectorDBEnums import VectorDBEnums
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory
from stores.vectordb.VectorStoreInterface import VectorStoreInterface


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
            provider = VectorDBProviderFactory(config=self._settings.model_dump()).create(backend)
            if provider is None:
                raise ValueError(f"Unable to create Qdrant provider for backend={backend!r}")
            return QdrantVectorStore(provider)

        if backend == VectorDBEnums.PGVECTOR.value:
            embedding_dim = int(getattr(self._settings, "EMBEDDING_MODEL_SIZE", 384) or 384)
            return PGVectorStore(
                session_factory=self._db_session_factory,
                config=PGVectorStoreConfig(embedding_dim=embedding_dim),
            )

        raise ValueError(f"Unsupported VECTOR_DB_BACKEND={backend!r}")

