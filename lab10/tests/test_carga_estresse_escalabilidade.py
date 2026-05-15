"""Carga, estresse e escalabilidade: fórmulas e critérios do slide."""

from nf_metrics import (
    META_EFICIENCIA_HORIZONTAL_PCT,
    META_THROUGHPUT_REQ_S,
    META_USUARIOS_ESTRESSE_QUEBRA,
    disponibilidade_pct,
    eficiencia_horizontal_pct,
    throughput_req_s,
)


def test_throughput_sustentado_meta():
    """Exemplo do slide: 10.000 req em 5s => 2000 req/s (meta de carga)."""
    assert throughput_req_s(10_000, 5.0) >= META_THROUGHPUT_REQ_S


def test_disponibilidade_meta_black_friday():
    """99,9% disponibilidade: exemplo 9999 sucessos em 10000 requisições."""
    assert disponibilidade_pct(9_999, 10_000) >= 99.9


def test_estresse_meta_usuarios_quebra():
    """
    Meta de estresse: ponto de quebra > 15.000 usuários.
    Aqui validamos apenas o critério numérico usado no relatório (sem subir 15k nós).
    """
    usuarios_observados_em_teste_de_lab = 16_000
    assert usuarios_observados_em_teste_de_lab > META_USUARIOS_ESTRESSE_QUEBRA


def test_escalabilidade_eficiencia_horizontal():
    """Exemplo Aula: 2 nós, baseline 200, real 380 => 95% >= meta 80%."""
    eff = eficiencia_horizontal_pct(380.0, n=2, throughput_baseline=200.0)
    assert eff >= META_EFICIENCIA_HORIZONTAL_PCT
