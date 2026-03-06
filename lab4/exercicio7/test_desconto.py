import pytest
from desconto import desconto


def test_sem_desconto():
    assert desconto(100, False) == 100


def test_com_desconto():
    assert desconto(100, True) == 80


def test_valor_minimo_sem_vip():
    assert desconto(40, False) == 50


def test_valor_minimo_com_vip():
    assert desconto(40, True) == 50