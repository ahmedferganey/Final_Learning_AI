from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.store_customer import store_customers
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    phone_number = Column(String, nullable=True)
    role = Column(String, default="customer")

    # Fixed: reference the Store model correctly by name
    stores = relationship("Store", back_populates="owner")
    customer_stores = relationship("Store", secondary=store_customers, back_populates="customers")
