# app/api/products.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from typing import List
from app.db.session import get_db
from app.models.product import Product
from app.models.store import Store
from app.schemas.product import ProductOut, ProductCreate, ProductFilter
from app.services.product_service import apply_product_filters

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/products/filter", response_model=List[ProductOut])
def filter_products(filters: ProductFilter, db: Session = Depends(get_db)):
    products = apply_product_filters(filters, db)

    return [
        ProductOut(
            id=p.id,
            name=p.name,
            price=p.price,
            store_name=p.store.name,
            city_name=p.store.city.name,
            category_name=p.category.name,
        )
        for p in products
    ]

@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return ProductOut(
        id=db_product.id,
        name=db_product.name,
        price=db_product.price,
        store_name=db_product.store.name,
        city_name=db_product.store.city.name,
        category_name=db_product.category.name,
    )

@router.get("/", response_model=List[ProductOut])
def list_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).options(
        joinedload(Product.store).joinedload(Store.city),
        joinedload(Product.category)
    ).all()

    return [
        ProductOut(
            id=p.id,
            name=p.name,
            price=p.price,
            store_name=p.store.name,
            city_name=p.store.city.name,
            category_name=p.category.name,
        )
        for p in products
    ]

