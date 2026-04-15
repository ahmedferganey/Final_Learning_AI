from pydantic import BaseModel
from typing import Optional, List

class DetectionRequest(BaseModel):
    video_id: str
    frame_range: Optional[List[int]] = None  # e.g., [0, 100]

class DetectionResult(BaseModel):
    object_id: str
    label: str
    confidence: float
    bounding_box: dict  # {x, y, width, height}

class DetectionResponse(BaseModel):
    video_id: str
    results: List[DetectionResult]

