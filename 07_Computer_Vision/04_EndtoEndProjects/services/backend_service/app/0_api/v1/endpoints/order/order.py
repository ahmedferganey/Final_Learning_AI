from fastapi import APIRouter, HTTPException, status
from app.schemas.order import OrderRequest, OrderResponse
from app.services.order_processor import process_order

router = APIRouter()

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderRequest):
    try:
        return await process_order(order)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

