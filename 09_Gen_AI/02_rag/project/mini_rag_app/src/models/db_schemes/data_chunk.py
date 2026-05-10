from pydantic import BaseModel, Field
from typing import Any, Dict, Optional, Union
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    chunk_asset_id: ObjectId

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):
        return [
            {"key": [("chunk_project_id", 1)], "name": "chunk_project_id_index_1", "unique": False},
        ]


# Vector DB (Qdrant) search result schema.
# We keep this close to DataChunk since the payload typically contains chunk text/metadata.
class RetrievedDocument(BaseModel):
    id: Optional[Union[str, int]] = None
    score: Optional[float] = None
    text: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
