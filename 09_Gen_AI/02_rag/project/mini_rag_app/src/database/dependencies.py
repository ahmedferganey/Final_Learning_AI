from typing import AsyncIterator

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db_session(request: Request) -> AsyncIterator[AsyncSession]:
    async with request.app.db_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
