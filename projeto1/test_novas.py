from sistema_notas import *

def test_nota_valida_inteira():
    assert validar_nota(5) == True
    assert validar_nota(0) == True
    assert validar_nota(10) == True
    assert validar_nota("a") == False

def test_nota_invalida_negativa():
    assert validar_nota(-1) == False

def test_nota_invalida_acima_dez():
    assert validar_nota(11) == False

def test_estatisticas():
    notas = [5, 7, 8, 4, 6]
    estatisticas = calcular_estatisticas(notas)
    assert estatisticas["media"] == 6.0
    assert estatisticas["maior"] == 8
    assert estatisticas["menor"] == 4
    assert estatisticas["aprovados"] == 3
    assert estatisticas["recuperacao"] == 1
    assert estatisticas["reprovados"] == 1

def test_normalizar_notas():
    notas = [5, 7, 8, 4, 6]
    notas_normalizadas = normalizar_notas(notas, nota_maxima=8)
    assert notas_normalizadas == [6.25, 8.75, 10.0, 5.0, 7.5]

test_normalizar_notas()
test_estatisticas()
test_nota_invalida_acima_dez()