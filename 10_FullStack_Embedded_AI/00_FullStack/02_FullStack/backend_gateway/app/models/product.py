# models/product.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Product(Base):
    __tablename__  = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    price = Column(Integer)
    store_id = Column(Integer, ForeignKey("stores.id"))
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # Relationships
    store = relationship("Store", back_populates="products")
    category = relationship("Category", back_populates="products")
