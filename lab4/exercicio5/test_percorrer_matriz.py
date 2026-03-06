from percorrer_matriz import percorrer_matriz

def test_lacos_ignorados(capsys):
    percorrer_matriz(0, 0)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_apenas_laco_interno_ignorado(capsys):
    percorrer_matriz(2, 0)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_um_laco_uma_vez_outro_varias(capsys):
    percorrer_matriz(1, 3)
    captured = capsys.readouterr()
    linhas = captured.out.strip().split("\n")
    assert len(linhas) == 3

def test_ambos_varias_vezes(capsys):
    percorrer_matriz(2, 2)
    captured = capsys.readouterr()
    linhas = captured.out.strip().split("\n")
    assert len(linhas) == 4