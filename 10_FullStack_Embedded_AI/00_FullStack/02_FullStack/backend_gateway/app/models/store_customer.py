# app/models/store_customer.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base

store_customers = Table(
    "store_customers",
    Base.metadata,
    Column("store_id", Integer, ForeignKey("stores.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
)

