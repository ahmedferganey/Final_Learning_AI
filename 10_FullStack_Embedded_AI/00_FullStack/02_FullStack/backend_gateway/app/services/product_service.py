# app/services/filter.py

from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.store import Store
from app.models.city import City
from app.models.country import Country
from app.models.category import Category
from app.schemas.product import ProductFilter

def apply_product_filters(filters: ProductFilter, db: Session):
    query = db.query(Product).join(Product.store).join(Store.city).join(City.country).join(Product.category)

    if filters.store_name:
        query = query.filter(Store.name.ilike(f"%{filters.store_name}%"))

    if filters.category:
        query = query.filter(Category.name.ilike(f"%{filters.category}%"))

    if filters.city:
        query = query.filter(City.name.ilike(f"%{filters.city}%"))

    if filters.country:
        query = query.filter(Country.name.ilike(f"%{filters.country}%"))

    return query.all()

