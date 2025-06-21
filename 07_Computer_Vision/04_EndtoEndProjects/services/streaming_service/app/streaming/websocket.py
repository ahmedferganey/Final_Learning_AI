from fastapi import WebSocket
from app.utils.video_buffer import VideoBuffer
import asyncio
import base64

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    buffer = VideoBuffer()

    while True:
        frame = buffer.get_latest_frame()
        if frame:
            await websocket.send_text(frame)
        await asyncio.sleep(0.1)

