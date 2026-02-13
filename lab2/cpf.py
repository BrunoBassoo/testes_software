import re


def validar_cpf(cpf: str) -> bool:

    # Verificação inicial
    if not isinstance(cpf, str):
        return False

    # Remove qualquer caractere que não seja número
    cpf = re.sub(r"\D", "", cpf)

    # Deve ter 11 dígitos
    if len(cpf) != 11:
        return False

    # trata sequencias iguais
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    if digito1 != int(cpf[9]):
        return False

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    if digito2 != int(cpf[10]):
        return False

    return True


def formatar_cpf(cpf: str) -> str:


    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")

    # Remove formatação se existir
    cpf = re.sub(r"\D", "", cpf)

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
