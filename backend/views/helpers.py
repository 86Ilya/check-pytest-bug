from typing import Dict

import httpx
from dependency_injector.wiring import inject
from sqlalchemy.ext.asyncio import AsyncSession


@inject
async def prepare_auth(
    username: str,
    password: str,
    httpx_client: httpx.AsyncClient,
    sso_auth_url: str,
    session: AsyncSession,
) -> Dict:
    pass
