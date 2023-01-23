import pytest

from tests.conftest import TestClient


def test_sample_url(client: TestClient):
    res = client.get("/sample")


def test_credentials_is_correct(client: TestClient):
    payload = {"username": "test", "password": "test"}
    res = client.post("/login", json=payload)
