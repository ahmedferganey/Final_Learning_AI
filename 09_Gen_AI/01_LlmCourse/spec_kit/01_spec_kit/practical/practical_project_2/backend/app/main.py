from contextlib import asynccontextmanager
from inspect import isawaitable
from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.core.config import get_settings
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    yield
    await engine.dispose()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="GymOS API",
        version=settings.app_version,
        lifespan=lifespan,
    )

    @app.get("/api/v1/health")
    async def health() -> JSONResponse:
        checks: dict[str, str] = {}

        try:
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            checks["database"] = "ok"
        except Exception:
            checks["database"] = "unreachable"

        try:
            import redis.asyncio as aioredis

            redis_client = aioredis.from_url(settings.redis_url, socket_connect_timeout=2)
            ping_result = redis_client.ping()
            if isawaitable(ping_result):
                await ping_result
            await redis_client.aclose()
            checks["redis"] = "ok"
        except Exception:
            checks["redis"] = "unreachable"

        all_ok = all(value == "ok" for value in checks.values())
        if all_ok:
            return JSONResponse(
                status_code=200,
                content={"status": "ok", "version": settings.app_version},
            )

        return JSONResponse(
            status_code=503,
            content={"status": "degraded", "checks": checks},
        )

    _register_routers(app)
    return app


def _register_routers(app: FastAPI) -> None:
    from app.modules.analytics.router import router as analytics_router
    from app.modules.auth.router import router as auth_router
    from app.modules.coaching.router import router as coaching_router
    from app.modules.notifications.router import router as notifications_router
    from app.modules.nutrition.router import router as nutrition_router
    from app.modules.sync.router import router as sync_router
    from app.modules.training.router import router as training_router
    from app.modules.users.router import router as users_router

    app.include_router(auth_router)
    app.include_router(users_router)
    app.include_router(training_router)
    app.include_router(coaching_router)
    app.include_router(analytics_router)
    app.include_router(nutrition_router)
    app.include_router(notifications_router)
    app.include_router(sync_router)


app = create_app()
