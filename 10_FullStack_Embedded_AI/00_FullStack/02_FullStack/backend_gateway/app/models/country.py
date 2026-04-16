# models/country.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    code = Column(String, unique=True, nullable=False)  # ISO code like "EG"

    cities = relationship("City", back_populates="country")
#    stores = relationship("Store", back_populates="country", cascade="all, delete")

