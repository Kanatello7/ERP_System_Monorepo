from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from .config import settings

from typing import AsyncGenerator
#from contextlib import asynccontextmanager

engine = create_async_engine(
    url=settings.DATABASE_URL
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session 
        finally:
            await session.close()