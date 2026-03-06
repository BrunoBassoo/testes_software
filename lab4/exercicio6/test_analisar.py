import pytest
from analisar import analisar


def test_lista_vazia():
    assert analisar([]) == "Abaixo"


def test_positivo_par_sem_ultrapassar():
    assert analisar([2,4]) == "Abaixo"


def test_numero_negativo():
    assert analisar([-1]) == "Abaixo"


def test_continue_impar():
    assert analisar([3]) == "Abaixo"


def test_ultrapassa_limite():
    assert analisar([6,6]) == "Acima"