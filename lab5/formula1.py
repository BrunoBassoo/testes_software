"""
Módulo temático de Fórmula 1 - Aula 05 (Testes de Mutação).
Funções para cálculos comuns no contexto de corridas.
"""

# Sistema de pontuação atual da F1 (2022+): 1º=25, 2º=18, 3º=15, ..., 10º=1
PONTOS_POR_POSICAO = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1
}


def pontos_por_posicao(posicao):
    """
    Retorna os pontos que um piloto ganha por ter terminado em determinada posição.
    Posições 1 a 10 recebem pontos; acima de 10 retorna 0.
    """
    if posicao >= 1 and posicao <= 10:
        return PONTOS_POR_POSICAO[posicao]
    return 0


def tempo_total_pit_stop(segundos_base, trocou_pneus):
    """
    Calcula o tempo total de um pit stop.
    segundos_base: tempo mínimo (parada na box)
    trocou_pneus: se True, adiciona 4 segundos para troca de pneus.
    """
    total = segundos_base
    if trocou_pneus:
        total = segundos_base + 4
    return total


def velocidade_media_kmh(distancia_km, tempo_horas):
    """
    Calcula a velocidade média em km/h.
    distancia_km: distância percorrida em quilômetros
    tempo_horas: tempo em horas (pode ser decimal, ex: 1.5 = 1h30)
    """
    if tempo_horas <= 0:
        return 0.0
    return distancia_km / tempo_horas


def volta_valida(tempo_volta_seg, limite_seg):
    """
    Verifica se uma volta está dentro do limite permitido (ex: volta de qualificação).
    Retorna True se tempo_volta_seg <= limite_seg.
    """
    return tempo_volta_seg <= limite_seg


def diferenca_tempo(volta1_seg, volta2_seg):
    """
    Retorna a diferença de tempo entre duas voltas (em segundos).
    Valor positivo significa que volta1 foi mais lenta que volta2.
    """
    return volta1_seg - volta2_seg
