# app/models/store.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.store_customer import store_customers
class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
#    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    city = relationship("City", back_populates="stores")
    products = relationship("Product", back_populates="store", cascade="all, delete-orphan")
#    country = relationship("Country", back_populates="stores")
    owner = relationship("User", back_populates="stores")
    customers = relationship("User", secondary=store_customers, back_populates="customer_stores")
	
