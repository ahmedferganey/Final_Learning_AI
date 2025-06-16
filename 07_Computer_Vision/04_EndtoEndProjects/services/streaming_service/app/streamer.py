from fastapi import APIRouter
from fastapi.responses import StreamingResponse, JSONResponse
from app.config import FRAMES_PATH, METADATA_PATH
from app.utils import frame_generator, get_latest_metadata

router = APIRouter()

@router.get("/video")
def stream_video():
    """
    Stream MJPEG video composed of latest frames from the FRAMES_PATH directory.
    """
    return StreamingResponse(
        frame_generator(FRAMES_PATH),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

@router.get("/metadata")
def metadata():
    """
    Serve the latest metadata JSON from METADATA_PATH.
    """
    data = get_latest_metadata(METADATA_PATH)
    return JSONResponse(content=data)

