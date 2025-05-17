# File: app/db/crud/qc_data.py
from sqlalchemy.orm import Session
from app.db.models.qc_data import QCData
from app.schemas.qc_data import QCDataCreate

def create_qc_data(db: Session, qc_data: QCDataCreate) -> QCData:
    db_record = QCData(**qc_data.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_qc_data_by_id(db: Session, data_id: int) -> QCData | None:
    return db.query(QCData).filter(QCData.id == data_id).first()

def get_all_qc_data(db: Session) -> list[QCData]:
    return db.query(QCData).all()
