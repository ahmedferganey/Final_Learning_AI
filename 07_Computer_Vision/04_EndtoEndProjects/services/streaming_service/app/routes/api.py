from fastapi import APIRouter
from app.utils.video_buffer import VideoBuffer

router = APIRouter()

@router.get("/")
def api_root():
    return {"message": "Streaming API is running 🚀"}

@router.get("/violations")
def get_violation_stats():
    buffer = VideoBuffer()
    return {"total_violations": buffer.get_violation_count()}

