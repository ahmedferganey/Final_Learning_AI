# app/models/city.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id"))  # 👈 Add this line

    country = relationship("Country", back_populates="cities")  # 👈 And this line
    stores = relationship("Store", back_populates="city")

