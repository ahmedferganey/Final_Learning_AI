# app/api/v1/endpoints/user.py
from fastapi import APIRouter, Depends
from app.core.firebase import verify_firebase_token

router = APIRouter()

@router.get("/me", tags=["Users"])
async def get_user_info(decoded_token=Depends(verify_firebase_token)):
    return {
        "uid": decoded_token["uid"],
        "email": decoded_token.get("email"),
        "name": decoded_token.get("name"),
    }

