from pydantic import BaseModel
from typing import Optional

class OrderRequest(BaseModel):
    customer_id: str
    video_id: str
    description: Optional[str] = None

class OrderResponse(BaseModel):
    order_id: str
    status: str
    message: Optional[str] = None

