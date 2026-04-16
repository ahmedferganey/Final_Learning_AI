# app/schemas/city.py

from pydantic import BaseModel

class CityBase(BaseModel):
    name: str
    country_id: str

class CityCreate(CityBase):
    pass

class CityOut(CityBase):
    id: int
    country_name: str
    
    model_config = {
        "from_attributes": True
    }
