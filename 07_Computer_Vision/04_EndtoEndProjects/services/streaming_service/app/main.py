from fastapi import FastAPI
from app.routes.api import router as api_router
from app.streaming.websocket import websocket_endpoint
import uvicorn

app = FastAPI(title="Streaming Service")

# Root route for health check or homepage
@app.get("/")
def root():
    return {"message": "Streaming Service is live 🚀"}

# Register API routes under /api prefix
app.include_router(api_router, prefix="/api")

# Register WebSocket endpoint
app.add_api_websocket_route("/ws", websocket_endpoint)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=9000, reload=True)

