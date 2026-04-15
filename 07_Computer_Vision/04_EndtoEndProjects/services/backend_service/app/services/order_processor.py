from app.schemas.order import OrderRequest, OrderResponse
import uuid

async def process_order(order: OrderRequest) -> OrderResponse:
    # Simulate order processing logic
    return OrderResponse(
        order_id=str(uuid.uuid4()),
        status="submitted",
        message="Order has been created successfully"
    )

