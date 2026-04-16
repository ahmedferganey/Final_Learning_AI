# app/schemas/store.py

from pydantic import BaseModel

class StoreBase(BaseModel):
    name: str
    city_id: int

class StoreCreate(StoreBase):
    pass

class StoreOut(StoreBase):
    id: int
    city_name: str
    country_name: str

    model_config = {
        "from_attributes": True
    }

class StoreOutLite(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }
