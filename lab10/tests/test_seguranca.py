"""Segurança: rate limiting 100 req/min/IP (middleware da API)."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_rate_limit_centesima_requisicao_retorna_429(client):
    """Após 100 GETs bem-sucedidos no mesmo IP, a 101ª deve ser bloqueada (429)."""
    for _ in range(100):
        r = client.get("/api/produtos")
        assert r.status_code == 200
    r101 = client.get("/api/produtos")
    assert r101.status_code == 429
    body = r101.json()
    assert body.get("detail") == "RATE_LIMIT_EXCEEDED"
