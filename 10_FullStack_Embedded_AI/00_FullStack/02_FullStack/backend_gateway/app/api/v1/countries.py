# app/api/v1/countries.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.country import Country
from app.schemas.country import CountryCreate, CountryOut 

router = APIRouter(prefix="/countries", tags=["Countries"])

@router.get("/", response_model=List[CountryOut])
def list_countries(db: Session = Depends(get_db)):
  """
      Retrieve list of countries
  """
  return db.query(Country).all()

@router.post("/", response_model=CountryOut)
def create_country(country: CountryCreate, db: Session = Depends(get_db)):
  """
      creeate a new country
  """
  db_country = Country(**country.model_dump())
  db.add(db_country)
  db.commit()
  db.refresh(db_country)
  return db_country