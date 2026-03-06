"""
MUTANTE 1 - pontos_por_posicao: troca <= por < em "posicao <= 10"
Original: if posicao >= 1 and posicao <= 10:
Mutante:  if posicao >= 1 and posicao < 10:
Efeito: para posicao==10 retorna 0 em vez de 1 → deve ser MORTO por test_pontos_decimo_lugar
"""
# Sistema de pontuação atual da F1 (2022+): 1º=25, 2º=18, 3º=15, ..., 10º=1
PONTOS_POR_POSICAO = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1
}


def pontos_por_posicao(posicao):
    if posicao >= 1 and posicao < 10:  # MUTAÇÃO: <= virou <
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
    return volta1_seg - volta2_seg
