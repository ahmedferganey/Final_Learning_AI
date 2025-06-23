# app/streaming/websocket.py
from fastapi import WebSocket
from app.utils.video_buffer import VideoBuffer
import asyncio
import base64

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    buffer = VideoBuffer()

    while True:
        frame_b64 = buffer.get_latest_frame()
        print(f"[WebSocket] Frame buffer status: {frame_b64 is not None}")        
        if frame_b64:
            try:
                # Send binary image (JPEG) to frontend
                frame_bytes = base64.b64decode(frame_b64)
                await websocket.send_bytes(frame_bytes)
            except Exception as e:
                print(f"[WebSocket Error] {e}")
        await asyncio.sleep(0.1)

