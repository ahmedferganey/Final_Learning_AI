from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.analytics import calculate_rejection_rate, get_top_defect_reasons

router = APIRouter()

@router.get("/rejection-rate")
def get_rejection_rate(db: Session = Depends(get_db)):
    rate = calculate_rejection_rate(db)
    return {"rejection_rate": f"{rate}%"}

@router.get("/top-defect-reasons")
def get_defect_reasons(limit: int = 5, db: Session = Depends(get_db)):
    data = get_top_defect_reasons(db, limit=limit)
    return {"top_defects": [{"reason": r[0], "count": r[1]} for r in data]}
