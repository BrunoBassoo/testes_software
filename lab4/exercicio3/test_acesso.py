from acesso import acesso

def test_permitido():
    assert acesso(20, True) == "Permitido"

def test_negado_sem_membro():
    assert acesso(20, False) == "Negado"

def test_negado_menor_membro():
    assert acesso(16, True) == "Negado"

def test_negado_menor_nao_membro():
    assert acesso(16, False) == "Negado"