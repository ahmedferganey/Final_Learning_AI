from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.models.qc_data import QCData

def get_total_inspected_count(db: Session) -> int:
    return db.query(func.count(QCData.id)).scalar()

def get_total_rejected_count(db: Session) -> int:
    return db.query(func.count()).filter(QCData.is_rejected == True).scalar()

def calculate_rejection_rate(db: Session) -> float:
    total = get_total_inspected_count(db)
    rejected = get_total_rejected_count(db)
    if total == 0:
        return 0.0
    return round((rejected / total) * 100, 2)

def get_top_defect_reasons(db: Session, limit: int = 5):
    return (
        db.query(QCData.rejection_reason, func.count(QCData.rejection_reason).label("count"))
        .filter(QCData.is_rejected == True)
        .group_by(QCData.rejection_reason)
        .order_by(func.count(QCData.rejection_reason).desc())
        .limit(limit)
        .all()
    )
