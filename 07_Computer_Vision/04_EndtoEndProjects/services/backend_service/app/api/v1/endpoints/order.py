from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_order():
    return {"message": "order endpoint"}
