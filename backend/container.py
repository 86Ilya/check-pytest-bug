import httpx
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject  # noqa: F401
from pydantic import BaseSettings
from sqlalchemy.engine import URL, make_url
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


class Settings(BaseSettings):
    auth_url: str
    postgres_dsn: str


async def init_db_engine(postgres_dsn: str):
    dsn: URL = make_url(postgres_dsn)
    dsn = dsn.set(drivername="postgresql+asyncpg")
    engine = create_async_engine(dsn)
    yield engine
    await engine.dispose()


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()
    httpx_client = providers.Singleton(httpx.AsyncClient)
    db_engine = providers.Resource(init_db_engine, postgres_dsn=config.postgres_dsn)

    db_session = providers.Factory(AsyncSession, db_engine, expire_on_commit=False)
