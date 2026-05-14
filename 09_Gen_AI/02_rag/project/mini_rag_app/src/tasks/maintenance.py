"""
Operational tasks (no HTTP route): worker reachability and dependency checks.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any

from celery_app import celery_app
from sqlalchemy import text
from tasks.worker_context import worker_bundle

logger = logging.getLogger(__name__)


@celery_app.task(name="tasks.maintenance.ping")
def ping_task() -> dict[str, Any]:
    return {"ok": True, "task": "tasks.maintenance.ping"}


@celery_app.task(name="tasks.maintenance.health_check")
def health_check_task() -> dict[str, Any]:
    return asyncio.run(_health_check_async())


async def _health_check_async() -> dict[str, Any]:
    async with worker_bundle() as bundle:
        async with bundle.session_factory() as session:
            await session.execute(text("SELECT 1"))
        return {
            "ok": True,
            "database": "reachable",
            "vector_store": "connected",
            "app_name": bundle.settings.APP_NAME,
        }
