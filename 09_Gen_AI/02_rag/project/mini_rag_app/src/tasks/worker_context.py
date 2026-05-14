"""
Async resources for Celery tasks (one event loop per task via asyncio.run).

Each task opens a fresh engine, sessions, and vector store for the duration of
the coroutine, then disposes them so AsyncEngine is never shared across loops.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from database.session import check_database_connection, create_engine_and_session_factory
from helpers.config import Settings, get_settings
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.llm.templates import TemplateParser
from stores.vectordb.VectorStoreFactory import VectorStoreFactory

if TYPE_CHECKING:
    from stores.vectordb.VectorStoreInterface import VectorStoreInterface

logger = logging.getLogger(__name__)


@dataclass
class WorkerBundle:
    settings: Settings
    engine: AsyncEngine
    session_factory: async_sessionmaker[AsyncSession]
    vector_store: "VectorStoreInterface"
    generation_client: object
    embedding_client: object
    template_parser: TemplateParser


@asynccontextmanager
async def worker_bundle():
    settings = get_settings()
    database_url = settings.get_database_url()
    engine, session_factory = create_engine_and_session_factory(database_url)
    await check_database_connection(engine)

    settings_payload = settings.model_dump()
    llm_factory = LLMProviderFactory(config=settings_payload)

    generation_client = llm_factory.create(settings.GENERATION_BACKEND)
    generation_client.set_generation_model(settings.GENERATION_MODEL_ID)

    embedding_client = llm_factory.create(settings.EMBEDDING_BACKEND)
    embedding_client.set_embedding_model(
        settings.EMBEDDING_MODEL_ID,
        settings.EMBEDDING_MODEL_SIZE,
    )

    vector_store = VectorStoreFactory(settings, session_factory).create()
    await vector_store.connect()
    template_parser = TemplateParser(default_language=settings.DEFAULT_LANGUAGE)

    try:
        yield WorkerBundle(
            settings=settings,
            engine=engine,
            session_factory=session_factory,
            vector_store=vector_store,
            generation_client=generation_client,
            embedding_client=embedding_client,
            template_parser=template_parser,
        )
    finally:
        try:
            await vector_store.disconnect()
        except Exception:
            logger.exception("vector_store.disconnect failed")
        try:
            await engine.dispose()
        except Exception:
            logger.exception("engine.dispose failed")
