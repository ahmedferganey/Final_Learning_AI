# app/api/v1/stores.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from typing import List

from app.db.session import get_db
from app.models.store import Store
from app.models.city import City
from app.schemas.store import StoreOut, StoreCreate

router = APIRouter(prefix="/stores", tags=["Stores"])


@router.get("/", response_model=List[StoreOut])
def list_stores(db: Session = Depends(get_db)):
    """
    List all stores with their associated cities.
    """
    stores = db.query(Store).options(
      joinedload(Store.city).joinedload(City.country)
      ).all()

    return [
        StoreOut(
            id=store.id,
            name=store.name,
            city_id=store.city_id,
            city_name=store.city.name,
            country_name=store.city.country.name
        )
        for store in stores
    ]
    
@router.post("/", response_model=StoreOut)
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
  db_store = Store(**store.model_dump())
  db.add(db_store)
  db.commit()
  db.refresh(db_store)
  
  return StoreOut(
    id=db_store.id,
    name=db_store.name,
    city_id=db_store.city_id,
    country_name=db_store.city.country.name
  )
  
  