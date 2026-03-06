from classificar import classificar

def test_alto():
    assert classificar(120) == "Alto"

def test_medio():
    assert classificar(60) == "Medio"

def test_baixo():
    assert classificar(30) == "Baixo"