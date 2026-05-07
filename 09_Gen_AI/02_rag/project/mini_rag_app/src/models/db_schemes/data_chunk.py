from pydantic import BaseModel, Field, Validator
from bson.objectid import ObjectId
from typing import Optional


class DataChunk(BaseModel):
    _id: Optional[ObjectId] # automaticly created by mongodb
    chunk_text : str = Field(..., min_length=1)
    chunk_metadata : dict
    chunk_order : int = Field(..., ge=0) # Ensure chunk_order is a non-negative integer
    chunk_project_id : ObjectId
    
    
    class config:
        arbitrary_types_allowed = True
        