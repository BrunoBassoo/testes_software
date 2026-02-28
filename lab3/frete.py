from typing import Union


def calcular_frete(peso, destino, valor_pedido) -> float:
    try:
        peso = float(peso)
        valor = float(valor_pedido)
        destino = str(destino)
    except Exception:
        raise ValueError("Argumentos inválidos. " + str(Exception))

    if peso <= 0:
        raise ValueError("'peso' deve ser maior que zero")
    if peso > 20:
        raise ValueError("'peso' acima do permitido (mais de 20 kg)")
    if valor < 0:
        raise ValueError("'valor_pedido' não pode ser negativo")

    if valor >= 200.0:
        return 0.0

    if peso <= 1.0:
        base = 10.0
    elif peso <= 5.0:
        base = 15.0
    else:
        base = 25.0

    if destino == "mesma":
        mult = 1.0
    elif destino == "outra":
        mult = 1.5
    elif destino == "internacional":
        mult = 2.0
    else:
        raise ValueError("'destino' inválido: use mesma, outra, internacional")

    frete = base * mult
    return round(frete, 2)
