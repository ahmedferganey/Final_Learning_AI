from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_detection():
    return {"message": "detection endpoint"}
