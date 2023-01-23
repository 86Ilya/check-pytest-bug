from fastapi import Depends, Request, APIRouter
from pydantic import BaseModel

from backend.container import Container, Provide, inject

from .helpers import prepare_auth

router = APIRouter()


class AuthCredentials(BaseModel):
    username: str
    password: str


@router.get("/sample")
async def sample():
    return "OK"


@router.post("/login")
@inject
async def login(
    request: Request,
    creds: AuthCredentials,
    httpx_client=Provide[Container.httpx_client],
    url=Provide[Container.config.auth_url],
    session=Provide[Container.db_session],
):
    await prepare_auth(
        creds.username,
        creds.password,
        httpx_client,
        url,
        session,
    )
    return "OK"
