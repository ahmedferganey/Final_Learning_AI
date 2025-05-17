from fastapi import APIRouter
from .upload import router as upload_router
from .analytics import router as analytics_router

router = APIRouter()
router.include_router(upload_router, prefix="/upload", tags=["Upload"])
router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
