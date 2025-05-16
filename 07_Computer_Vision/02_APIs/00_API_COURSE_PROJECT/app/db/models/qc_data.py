# app/db/models/qc_data.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.base import Base
from datetime import datetime

class QCData(Base):
    __tablename__ = "qc_data"

    id = Column(Integer, primary_key=True, index=True)
    part_number = Column(String, index=True)
    result = Column(String)
    operator = Column(String)
    inspector = Column(String)
    checker = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    rejection_reason = Column(String, nullable=True)
