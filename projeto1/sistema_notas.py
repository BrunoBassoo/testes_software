def validar_nota(nota):
    if (nota >= 0 or nota <= 10):
        return True
    raise ValueError("Nota não está de acordo com a regra!")


def calcular_media(notas):
    n_validas = 0
    n_total = 0
    for i in notas:
        if(validar_nota(notas[i])):
            n_total += notas[i]
            n_validas += 1
    return f"A média é: {(n_total / n_validas)}"

   
def obter_situacao(media):
    if validar_nota(media):
        if media >= 7.0:
            return "Aprovado!"
        if media >= 5.0:
            return "Recuperação!"
        return "Reprovado!"
    
    raise ValueError("Média inválida!")
    
def calcular_estatisticas(notas):
    media = calcular_media(notas)

    maior = notas[0]
    menor = notas[0]

    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for nota in notas:
        situacao = obter_situacao(nota)
        if situacao == "Aprovado!":
            aprovados += 1
        elif situacao == "Recuperação!":
            recuperacao += 1
        elif situacao == "Reprovado!":
            reprovados += 1

    estatisticas = {
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "recuperacao": recuperacao,
        "reprovados": reprovados
    }

    return estatisticas




calcular_estatisticas([1,2,3,4,5,5,5,6,7,2,1,5])