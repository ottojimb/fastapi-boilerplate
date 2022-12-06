from app.database.session import async_session
from typing import AsyncGenerator


async def get_session() -> AsyncGenerator:
    """
    Dependency function that yields db sessions
    """
    async with async_session() as session:
        yield session
        await session.commit()
