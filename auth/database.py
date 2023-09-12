from typing import AsyncGenerator
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from config import*
from models import role

DATABASE_URL = f"postgresql+asyncpg://%{DB_USER}s:%{DB_PASS}s@%{DB_HOST}s:%{DB_PORT}s/%{DB_NAME}s"
Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id=Column(Integer,primary_key=True),
    email=Column(String, nullable=False),
    username=Column(String, nullable=False),
    registered_at=Column(TIMESTAMP, default=datetime.utcnow),
    role_id=Column(Integer, ForeignKey(role.id)),
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool =Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
