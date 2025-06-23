# app/main.py

from fastapi import FastAPI
from app.routes.api import router as api_router
from app.streaming.websocket import websocket_endpoint
import subprocess
import threading
import os

app = FastAPI(title="Streaming Service")

# Include REST and WebSocket routes
app.include_router(api_router, prefix="/api")
app.add_api_websocket_route("/ws", websocket_endpoint)


def start_rabbitmq_listener():
    # Use full path in Docker to avoid path issues
    subprocess.run(["python", "-u", "app/consumers/annoted_frame_listener.py"])


@app.on_event("startup")
def on_startup():
    # Start consumer in a daemon thread at app startup
    threading.Thread(target=start_rabbitmq_listener, daemon=True).start()


# ⛔ DO NOT include uvicorn.run here inside __main__ for Docker!
# Instead, run with uvicorn via Docker CMD or entrypoint

# This block is optional and only needed for running outside Docker (local dev)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=9000, reload=True)

