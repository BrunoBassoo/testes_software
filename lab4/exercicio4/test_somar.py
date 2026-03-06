from somar_ate import somar_ate

def test_laco_ignorado():
    assert somar_ate(0) == 0

def test_laco_uma_vez():
    assert somar_ate(1) == 0

def test_laco_varias_vezes():
    assert somar_ate(4) == 6