from fastapi import FastAPI
from app import streamer, websocket_server

app = FastAPI(title="Streaming Service")

# MJPEG Streaming Endpoints
app.include_router(streamer.router)

# WebSocket Streaming Endpoints
app.include_router(websocket_server.router)

# Health Check Endpoint
@app.get("/")
def root():
    return {"message": "Streaming service is up"}

