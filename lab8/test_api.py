"""
Suíte de testes de sistema para API REST pública (Aula 08 - CC8550).
API principal: JSONPlaceholder. Códigos 4xx e Bearer: httpbin.org.
"""

import pytest
import requests
import jsonschema

JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"
HTTPBIN = "https://httpbin.org"

# Schema mínimo de um post (GET /posts/:id)
SCHEMA_POST = {
    "type": "object",
    "required": ["id", "userId", "title", "body"],
    "properties": {
        "id": {"type": "integer"},
        "userId": {"type": "integer"},
        "title": {"type": "string", "minLength": 1},
        "body": {"type": "string"},
    },
    "additionalProperties": True,
}


@pytest.fixture
def post_criado():
    """Cria post via POST (setup), entrega o JSON; teardown envia DELETE."""
    payload = {
        "title": "Post fixture lab8",
        "body": "Conteúdo de teste",
        "userId": 1,
    }
    resp = requests.post(f"{JSONPLACEHOLDER}/posts", json=payload, timeout=10)
    assert resp.status_code == 201
    post = resp.json()
    yield post
    pid = post.get("id")
    if pid is not None:
        requests.delete(f"{JSONPLACEHOLDER}/posts/{pid}", timeout=10)


def test_get_colecao_status_200_lista_nao_vazia():
    """GET /posts na coleção deve retornar 200 e lista JSON não vazia."""
    resp = requests.get(f"{JSONPLACEHOLDER}/posts", timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_recurso_existente_schema_jsonschema():
    """GET /posts/1 deve retornar 200 e corpo conforme schema jsonschema."""
    resp = requests.get(f"{JSONPLACEHOLDER}/posts/1", timeout=10)
    assert resp.status_code == 200
    jsonschema.validate(instance=resp.json(), schema=SCHEMA_POST)


def test_get_recurso_inexistente_404():
    """GET /posts/:id inexistente deve retornar 404."""
    resp = requests.get(f"{JSONPLACEHOLDER}/posts/999999", timeout=10)
    assert resp.status_code == 404


def test_post_criar_recurso_201_com_id():
    """POST /posts cria recurso simulado → 201 e campo id no JSON."""
    payload = {"title": "Novo post", "body": "Corpo", "userId": 1}
    resp = requests.post(f"{JSONPLACEHOLDER}/posts", json=payload, timeout=10)
    assert resp.status_code == 201
    data = resp.json()
    assert "id" in data
    assert isinstance(data["id"], int)


def test_patch_atualiza_campo():
    """PATCH /posts/1 deve retornar 200 e refletir título alterado."""
    payload = {"title": "Titulo atualizado lab8"}
    resp = requests.patch(f"{JSONPLACEHOLDER}/posts/1", json=payload, timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("title") == payload["title"]


def test_delete_status_204_ou_200():
    """DELETE /posts/1 — JSONPlaceholder retorna 200 (aceito também 204)."""
    resp = requests.delete(f"{JSONPLACEHOLDER}/posts/1", timeout=10)
    assert resp.status_code in (200, 204)


def test_requisicao_que_retorna_4xx():
    """GET em rota httpbin que força 400 — valida tratamento de resposta 4xx (erro de negócio/validação)."""
    resp = requests.get(f"{HTTPBIN}/status/400", timeout=10)
    assert 400 <= resp.status_code < 500


def test_endpoint_autenticado_com_credencial_bearer():
    """GET /bearer com Authorization Bearer → 200 e autenticado."""
    headers = {"Authorization": "Bearer token_de_teste"}
    resp = requests.get(f"{HTTPBIN}/bearer", headers=headers, timeout=10)
    assert resp.status_code == 200
    assert resp.json().get("authenticated") is True


def test_endpoint_autenticado_sem_credencial_401():
    """GET /bearer sem header Authorization → 401."""
    resp = requests.get(f"{HTTPBIN}/bearer", timeout=10)
    assert resp.status_code == 401


def test_fixture_post_criado(post_criado):
    """Usa fixture post_criado: POST retornou id e título esperados."""
    assert "id" in post_criado
    assert post_criado.get("title") == "Post fixture lab8"
    assert post_criado.get("userId") == 1


def test_tempo_resposta_get_menor_que_2_segundos():
    """GET em recurso existente deve completar em menos de 2,0 s."""
    resp = requests.get(f"{JSONPLACEHOLDER}/posts/1", timeout=10)
    assert resp.status_code == 200
    assert resp.elapsed.total_seconds() < 2.0
