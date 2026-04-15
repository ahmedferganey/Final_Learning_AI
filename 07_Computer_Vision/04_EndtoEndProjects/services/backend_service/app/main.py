from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import asyncio

from app.api.v1.endpoints import user, order, detection, health
from app.streaming.endpoints import router as streaming_router
from app.streaming.consumer import consume_frames
from app.core.config import settings
from app.core.logger import setup_logging

# 1. Setup logging

setup_logging()

# Lifespan context: used to start and gracefully stop background tasks
@asynccontextmanager
async def lifespan(app: FastAPI):
    consumer_task = asyncio.create_task(consume_frames())  # Start RabbitMQ consumer loop
    try:
        yield  # Application runs here
    finally:
        consumer_task.cancel()  # On shutdown, stop the consumer task
        await asyncio.sleep(0.1)  # Small delay to ensure cleanup

# 2. Create FastAPI app

app = FastAPI(
    title="Backend Service API",
    version="1.0.0",
    description="Production backend for detection, order, and real-time streaming via RabbitMQ",
    lifespan=lifespan
)

# 3. CORS Configuration (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pizza-store-4fcd5.web.app"],  # Change to your deployed frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Include API Routers
app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
app.include_router(user.router, prefix="/api/v1/user", tags=["User"])
app.include_router(order.router, prefix="/api/v1/order", tags=["Order"])
app.include_router(detection.router, prefix="/api/v1/detection", tags=["Detection"])

# 5. Include WebSocket Router
app.include_router(websocket_router, prefix="/ws")

# 6. Include Streaming HTTP Endpoints
app.include_router(streaming_router, prefix="/api/v1/streaming", tags=["Streaming"])


# 7. App startup and shutdown
@app.on_event("startup")
async def startup_event():
    init_firebase()
    # You can optionally connect to DB or start background tasks here

@app.on_event("shutdown")
async def shutdown_event():
    # Cleanup connections, queues, etc.
    pass

