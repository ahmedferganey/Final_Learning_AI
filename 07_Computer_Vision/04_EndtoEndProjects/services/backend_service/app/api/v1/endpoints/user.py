from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_user():
    return {"message": "user endpoint"}
