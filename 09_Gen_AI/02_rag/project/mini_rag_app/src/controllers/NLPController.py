from .BaseController import BaseController
from models.db_schemes import Project, DataChunk
from typing import List, Optional
from stores.llm.LlmEnums import DocumentTypeEnum
import logging
import uuid

logger = logging.getLogger(__name__)

class NLPController(BaseController):
    def __init__(self, vectordb_client, generation_client, embedding_client):
        super().__init__()
        self.vectordb_client = vectordb_client
        self.generation_client = generation_client
        self.embedding_client = embedding_client

    def create_collection_name(self, project_id: str):
        return f"project_{project_id}_collection".strip()
    
    def reset_vector_db_collection(self, project: Project):
        collection_name = self.create_collection_name(project.project_id)
        if self.vectordb_client.collection_exists(collection_name):
            return self.vectordb_client.delete_collection(collection_name)
    
    def get_vector_db_collection_info(self, project: Project):
        collection_name = self.create_collection_name(project.project_id)
        if self.vectordb_client.collection_exists(collection_name):
            return self.vectordb_client.get_collection_info(collection_name)
        return None

    def search_vector_db_collection(self, project: Project, query_text: str, top_k: int = 5, limit: int = 5):
        collection_name = self.create_collection_name(project.project_id)

        if not self.vectordb_client.collection_exists(collection_name):
            return None, collection_name

        query_vector = self.embedding_client.embed_text(
            query_text,
            document_type=DocumentTypeEnum.QUERY.value,
        )

        if query_vector is None:
            return None, collection_name

        hits = self.vectordb_client.search_by_vector(
            collection_name=collection_name,
            query_vector=query_vector,
            top_k=top_k,
            limit=limit,
        )

        return hits, collection_name

    def create_record_id(self, project: Project, chunk: DataChunk) -> str:
        seed = f"{project.project_id}:{chunk.id}:{chunk.chunk_asset_id}:{chunk.chunk_order}"
        return str(uuid.uuid5(uuid.NAMESPACE_URL, seed))
    
    def index_into_vector_db(self, project: Project, chunks: List[DataChunk], do_reset: Optional[int] = 0):
        try:
            collection_name = self.create_collection_name(project.project_id)
            if do_reset:
                self.reset_vector_db_collection(project)

            texts = [chunk.chunk_text for chunk in chunks]
            metadata = [chunk.chunk_metadata for chunk in chunks]
            record_ids = [self.create_record_id(project, chunk) for chunk in chunks]

            if hasattr(self.embedding_client, "embed_texts"):
                vectors = self.embedding_client.embed_texts(
                    texts,
                    document_type=DocumentTypeEnum.DOCUMENT.value,
                )
            else:
                vectors = [
                    self.embedding_client.embed_text(
                        text,
                        document_type=DocumentTypeEnum.DOCUMENT.value,
                    )
                    for text in texts
                ]

            if not vectors or len(vectors) != len(texts) or any(vector is None for vector in vectors):
                logger.error("Embedding generation failed for project '%s'", project.project_id)
                return False

            if not self.vectordb_client.collection_exists(collection_name):
                self.vectordb_client.create_collection(
                    collection_name=collection_name,
                    do_reset=do_reset,
                    embedding_size=self.embedding_client.embedding_size,
                )

            return self.vectordb_client.insert_many(
                collection_name=collection_name,
                texts=texts,
                vectors=vectors,
                metadata=metadata,
                record_ids=record_ids,
            )
        except Exception as exc:
            logger.exception("Failed to index project '%s': %s", project.project_id, exc)
            return False
