from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_health():
    return {"message": "health endpoint"}
