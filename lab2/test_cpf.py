import pytest
import conftest
from cpf import validar_cpf, formatar_cpf


# ============ TESTES ============ #

@pytest.mark.parametrize("cpf", [
    "52998224725",   # cpf valido padrao
    "00000000191",   # *  *  com zeros
])
def test_validar_cpf_valido_retorna_true(cpf):
    # Arrange
    cpf_teste = cpf

    # Act
    resultado = validar_cpf(cpf_teste)

    # Assert
    assert resultado is True


@pytest.mark.parametrize("cpf", [
    "12345678900",   # Dígitos verificadores errados
    "11111111111",   # Todos iguais
    "1234567890",    # Menos de 11 dígitos
    "123456789012",  # Mais de 11 dígitos
    "abcdefghijk",   # Letras
    "",              # String vazia
    None,            # None
])
def test_validar_cpf_invalido_retorna_false(cpf):
    # Arrange
    cpf_teste = cpf

    # Act
    resultado = validar_cpf(cpf_teste)

    # Assert
    assert resultado is False


# ============ FORMATAÇÃO ============ #

def test_formatar_cpf_valido_retorna_formatado():
    # Arrange
    cpf = "52998224725"

    validar_cpf(cpf) # validar cpf para garantir que é válido
    esperado = "529.982.247-25"

    # Act
    resultado = formatar_cpf(cpf)

    # Assert
    assert resultado == esperado


def test_formatar_cpf_valido_com_zeros():
    # Arrange
    cpf = "00000000191" # formatar válido
    validar_cpf(cpf) # validar cpf para garantir que é válido
    esperado = "000.000.001-91"

    # Act
    resultado = formatar_cpf(cpf)

    # Assert
    assert resultado == esperado


@pytest.mark.parametrize("cpf_invalido", [
    "12345678900",
    "11111111111", # iguais
    "abcdefghijk", # cpf invalido
    "", # teste string vazia
    "111111", # teste com menos de 11 digitos
    "31938329328349", # teste com mais de 11 digitos
    None,
])
def test_formatar_cpf_invalido_levanta_value_error(cpf_invalido):
    # Arrange
    cpf = cpf_invalido # teste formatar invalido

    # Act & Assert
    with pytest.raises(ValueError): 
        formatar_cpf(cpf)

