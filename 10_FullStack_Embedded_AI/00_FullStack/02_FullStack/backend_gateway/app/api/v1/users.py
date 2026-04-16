# app/api/v1/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.models.user import User
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.firebase_uid == user_in.firebase_uid).first()
  if user:
    raise HTTPException(status_code=400, detail="User already exists")
  new_user = User(**user_in.dict())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@router.get("/{firebase_uid}", response_model=UserOut)
def get_user(firebase_uid: str, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.firebase_uid == firebase_uid).first()
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user

@router.put("/{firebase_uid}", response_model=UserOut)
def update_user(firebase_uid: str, user_in: UserUpdate, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.firebase_uid == firebase_uid).first()
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  
  for key, value in user_in.dict(exclude_unset=True).items():
    setattr(user, key, value)
  
  db.commit()
  db.refresh(user)
  return user 
