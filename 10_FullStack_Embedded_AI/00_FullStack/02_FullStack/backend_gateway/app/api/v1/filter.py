from pydantic import BaseModel, Field
from typing import Optional

class ProductFilter(BaseModel):
    store_name: Optional[str] = Field(None, description="Name of the store")
    category: Optional[str] = Field(None, description="Category of the product")
    country: Optional[str] = Field(None, description="Country where the product is available")
    city: Optional[str] = Field(None, description="City where the product is available")