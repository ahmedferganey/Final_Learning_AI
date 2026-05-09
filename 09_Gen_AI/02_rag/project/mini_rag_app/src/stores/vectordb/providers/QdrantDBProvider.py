from qdrant_client import models, QdrantClient
from ..VectorDBInterface import VectorDBInterface
import logging
from ..VectorDBEnums import VectorDBEnums, DistanceMethodEnums
from typing import List
import uuid


class QdrantDBProvider(VectorDBInterface):
    
    def __init__(self, db_path: str, distance_method: str):
        self.client = None
        self.db_path = db_path
        self.distance_method = None

        if distance_method == DistanceMethodEnums.COSINE.value:
            self.distance_method = models.Distance.COSINE
        elif distance_method == DistanceMethodEnums.EUCLIDEAN.value:
            self.distance_method = models.Distance.EUCLIDEAN
        elif distance_method == DistanceMethodEnums.MANHATTAN.value:
            self.distance_method = models.Distance.MANHATTAN
        elif distance_method == DistanceMethodEnums.Dot.value:        
            self.distance_method = models.Distance.DOT

        self.logger = logging.getLogger(__name__)

    def normalize_record_id(self, record_id):
        if record_id is None:
            return str(uuid.uuid4())

        if isinstance(record_id, int):
            return record_id

        if isinstance(record_id, uuid.UUID):
            return str(record_id)

        try:
            return str(uuid.UUID(str(record_id)))
        except (ValueError, TypeError, AttributeError):
            return str(uuid.uuid5(uuid.NAMESPACE_URL, str(record_id)))

    def connect(self):
        self.client = QdrantClient(path=self.db_path)

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
    
    def collection_exists(self, collection_name: str) -> bool:
        try:
            return self.client.collection_exists(collection_name)
        except Exception as e:
            self.logger.error(f"Error checking collection existence: {e}")
            return False
        
    def list_all_collections(self) -> list:
        try:
            return self.client.get_collections().collections
        except Exception as e:
            self.logger.error(f"Error listing collections: {e}")
            return []
    
    def get_collection_info(self, collection_name: str) -> dict:
        try:
            return self.client.get_collection(collection_name).dict()
        except Exception as e:
            self.logger.error(f"Error getting collection info: {e}")
            return {}
    
    def delete_collection(self, collection_name):
        if self.collection_exists(collection_name):
            return self.client.delete_collection(collection_name)
        else:
            self.logger.warning(f"Collection {collection_name} does not exist.")
            return False 
        
    def create_collection(self, collection_name: str, embedding_size: int, do_reset: bool = False):
        if self.collection_exists(collection_name):
            if do_reset:
                self.delete_collection(collection_name)
            else:
                self.logger.warning(f"Collection {collection_name} already exists.")
                return False

        try:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(size=embedding_size, distance=self.distance_method)
            )
            return True
        except Exception as e:
            self.logger.error(f"Error creating collection: {e}")
            return False
        
    def insert_one(self, collection_name: str, text: str, vector: List[float], metadata: dict = None, record_id: str = None):
        if not self.collection_exists(collection_name):
            self.logger.warning(f"Collection {collection_name} does not exist.")
            return False
        try:
            normalized_record_id = self.normalize_record_id(record_id)
            self.client.upload_records(
                collection_name=collection_name,
                records=[
                    models.Record(id=normalized_record_id, vector=vector, payload={"text": text, **(metadata or {})})
                ]
            )
            return True
        except Exception as e:
            self.logger.error(f"Error inserting point: {e}")
            return False
    
    def insert_many(self, collection_name: str, texts: List[str], 
                    vectors: List[List[float]], metadata: List[dict] = None, 
                    record_ids: List[str] = None, batch_size: int = 50):
        
        if metadata is None:
            metadata = [None] * len(texts)

        if record_ids is None:
            record_ids = [self.normalize_record_id(f"{collection_name}:{i}") for i in range(len(texts))]
        else:
            record_ids = [self.normalize_record_id(record_id) for record_id in record_ids]

        for i in range(0, len(texts), batch_size):
            batch_end = i + batch_size

            batch_texts = texts[i:batch_end]
            batch_vectors = vectors[i:batch_end]
            batch_metadata = metadata[i:batch_end]
            batch_record_ids = record_ids[i:batch_end]

            batch_records = [
                models.Record(
                    id=batch_record_ids[x],
                    vector=batch_vectors[x],
                    payload={
                        "text": batch_texts[x], "metadata": batch_metadata[x]
                    }
                )

                for x in range(len(batch_texts))
            ]

            try:
                _ = self.client.upload_records(
                    collection_name=collection_name,
                    records=batch_records,
                )
            except Exception as e:
                self.logger.error(f"Error while inserting batch: {e}")
                return False

        return True
    
    def search_by_vector(self, collection_name: str, query_vector: List[float], top_k: int = 5, limit: int = 5):
        if not self.collection_exists(collection_name):
            self.logger.warning(f"Collection {collection_name} does not exist.")
            return []
        try:
            search_result = self.client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=limit or top_k,
                with_payload=True
            )
            return search_result
        except Exception as e:
            self.logger.error(f"Error searching points: {e}")
            return []
