import pytest
import os
from fastapi.testclient import TestClient


from backend.container import Container, Settings
from backend.main import create_web_app


@pytest.fixture(scope="module")
def container():
    container = Container()

    os.environ["POSTGRES_DSN"] = "postgresql://postgres:123456@localhost:7432/pytest"
    os.environ["auth_url"] = "test"

    settings = Settings()
    container.config.from_pydantic(settings)
    yield container
    container.unwire()


@pytest.fixture(scope="module")
def client(container: Container):
    app = create_web_app(container)
    return TestClient(app)
