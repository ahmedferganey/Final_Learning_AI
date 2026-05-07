from pydantic import BaseModel, Field, Validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    _id: Optional[ObjectId] # automaticly created by mongodb
    project_id: str = (..., min_length=1)

    @Validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value
    
    class config:
        arbitrary_types_allowed = True
        