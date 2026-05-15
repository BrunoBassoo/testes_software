"""Métricas e metas do cenário Black Friday (Aula 10 / material não funcional)."""

# Metas extraídas da atividade do slide "Atividade Prática"
USUARIOS_SIMULTANEOS_ESPERADOS = 10_000
META_P95_MS = 500
META_DISPONIBILIDADE = 99.9  # %
META_THROUGHPUT_REQ_S = 2_000
META_USUARIOS_ESTRESSE_QUEBRA = 15_000
META_EFICIENCIA_HORIZONTAL_PCT = 80.0
META_RATE_LIMIT_REQ_POR_MINUTO_POR_IP = 100


def percentile_95(values_ms: list[float]) -> float:
    """Percentil 95 aproximado (ordenação + índice)."""
    if not values_ms:
        return 0.0
    s = sorted(values_ms)
    idx = min(len(s) - 1, max(0, int(round(0.95 * (len(s) - 1)))))
    return float(s[idx])


def throughput_req_s(total_requests: int, duration_s: float) -> float:
    """Throughput = total / tempo (requisições por segundo)."""
    if duration_s <= 0:
        return 0.0
    return total_requests / duration_s


def eficiencia_horizontal_pct(throughput_com_n_nos: float, n: int, throughput_baseline: float) -> float:
    """
    Eficiência = (throughput real / throughput ideal) * 100,
    onde throughput ideal = baseline * n (Aula).
    """
    ideal = throughput_baseline * n
    if ideal <= 0:
        return 0.0
    return 100.0 * throughput_com_n_nos / ideal


def disponibilidade_pct(sucessos: int, total: int) -> float:
    """Disponibilidade aproximada em % (1 - taxa de falha)."""
    if total <= 0:
        return 0.0
    return 100.0 * sucessos / total
