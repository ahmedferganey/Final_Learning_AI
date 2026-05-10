from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId
from datetime import datetime

class Asset(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    asset_project_id: ObjectId = Field(...)
    asset_name: str = Field(..., min_length=1)
    asset_type: str = Field(..., min_length=1)
    asset_size: Optional[int] = Field(default=None, gt=0)
    asset_pushed_at: datetime = Field(default_factory=datetime.utcnow)
    asset_config: dict = Field(default_factory=dict)

    @field_validator("asset_name", "asset_type")
    @classmethod
    def validate_non_empty(cls, value: str):
        if not value.strip():
            raise ValueError('Field cannot be empty or whitespace')
        return value

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):
        return [
            {"key": [("asset_project_id", 1), ("asset_name", 1)], "name": "project_name_index_1", "unique": True}
        ]
