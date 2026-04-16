import json
import asyncio
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from websockets.exceptions import ConnectionClosed
from app.config import settings
from app.streaming.video_streamer import (
    get_sorted_frame_paths, read_frame, encode_frame_to_jpeg_bytes
)

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# Jinja2 templates for frontend
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/violations/count")
async def get_violations_count():
    try:
        with open(settings.METADATA_PATH) as f:
            metadata = json.load(f)
        return {"violations": len(metadata.get("violations", []))}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.websocket("/ws")
async def websocket_video_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        frame_files = get_sorted_frame_paths()
        for file in frame_files:
            frame = read_frame(file)
            if frame is not None:
                jpeg_bytes = encode_frame_to_jpeg_bytes(frame)
                await websocket.send_bytes(jpeg_bytes)
            await asyncio.sleep(settings.STREAM_DELAY)
    except (WebSocketDisconnect, ConnectionClosed):
        print("WebSocket client disconnected.")

# Run manually if needed (for testing without Docker)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8004, reload=True)

