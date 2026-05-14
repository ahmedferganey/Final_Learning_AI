from pydantic import BaseModel, Field
from typing import Any, Dict, Optional, Union
from uuid import UUID

class DataChunk(BaseModel):
    id: Optional[UUID] = Field(default=None)
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    project_uuid: UUID
    asset_uuid: UUID

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):
        return [
            {"key": [("project_uuid", 1)], "name": "project_uuid_index_1", "unique": False},
        ]


# Vector DB (Qdrant) search result schema.
# We keep this close to DataChunk since the payload typically contains chunk text/metadata.
class RetrievedDocument(BaseModel):
    id: Optional[Union[str, int]] = None
    score: Optional[float] = None
    text: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
