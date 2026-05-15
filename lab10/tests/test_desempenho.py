"""Desempenho: pytest-benchmark em função crítica (simulação de busca)."""

from nf_metrics import META_P95_MS, percentile_95


def buscar_produto_memoria(produto_id: int) -> dict:
    """Simula caminho quente de leitura (sem I/O de rede)."""
    return {"id": produto_id, "nome": f"Item {produto_id}", "preco": 99.9}


def test_benchmark_busca_produto(benchmark):
    """Exemplo Aula: medir tempo de função de busca com pytest-benchmark."""
    resultado = benchmark(buscar_produto_memoria, 42)
    assert resultado["id"] == 42


def test_metodologia_p95_sobre_amostra_sintetica():
    """Valida cálculo de P95 usado para confrontar meta < 500ms em relatórios."""
    latencias = [50.0] * 94 + [400.0] * 5 + [900.0]
    assert percentile_95(latencias) <= META_P95_MS
