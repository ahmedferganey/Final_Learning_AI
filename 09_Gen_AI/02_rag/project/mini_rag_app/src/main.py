from fastapi import FastAPI
from routes import base, data, nlp
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
import logging
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.vectordb.VectorDBProviderFactory import   VectorDBProviderFactory


logger = logging.getLogger("uvicorn.error")

app = FastAPI()

@app.on_event("startup")
async def startup_span():
    settings = get_settings()
    mongo_url = settings.get_mongodb_url()
    app.mongo_conn = AsyncIOMotorClient(mongo_url)
    await app.mongo_conn.admin.command("ping")
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    logger.info("MongoDB connection established for database '%s'", settings.MONGODB_DATABASE)
    llm_factory = LLMProviderFactory(config=settings.dict())
    vectordb_provider_factory = VectorDBProviderFactory(config=settings.dict())


    # generation client
    app.generation_client = llm_factory.create(settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(settings.GENERATION_MODEL_ID)
   
    # embedding client
    app.embedding_client = llm_factory.create(settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(settings.EMBEDDING_MODEL_ID, settings.EMBEDDING_MODEL_SIZE)

    #vector db client
    app.vectordb_client = vectordb_provider_factory.create(settings.VECTOR_DB_BACKEND)
    app.vectordb_client.connect()                                                           


@app.on_event("shutdown")
async def shutdown_span():
    app.mongo_conn.close()
    app.vectordb_client.disconnect()

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)
