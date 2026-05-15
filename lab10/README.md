# Lab 10 — Testes não funcionais (E-commerce / Black Friday)

Material alinhado ao PDF **“Aula 10 (2)”** (conteúdo: testes não funcionais — desempenho, carga, estresse, escalabilidade e segurança) e à **atividade prática** do final dos slides: *plano integrado* + **exemplos em Python** + instruções para **métricas** e **relatório** (`RELATORIO.md`).

## Requisitos de negócio (atividade)

| Tipo            | Métrica obrigatória        | Meta definida              |
|-----------------|----------------------------|----------------------------|
| Desempenho      | Tempo de resposta         | **P95 < 500 ms**           |
| Carga           | Throughput sustentado     | **> 2000 req/s**           |
| Estresse        | Ponto de quebra           | **> 15 000 usuários**      |
| Escalabilidade  | Eficiência horizontal     | **> 80 %**                 |
| Segurança       | Rate limiting             | **100 req/min/IP**       |
| Contexto        | Usuários simultâneos      | **10 000** (esperado BF)   |
| Disponibilidade | Durante o evento          | **99,9 %**                 |

## Estrutura

```text
lab10/
  app/main.py              # API FastAPI mínima + rate limit
  nf_metrics.py            # Metas e funções de métricas (P95, throughput, etc.)
  locustfile.py            # Carga (mix de tarefas)
  locustfile_stress.py     # Estresse / spike (Locust)
  tests/                   # pytest + pytest-benchmark + TestClient
  RELATORIO.md             # Preencher com resultados reais (Locust/ambiente)
  requirements.txt
  pytest.ini
```

## Instalação

```powershell
cd c:\Users\bruno\Documents\FEI\test_software\testes_software\lab10
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## 1) API local (alvo do Locust)

```powershell
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## 2) Testes automatizados (pytest)

```powershell
python -m pytest tests -v --benchmark-disable
```

(benchmark opcional: `python -m pytest tests/test_desempenho.py -v --benchmark-min-rounds=20`)

## 3) Carga com Locust (métricas reais P95 / throughput)

Em outro terminal, com a API no ar:

```powershell
locust -f locustfile.py --host=http://127.0.0.1:8000
```

Abrir `http://localhost:8089`, definir usuários e taxa de spawn, observar **P95** e **RPS**.

Headless (exemplo):

```powershell
locust -f locustfile.py --host=http://127.0.0.1:8000 --users 500 --spawn-rate 50 --run-time 60s --headless
```

## 4) Estresse (spike)

```powershell
locust -f locustfile_stress.py --host=http://127.0.0.1:8000 --users 300 --spawn-rate 60 --run-time 30s --headless --csv=resultado_estresse
```

Interpretação (Aula): queda de throughput + aumento de falhas indica aproximação do **ponto de quebra**; a meta de **> 15 000 usuários** deve ser avaliada em **ambiente de homologação** com hardware e rede representativos.

## 5) Relatório de aprovação / reprovação

Após coletar números do Locust (e, se aplicável, de monitoramento), registrar conclusões em **`RELATORIO.md`**.

## Plano de teste (resumo)

1. **Desempenho:** medir P95 nas rotas quentes (`/api/produto/{id}`, `/api/produtos`) sob carga moderada; comparar com **500 ms**.
2. **Carga:** sustentar taxa alinhada ao mix Black Friday; verificar **RPS** e erros **HTTP**.
3. **Estresse:** rampa agressiva até erros/latência degradarem; estimar usuários no limiar.
4. **Escalabilidade:** com **2+ instâncias** atrás de balanceador, medir RPS e aplicar **eficiência = RPS_real / (RPS_baseline × N)**.
5. **Segurança:** validar **429** após limite por IP (teste automatizado em `tests/test_seguranca.py`); complementar com SAST/DAST (ex.: **bandit**, OWASP ZAP) em pipeline.
