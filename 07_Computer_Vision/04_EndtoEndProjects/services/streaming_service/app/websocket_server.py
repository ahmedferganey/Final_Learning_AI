from fastapi import APIRouter, WebSocket
import os
import time
import cv2
from app.config import FRAMES_PATH
from app.utils import get_sorted_frames

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    last_sent = None
    try:
        while True:
            frames = get_sorted_frames(FRAMES_PATH)
            if frames and frames[-1] != last_sent:
                frame_path = os.path.join(FRAMES_PATH, frames[-1])
                with open(frame_path, "rb") as f:
                    await websocket.send_bytes(f.read())
                last_sent = frames[-1]
            time.sleep(0.1)
    except Exception as e:
        print(f"WebSocket closed: {e}")
