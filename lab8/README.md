# Atividade Aula 08 — Suíte de testes REST (CC8550)

## 1. APIs e documentação

- **Principal:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — [Guia](https://jsonplaceholder.typicode.com/guide/)
- **Complementar:** [httpbin.org](https://httpbin.org/) — rotas `/status/400` e `/bearer` (documentação no site do httpbin)

## 2. Justificativa da escolha

O **JSONPlaceholder** oferece CRUD simulado sobre **posts** com **200**, **201**, **404** e listas reais, ideal para status code, schema e fixture. Ele **não** expõe autenticação Bearer nem respostas **4xx** configuráveis para “dados inválidos”. Por isso o **httpbin** é usado de forma explícita: **`/bearer`** para testar **200 com credencial** e **401 sem credencial**, e **`/status/400`** para um **4xx** determinístico em CI (equivalente a validar que a suíte trata falhas HTTP da faixa 4xx).

## 3. Instalação

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

(Linux/macOS: `source venv/bin/activate`.)

## 4. Execução

```bash
python -m pytest test_api.py -v
```

Opcional — salvar saída:

```bash
python -m pytest test_api.py -v > resultado.txt
```

## 5. Testes implementados

| # | Teste | O que valida |
|---|--------|----------------|
| 1 | `test_get_colecao_status_200_lista_nao_vazia` | GET coleção → 200, lista não vazia |
| 2 | `test_get_recurso_existente_schema_jsonschema` | GET recurso → `jsonschema` |
| 3 | `test_get_recurso_inexistente_404` | GET inexistente → 404 |
| 4 | `test_post_criar_recurso_201_com_id` | POST → 201 e `id` |
| 5 | `test_patch_atualiza_campo` | PATCH → campo alterado |
| 6 | `test_delete_status_204_ou_200` | DELETE → 200 ou 204 |
| 7 | `test_requisicao_que_retorna_4xx` | Resposta **4xx** (httpbin) |
| 8 | `test_endpoint_autenticado_com_credencial_bearer` / `test_endpoint_autenticado_sem_credencial_401` | Com Bearer / sem credencial → 401 |
| 9 | `test_fixture_post_criado` | `@pytest.fixture` `post_criado` |
| 10 | `test_tempo_resposta_get_menor_que_2_segundos` | Tempo de resposta menor que 2,0 s |

## 6. Restrições atendidas

- Apenas **Python** (`requests`, `pytest`, `jsonschema`).
- Sem `time.sleep()`.
- Cada função de teste tem **docstring** com o critério validado.

## 7. Entrega no GitHub

Repositório público com `test_api.py`, `requirements.txt` e `README.md` commitados; enviar o link pelo Moodle conforme prazo do curso.
