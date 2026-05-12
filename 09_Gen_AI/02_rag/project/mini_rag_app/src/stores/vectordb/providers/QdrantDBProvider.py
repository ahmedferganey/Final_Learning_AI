from qdrant_client import models, QdrantClient
import logging
from ..VectorDBEnums import VectorDBEnums, DistanceMethodEnums
from typing import List
import uuid

from models.db_schemes import RetrievedDocument


class QdrantDBProvider:
    
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

        self.logger = logging.getLogger("minirag.vectordb.qdrant")

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
        self.logger.info("Connecting to Qdrant (path=%s)", self.db_path)
        self.client = QdrantClient(path=self.db_path)
        self.logger.info("Connected to Qdrant")

    def disconnect(self):
        if self.client:
            self.logger.info("Disconnecting from Qdrant")
            self.client.close()
            self.client = None
            self.logger.info("Disconnected from Qdrant")
    
    def collection_exists(self, collection_name: str) -> bool:
        try:
            return self.client.collection_exists(collection_name)
        except Exception as e:
            self.logger.exception("Error checking collection existence (collection=%s): %s", collection_name, e)
            return False
        
    def list_all_collections(self) -> list:
        try:
            return self.client.get_collections().collections
        except Exception as e:
            self.logger.exception("Error listing collections: %s", e)
            return []
    
    def get_collection_info(self, collection_name: str) -> dict:
        try:
            return self.client.get_collection(collection_name).dict()
        except Exception as e:
            self.logger.exception("Error getting collection info (collection=%s): %s", collection_name, e)
            return {}
    
    def delete_collection(self, collection_name):
        if self.collection_exists(collection_name):
            self.logger.info("Deleting collection (collection=%s)", collection_name)
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
            self.logger.info(
                "Creating collection (collection=%s, embedding_size=%s, distance=%s)",
                collection_name,
                embedding_size,
                getattr(self.distance_method, "name", self.distance_method),
            )
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(size=embedding_size, distance=self.distance_method)
            )
            return True
        except Exception as e:
            self.logger.exception("Error creating collection (collection=%s): %s", collection_name, e)
            return False
        
    def insert_one(self, collection_name: str, text: str, vector: List[float], metadata: dict = None, record_id: str = None):
        if not self.collection_exists(collection_name):
            self.logger.warning(f"Collection {collection_name} does not exist.")
            return False
        try:
            normalized_record_id = self.normalize_record_id(record_id)
            self.logger.debug("Inserting one record (collection=%s, id=%s)", collection_name, normalized_record_id)
            self.client.upload_records(
                collection_name=collection_name,
                records=[
                    models.Record(id=normalized_record_id, vector=vector, payload={"text": text, **(metadata or {})})
                ]
            )
            return True
        except Exception as e:
            self.logger.exception("Error inserting record (collection=%s): %s", collection_name, e)
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
                self.logger.debug(
                    "Uploading batch (collection=%s, start=%s, end=%s, batch_size=%s)",
                    collection_name,
                    i,
                    batch_end,
                    batch_size,
                )
                _ = self.client.upload_records(
                    collection_name=collection_name,
                    records=batch_records,
                )
            except Exception as e:
                self.logger.exception("Error uploading batch (collection=%s): %s", collection_name, e)
                return False

        return True
    
    def search_by_vector(self, collection_name: str, query_vector: List[float], top_k: int = 5, limit: int = 5):
        if not self.collection_exists(collection_name):
            self.logger.warning(f"Collection {collection_name} does not exist.")
            return []
        try:
            self.logger.debug(
                "Searching (collection=%s, limit=%s, top_k=%s)",
                collection_name,
                (limit or top_k),
                top_k,
            )
            search_result = self.client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=limit or top_k,
                with_payload=True
            )
            if not search_result or len(search_result) ==0:
                return None
            # Convert provider-specific objects (ScoredPoint) into app-level schemas.
            docs: List[RetrievedDocument] = []
            for item in (search_result or []):
                payload = getattr(item, "payload", None) or {}
                text = payload.get("text")

                # Normalize metadata across our two insert paths:
                # - insert_one: payload={"text": text, **metadata}
                # - insert_many: payload={"text": text, "metadata": {...}}
                metadata = payload.get("metadata")
                if isinstance(metadata, dict):
                    normalized_metadata = metadata
                else:
                    normalized_metadata = {k: v for k, v in payload.items() if k != "text"}

                docs.append(
                    RetrievedDocument(
                        id=getattr(item, "id", None),
                        score=getattr(item, "score", None),
                        text=text,
                        metadata=normalized_metadata,
                    )
                )

            return docs
        except Exception as e:
            self.logger.exception("Error searching (collection=%s): %s", collection_name, e)
            return []
