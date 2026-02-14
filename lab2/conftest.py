import pytest

@pytest.fixture
def cpfs_validos():
    return [
        "52998224725",   
        "12345678909",   
        "11144477735",   
        "39053344705",   
        "00000003291",   
    ]


@pytest.fixture
def cpfs_invalidos():

    return [
        "12345678900",   # Dígitos verificadores errados
        "11111111111",   # Todos iguais
        "1234567890",    # Menos de 11 dígitos
        "123456789012",  # Mais de 11 dígitos
        "abcdefghijk",   # Letras
        "",              # String vazia
        None,            # None
    ]
