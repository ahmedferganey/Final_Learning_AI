from fastapi import FastAPI
from routes import base, data, nlp
from helpers.config import get_settings
import logging
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.vectordb.VectorDBProviderFactory import   VectorDBProviderFactory
from stores.vectordb.QdrantVectorStore import QdrantVectorStore
from stores.llm.templates import TemplateParser
from database.session import create_engine_and_session_factory, check_database_connection


logger = logging.getLogger("uvicorn.error")

app = FastAPI()

@app.on_event("startup")
async def startup_span():
    settings = get_settings()
    # Keep settings accessible at runtime (routes/controllers can read defaults like DEFAULT_LANGUAGE).
    app.settings = settings

    database_url = settings.get_database_url()
    app.db_engine, app.db_session_factory = create_engine_and_session_factory(database_url)
    await check_database_connection(app.db_engine)
    logger.info("PostgreSQL connection established")

    settings_payload = settings.model_dump()
    llm_factory = LLMProviderFactory(config=settings_payload)
    vectordb_provider_factory = VectorDBProviderFactory(config=settings_payload)


    # generation client
    app.generation_client = llm_factory.create(settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(settings.GENERATION_MODEL_ID)
   
    # embedding client
    app.embedding_client = llm_factory.create(settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(settings.EMBEDDING_MODEL_ID, settings.EMBEDDING_MODEL_SIZE)

    #vector db client
    app.vectordb_client = vectordb_provider_factory.create(settings.VECTOR_DB_BACKEND)
    app.vectordb_client.connect()                                                           
    # Provider-neutral interface for the rest of the app (Step 1/2).
    # PGVector will be added later without changing callers.
    app.vector_store = QdrantVectorStore(app.vectordb_client)

    # Shared template loader (language fallback + potential future caching).
    app.template_parser = TemplateParser(default_language=settings.DEFAULT_LANGUAGE)

    
@app.on_event("shutdown")
async def shutdown_span():
    if hasattr(app, "db_engine"):
        await app.db_engine.dispose()

    if hasattr(app, "vectordb_client"):
        app.vectordb_client.disconnect()

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)
