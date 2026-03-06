"""
MUTANTE 5 - diferenca_tempo: troca - por +
Original: return volta1_seg - volta2_seg
Mutante:  return volta1_seg + volta2_seg
Efeito: resultado errado → MORTO por test_diferenca_volta1_mais_lenta e outros
"""
PONTOS_POR_POSICAO = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1
}


def pontos_por_posicao(posicao):
    if posicao >= 1 and posicao <= 10:
        return PONTOS_POR_POSICAO[posicao]
    return 0


def tempo_total_pit_stop(segundos_base, trocou_pneus):
    total = segundos_base
    if trocou_pneus:
        total = segundos_base + 4
    return total


def velocidade_media_kmh(distancia_km, tempo_horas):
    if tempo_horas <= 0:
        return 0.0
    return distancia_km / tempo_horas


def volta_valida(tempo_volta_seg, limite_seg):
    return tempo_volta_seg <= limite_seg


def diferenca_tempo(volta1_seg, volta2_seg):
    return volta1_seg + volta2_seg  # MUTAÇÃO: - virou +
