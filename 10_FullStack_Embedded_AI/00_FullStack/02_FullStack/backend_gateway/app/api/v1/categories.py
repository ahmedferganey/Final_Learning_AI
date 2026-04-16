# app/api/v1/categories.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryOut

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    """
    Retrieve a list of all categories.
    """
    return db.query(Category).all()
  
@router.post("/", response_model=CategoryOut)
def create_category(category: CategoryCreate, db : Session = Depends(get_db)):
    """
    Create a new category.
    """
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category