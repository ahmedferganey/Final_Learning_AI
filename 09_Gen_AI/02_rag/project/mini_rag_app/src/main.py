from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
import logging

logger = logging.getLogger("uvicorn.error")

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    mongo_url = settings.get_mongodb_url()
    app.mongo_conn = AsyncIOMotorClient(mongo_url)
    await app.mongo_conn.admin.command("ping")
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    logger.info("MongoDB connection established for database '%s'", settings.MONGODB_DATABASE)

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()


app.include_router(base.base_router)
app.include_router(data.data_router)
