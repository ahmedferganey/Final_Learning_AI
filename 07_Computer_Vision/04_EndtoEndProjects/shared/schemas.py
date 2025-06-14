from pydantic import BaseModel
from typing import List

class Detection(BaseModel):
    label: str
    bbox: List[int]  # [x, y, w, h]
    violation: bool = False

class Metadata(BaseModel):
    timestamp: int
    detections: List[Detection]
    violations: List[str]
    latest_frame: str

