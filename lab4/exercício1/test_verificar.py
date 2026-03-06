import pytest
from verificar import verificar


def test_par_positivo():
    # Caminho: n > 0 -> n % 2 == 0
    assert verificar(4) == "Par positivo"


def test_impar_positivo():
    # Caminho: n > 0 -> n % 2 != 0
    assert verificar(3) == "Impar positivo"


def test_negativo():
    # Caminho: n > 0 False -> n < 0 True
    assert verificar(-2) == "Negativo"


def test_zero():
    # Caminho: n > 0 False -> n < 0 False
    assert verificar(0) == "Zero"