# app/schemas/country.py

from pydantic import BaseModel
from typing import Optional, List
from app.schemas.store import StoreOutLite

class CountryBase(BaseModel):
    name: str
    code: str  # ISO country code, e.g. "EG", "US"

class CountryCreate(CountryBase):
    pass

class CountryOut(CountryBase):
    id: int
    # Removed stores list; use cities and their stores instead if needed    
#    stores: Optional[List[StoreOutLite]] = []
    cities: Optional[List[str]] = []  # List of city names if you want

    model_config = {
        "from_attributes": True
    }

