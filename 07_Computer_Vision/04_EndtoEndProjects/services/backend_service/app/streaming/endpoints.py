from fastapi import APIRouter, WebSocket
from app.streaming.stream_handler import handle_stream

router = APIRouter()

@router.websocket("/ws")
async def stream(websocket: WebSocket):
    await handle_stream(websocket)
