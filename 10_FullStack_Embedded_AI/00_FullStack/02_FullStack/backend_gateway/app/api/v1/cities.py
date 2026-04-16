# app/api/v1/cities.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from typing import List

from app.db.session import get_db
from app.models.city import City
from app.schemas.city import CityCreate, CityOut

router = APIRouter(prefix="/cities", tags=["Cities"])

@router.get("/", response_model=List[CityOut])
def list_cities(db: Session = Depends(get_db)):
    cities = db.query(City).options(
        joinedload(City.country)
    ).all()

    return [
        CityOut(
            id=city.id,
            name=city.name,
            country_id=city.country.id,
            country_name=city.country.name
        )
        for city in cities
    ]

@router.post("/", response_model=CityOut)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    db_city = City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)

    return CityOut(
        id=db_city.id,
        name=db_city.name,
        country_id=db_city.country.id,
        country_name=db_city.country.name
    )
