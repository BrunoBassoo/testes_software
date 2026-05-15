# Relatório — Atividade “Teste integrado de e-commerce” (Black Friday)

**Disciplina:** CC8550 — Simulação e Teste de Software  
**Cenário:** Lançamento na Black Friday — **10 000** usuários simultâneos esperados; **P95 < 500 ms**; **99,9 %** disponibilidade; proteção contra abuso e vazamento de dados.

## 1. Metas (slide) vs evidências

Preencha a tabela após executar Locust contra o ambiente alvo (ex.: API deste lab em `127.0.0.1:8000` **não** substitui cluster de produção).

| Tipo           | Métrica                         | Meta              | Resultado medido | Aprovado? |
|----------------|----------------------------------|-------------------|------------------|-----------|
| Desempenho     | Tempo de resposta **P95**       | **< 500 ms**      | *(ms)*           | SIM / NÃO |
| Carga          | **Throughput** sustentado       | **> 2000 req/s**  | *(req/s)*        | SIM / NÃO |
| Estresse       | **Usuários** no ponto de quebra | **> 15 000**      | *(usuários)*     | SIM / NÃO |
| Escalabilidade | **Eficiência horizontal**       | **> 80 %**        | *( % )*          | SIM / NÃO |
| Segurança      | **Rate limit**                  | **100 req/min/IP**| *(confirmado)*   | SIM / NÃO |
| Disponibilidade| Taxa de sucesso (aprox.)        | **≥ 99,9 %**      | *( % )*          | SIM / NÃO |

### Como obter números

- **Locust (UI):** coluna **95%** (latência) e **RPS** (throughput).
- **Locust (headless):** resumo no terminal; opcional `--csv=...` para séries.
- **Escalabilidade:** medir RPS com **1** instância (baseline) e com **N** instâncias atrás de balanceador; calcular  
  `eficiência = 100 × RPS_real / (RPS_baseline × N)` (vide Aula).
- **Segurança (rate limit):** `python -m pytest tests/test_seguranca.py -v` — valida **429** na 101ª requisição no mesmo IP.

## 2. Análise (texto objetivo)

- **Gargalo principal observado:** *(ex.: CPU, rede, fila, banco)*  
- **Risco para a Black Friday:** *(breve)*  
- **Ações corretivas:** *(cache, autoscaling, índices, CDN, WAF, limites, filas)*  

## 3. Conclusão

- **Veredito geral:** APROVADO / REPROVADO para go-live na Black Friday, com base nas metas acima.  
- **Ressalvas:** *(ex.: metas de 15k usuários e 2k req/s só validadas em ambiente de escala real)*  

## 4. Evidência automatizada local (pytest)

Os testes em `tests/` cobrem:

- **Desempenho (metodologia):** `pytest-benchmark` + cálculo de **P95** sintético alinhado à meta.
- **Carga / disponibilidade / escalabilidade / critério de estresse:** fórmulas e exemplos numéricos do slide.
- **Segurança:** limite **100 req/min/IP** na API de demonstração.

Comando sugerido:

```text
python -m pytest tests -v --benchmark-disable
```

*(Opcional)* SAST em código da aplicação: `bandit -r app -ll` (conforme slide).
