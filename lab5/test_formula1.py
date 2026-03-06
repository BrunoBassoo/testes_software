"""
Testes unitários para o módulo formula1 - Aula 05 (Testes de Mutação).
Execute com: pytest test_formula1.py -v
Para mutação: mutmut run
"""
import pytest
from formula1 import (
    pontos_por_posicao,
    tempo_total_pit_stop,
    velocidade_media_kmh,
    volta_valida,
    diferenca_tempo,
)


# --- pontos_por_posicao ---
def test_pontos_campeao():
    assert pontos_por_posicao(1) == 25


def test_pontos_segundo_lugar():
    assert pontos_por_posicao(2) == 18


def test_pontos_decimo_lugar():
    assert pontos_por_posicao(10) == 1


def test_pontos_fora_do_top10():
    assert pontos_por_posicao(11) == 0
    assert pontos_por_posicao(20) == 0


def test_pontos_posicao_zero():
    assert pontos_por_posicao(0) == 0


def test_pontos_posicao_negativa():
    assert pontos_por_posicao(-1) == 0


# --- tempo_total_pit_stop ---
def test_pit_stop_sem_troca():
    assert tempo_total_pit_stop(3.0, False) == 3.0


def test_pit_stop_com_troca():
    assert tempo_total_pit_stop(3.0, True) == 7.0


def test_pit_stop_base_diferente():
    assert tempo_total_pit_stop(2.5, True) == 6.5


# --- velocidade_media_kmh ---
def test_velocidade_media_basica():
    assert velocidade_media_kmh(100, 1.0) == 100.0


def test_velocidade_media_meia_hora():
    assert velocidade_media_kmh(50, 0.5) == 100.0


def test_velocidade_media_tempo_zero():
    assert velocidade_media_kmh(100, 0) == 0.0


def test_velocidade_media_tempo_negativo():
    assert velocidade_media_kmh(100, -1) == 0.0


# --- volta_valida ---
def test_volta_valida_no_limite():
    assert volta_valida(90.0, 90.0) is True


def test_volta_valida_abaixo_limite():
    assert volta_valida(88.0, 90.0) is True


def test_volta_invalida_acima_limite():
    assert volta_valida(91.0, 90.0) is False


# --- diferenca_tempo ---
def test_diferenca_volta1_mais_lenta():
    assert diferenca_tempo(95.0, 90.0) == 5.0


def test_diferenca_volta1_mais_rapida():
    assert diferenca_tempo(90.0, 95.0) == -5.0


def test_diferenca_voltas_iguais():
    assert diferenca_tempo(90.0, 90.0) == 0.0
