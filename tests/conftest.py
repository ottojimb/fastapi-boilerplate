import asyncio
from typing import AsyncGenerator, Callable, Generator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.config import settings
from app.database.session import async_session
from app.database.tables import Base


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
async def db_session() -> AsyncGenerator:
    engine = create_async_engine(settings.DATABASE_URI_TEST, future=True, echo=False)
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(
            lambda session: session.execute(
                text("CREATE EXTENSION IF NOT EXISTS postgis;")
            )
        )
        await connection.run_sync(Base.metadata.create_all)
        async with async_session(bind=connection) as session:
            yield session
            await session.flush()
            await session.rollback()


@pytest.fixture()
def override_get_session(db_session: AsyncSession) -> Callable:
    async def _override_get_session():
        yield db_session

    return _override_get_session


@pytest.fixture()
def app(override_get_session: Callable) -> FastAPI:
    from app.api.dependencies.database import get_session
    from app.main import app

    app.dependency_overrides[get_session] = override_get_session
    return app


@pytest.fixture()
async def async_client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
