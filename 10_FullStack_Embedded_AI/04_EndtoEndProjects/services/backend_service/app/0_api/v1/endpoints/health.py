from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Health Check"])
def health_check():
    return {"status": "OK", "message": "Backend Service is healthy"}

