from fastapi import APIRouter, WebSocket
from app.streaming.manager import stream_manager

router = APIRouter()

@router.websocket("/ws/stream/{camera_id}")
async def streaming_router(websocket: WebSocket, camera_id: str):
    await websocket.accept()
    await stream_manager.connect(websocket, camera_id)
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        stream_manager.disconnect(websocket, camera_id)

