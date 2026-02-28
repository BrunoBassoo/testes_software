import pytest
from hypothesis import given, strategies as st

from frete import calcular_frete


@pytest.fixture
def valor_baixo():
    return 100.0


@pytest.mark.parametrize(
    "peso,destino,esperado",
    [
        (0.5, "mesma", 10.0),
        (2.0, "mesma", 15.0),
        (10.0, "mesma", 25.0),
        (2.0, "outra", 22.5),
        (10.0, "internacional", 50.0),
    ],
)
# 5 casos de equivalencia
def test_classes_equivalencia(peso, destino, esperado, valor_baixo):
    assert calcular_frete(peso, destino, valor_baixo) == esperado


# 9 valores limites
@pytest.mark.parametrize(
    "peso, destino",
    [
        (0.999, "mesma"),
        (1.0, "mesma"),
        (1.001, "mesma"),
        (4.999, "mesma"),
        (5.0, "mesma"),
        (5.001, "mesma"),
        (19.999, "mesma"),
        (20.0, "mesma"),
    ],
)
def test_fronteiras(peso, destino, valor_baixo):
    if peso <= 1.0:
        base = 10.0
    elif peso <= 5.0:
        base = 15.0
    else:
        base = 25.0
    assert calcular_frete(peso, destino, valor_baixo) == round(base * 1.0, 2)


@pytest.mark.parametrize(
    "peso,destino,esperado",
    [
        (0.5, "mesma", 10.0),
        (0.5, "outra", 15.0),
        (0.5, "internacional", 20.0),
        (3.0, "mesma", 15.0),
        (3.0, "outra", 22.5),
        (10.0, "internacional", 50.0),
    ],
)
# 6 tabelas de decisao
def test_tabela_decisao(peso, destino, esperado, valor_baixo):
    assert calcular_frete(peso, destino, valor_baixo) == esperado


# 2 entradas inválidas
def test_entradas_invalidas():
    with pytest.raises(ValueError):
        calcular_frete(0.0, "mesma", 50.0)
    with pytest.raises(ValueError):
        calcular_frete(-1.0, "mesma", 50.0)
    with pytest.raises(ValueError):
        calcular_frete(10.0, "x", 50.0)

def test_frete_gratis_para_pedidos_acima_de_200():
    assert calcular_frete(5.0, "mesma", 200.0) == 0.0
    assert calcular_frete(5.0, "outra", 250.0) == 0.0


#========= Hypothesis (3 propriedades) ========= #
@given(
    peso=st.floats(min_value=0.0001, max_value=20.0, allow_nan=False, allow_infinity=False),
    destino=st.sampled_from(["mesma", "outra", "internacional"]),
    valor=st.floats(min_value=0.0, max_value=199.99, allow_nan=False, allow_infinity=False),
)
# valor negativo
def test_frete_nao_negativo(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) >= 0.0


@given(
    peso=st.floats(min_value=0.0001, max_value=20.0, allow_nan=False, allow_infinity=False),
    destino=st.sampled_from(["mesma", "outra", "internacional"]),
    valor=st.floats(min_value=200.0, max_value=10000.0, allow_nan=False, allow_infinity=False),
)
# frete gratis
def test_frete_gratis_propriedade(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) == 0.0


@given(
    peso=st.floats(min_value=0.0001, max_value=20.0, allow_nan=False, allow_infinity=False),
    valor=st.floats(min_value=0.0, max_value=199.99, allow_nan=False, allow_infinity=False),
)
# teste regiao maior ou igual
def test_outra_regiao_maior_ou_igual_mesma(peso, valor):
    f_mesma = calcular_frete(peso, "mesma", valor)
    f_outra = calcular_frete(peso, "outra", valor)
    f_int = calcular_frete(peso, "internacional", valor)
    assert f_outra >= f_mesma
    assert f_int >= f_outra
