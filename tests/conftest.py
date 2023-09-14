import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from auth.database import get_async_session
from auth.database import Base as metadata
from config import *

from main import app


DATABASE_URL_TEST=f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test=create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker=sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
metadata.bind=engine_test