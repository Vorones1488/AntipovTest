from src.config import setting
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase



engin = create_async_engine(
    url=setting.DATABASE_URL_asyncpg)

async_session_maker = async_sessionmaker(engin, class_=AsyncSession, expire_on_commit=False)
class Base(DeclarativeBase):
    pass

async def get_asinc_sesiion() -> AsyncGenerator[AsyncSession, None]:
    with async_sessionmaker() as session:
        yield session

