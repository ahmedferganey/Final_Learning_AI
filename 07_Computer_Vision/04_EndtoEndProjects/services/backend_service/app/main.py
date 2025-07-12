from fastapi import FastAPI

from app.api.v1.endpoints import user, order, detection, health
from app.streaming import endpoints as streaming_endpoints

app = FastAPI()

app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(order.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(detection.router, prefix="/api/v1/detection", tags=["detection"])
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])
app.include_router(streaming_endpoints.router, prefix="/stream", tags=["streaming"])
