from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings


engine = create_async_engine(
    settings.DATABASE_URI,
    echo=settings.DB_ECHO_LOG,
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
