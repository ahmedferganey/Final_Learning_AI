# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional 

class UserBase(BaseModel):
  firebase_uid: str
  name: Optional[str] = None
  email: Optional[EmailStr] = None
  phone_number: Optional[str] = None
  role: Optional[str] = "customer"
  

class UserCreate(UserBase):
  pass

class UserUpdate(BaseModel):
  name: Optional[str] 
  phone_number: Optional[str]
  role: Optional[str]
  
class UserOut(UserBase):
    id: int

    model_config = {
        "from_attributes": True
    }
  
