# File: app/schemas/qc_data.py
from pydantic import BaseModel
from datetime import datetime

class QCDataBase(BaseModel):
    operator_id: int
    inspector_id: int
    checker_id: int
    part_number: str
    status: str  # e.g., "Accepted" or "Rejected"
    timestamp: datetime

class QCDataCreate(QCDataBase):
    pass

class QCDataRead(QCDataBase):
    id: int

    class Config:
        orm_mode = True
