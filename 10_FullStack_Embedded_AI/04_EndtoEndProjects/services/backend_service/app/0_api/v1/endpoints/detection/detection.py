from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.detection import DetectionRequest, DetectionResponse
from app.services.detection_client import trigger_detection_job
from app.crud.detection import store_detection_result

router = APIRouter()

@router.post("/", response_model=DetectionResponse, status_code=status.HTTP_200_OK)
async def run_detection(request: DetectionRequest):
    try:
        detection_result = await trigger_detection_job(request)
        await store_detection_result(detection_result)
        return detection_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

