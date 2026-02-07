import pytest

from sistema_notas import (
    validar_nota,
    calcular_media,
    obter_situacao,
    calcular_estatisticas,
    normalizar_notas,
)


def test_validar_nota_valida():
    assert validar_nota(0)
    assert validar_nota(10)
    assert validar_nota(5.5)


def test_validar_nota_invalida():
    with pytest.raises(ValueError):
        validar_nota(-1)
    with pytest.raises(ValueError):
        validar_nota(11)
    with pytest.raises(ValueError):
        validar_nota("a")


def test_calcular_media():
    assert calcular_media([5, 7]) == 6


def test_calcular_media_vazia():
    with pytest.raises(ValueError):
        calcular_media([])


def test_obter_situacao():
    assert obter_situacao(7) == "Aprovado!"
    assert obter_situacao(5) == "Recuperação!"
    assert obter_situacao(4.9) == "Reprovado!"
    assert obter_situacao(10) == "Aprovado!"
    assert obter_situacao(0) == "Reprovado!"


def test_calcular_estatisticas():
    notas = [10, 5, 4]
    est = calcular_estatisticas(notas)
    assert est["maior"] == 10
    assert est["menor"] == 4
    assert pytest.approx(est["media"]) == (10 + 5 + 4) / 3
    assert est["aprovados"] == 1
    assert est["recuperacao"] == 1
    assert est["reprovados"] == 1


def test_normalizar_notas():
    assert normalizar_notas([5, 10], nota_maxima=10) == [5.0, 10.0]
    assert normalizar_notas([50, 100], nota_maxima=100) == [5.0, 10.0]
    assert normalizar_notas([0, 50, 100], nota_maxima=100) == [0.0, 5.0, 10.0]
    assert normalizar_notas([2.5, 7.5], nota_maxima=10) == [2.5, 7.5]


def test_normalizar_invalid():
    with pytest.raises(ValueError):
        normalizar_notas([11], nota_maxima=10)
    with pytest.raises(ValueError):
        normalizar_notas([5], nota_maxima=0)


def test_estatisticas_exemplo():
    notas = [5, 7, 8, 4, 6]
    estatisticas = calcular_estatisticas(notas)
    assert pytest.approx(estatisticas["media"]) == 6.0
    assert estatisticas["maior"] == 8
    assert estatisticas["menor"] == 4
    assert estatisticas["aprovados"] == 2
    assert estatisticas["recuperacao"] == 2
    assert estatisticas["reprovados"] == 1



def test_normalizar_com_escala_personalizada():
    notas = [5, 7, 8, 4, 6]
    notas_normalizadas = normalizar_notas(notas, nota_maxima=8)
    assert notas_normalizadas == [6.25, 8.75, 10.0, 5.0, 7.5]
    

def test_validar_nota_float_precision():
    assert validar_nota(3.3333)


def test_calcular_media_com_entrada_invalida_levanta():
    with pytest.raises(ValueError):
        calcular_media([5, "x"])


def test_calcular_media_com_none_levanta():
    with pytest.raises(ValueError):
        calcular_media([5, None])


def test_obter_situacao_tipo_invalido_levanta():
    with pytest.raises(ValueError):
        obter_situacao("invalid")


def test_obter_situacao_boundaries():
    assert obter_situacao(5.0) == "Recuperação!"
    assert obter_situacao(7.0) == "Aprovado!"


def test_calcular_estatisticas_valor_unico():
    est = calcular_estatisticas([7])
    assert est["media"] == 7
    assert est["maior"] == 7
    assert est["menor"] == 7
    assert est["aprovados"] == 1
    assert est["recuperacao"] == 0
    assert est["reprovados"] == 0


def test_calcular_estatisticas_com_invalido_levanta():
    with pytest.raises(ValueError):
        calcular_estatisticas([5, "a"])


def test_normalizar_ordem_preservada():
    notas = [1, 10, 5]
    assert normalizar_notas(notas, nota_maxima=10) == [1.0, 10.0, 5.0]


def test_normalizar_com_floats_precisao():
    assert normalizar_notas([2.5], nota_maxima=5) == [5.0]


def test_normalizar_input_negativo_levanta():
    with pytest.raises(ValueError):
        normalizar_notas([-1], nota_maxima=10)


def test_normalizar_input_nao_numerico_levanta():
    with pytest.raises(ValueError):
        normalizar_notas(["a"], nota_maxima=10)


def test_calcular_media_lista_grande():
    notas = list(range(11)) * 100  # 0..10 repeated
    avg = calcular_media(notas)
    assert pytest.approx(avg) == sum(notas) / len(notas)


def test_calcular_media_precisao():
    assert calcular_media([1, 2]) == 1.5


def test_estatisticas_contagens_somam():
    import random
    random.seed(0)
    notas = [random.randint(0, 10) for _ in range(50)]
    est = calcular_estatisticas(notas)
    total = est["aprovados"] + est["recuperacao"] + est["reprovados"]
    assert total == len(notas)

