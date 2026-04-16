from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float
    store_id: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    store_name: str
    city_name: str
    category_name: str

    model_config = {
        "from_attributes": True
    }

class ProductFilter(BaseModel):
    country: Optional[str] = None
    city: Optional[str] = None
    category: Optional[str] = None
    store_name: Optional[str] = None
