def desconto(preco, cliente_vip):
    total = preco

    if cliente_vip:
        desconto = preco * 0.2
        total = preco - desconto

    if total < 50:
        total = 50

    return total