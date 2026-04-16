import os

import pytest
from _pytest.config import ExitCode
from httpx import ASGITransport, AsyncClient

os.environ.setdefault("APP_ENV", "test")
os.environ.setdefault("APP_VERSION", "0.1.0")
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://gymos:gymos@localhost:5432/gymos")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    if exitstatus == ExitCode.NO_TESTS_COLLECTED:
        session.exitstatus = ExitCode.OK


@pytest.fixture
async def client() -> AsyncClient:
    from app.main import create_app

    async with AsyncClient(
        transport=ASGITransport(app=create_app()),
        base_url="http://test",
    ) as ac:
        yield ac
