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

def normalizar_notas(notas, nota_maxima=10):
    if nota_maxima <= 0:
        raise ValueError("Nota máxima deve ser maior que zero.")
    
    notas_normalizadas = []
    for nota in notas:
        if validar_nota(nota):
            nota_normalizada = (nota / nota_maxima) * 10
            notas_normalizadas.append(nota_normalizada)
        else:
            raise ValueError(f"Nota {nota} é invalida e n pode ser normalizada.")
    
    return notas_normalizadas



