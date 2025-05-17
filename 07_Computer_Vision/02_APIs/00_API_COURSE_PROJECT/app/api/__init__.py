from fastapi import APIRouter
from app.api.routes import router as api_router

api_router_main = APIRouter()
api_router_main.include_router(api_router)
