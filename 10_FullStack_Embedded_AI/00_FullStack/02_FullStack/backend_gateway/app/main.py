# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine

if settings.ENV != "production":
    Base.metadata.create_all(bind=engine)



app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    debug=settings.DEBUG)


# ✅ CORS Middleware (customize for security in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register versioned API router
app.include_router(api_router, prefix="/api/v1")


# ✅ Healthcheck / root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the API Gateway Provided by Fragello",
        "environment": settings.ENV,
        "debug": settings.DEBUG
    }
