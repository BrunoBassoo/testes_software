def validar_nota(nota):
    if not isinstance(nota, (int, float)):
        raise ValueError("Nota deve ser numérica.")
    if 0 <= nota <= 10:
        return True
    raise ValueError("Nota não está de acordo com a regra!")


def calcular_media(notas):
    if not notas:
        raise ValueError("Lista de notas vazia.")

    n_total = 0
    n_validas = 0
    for nota in notas:
        if validar_nota(nota):
            n_total += nota
            n_validas += 1

    if n_validas == 0:
        raise ValueError("Nenhuma nota válida.")

    return n_total / n_validas

   
def obter_situacao(media):
    if not isinstance(media, (int, float)):
        raise ValueError("Média inválida!")
    if not (0 <= media <= 10):
        raise ValueError("Média inválida!")

    if media >= 7.0:
        return "Aprovado!"
    if media >= 5.0:
        return "Recuperação!"
    return "Reprovado!"
    
def calcular_estatisticas(notas):
    if not notas:
        raise ValueError("Lista de notas vazia.")

    media = calcular_media(notas)
    maior = max(notas)
    menor = min(notas)

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for nota in notas:
        situacao = obter_situacao(nota)
        if situacao == "Aprovado!":
            aprovados += 1
        elif situacao == "Recuperação!":
            recuperacao += 1
        else:
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
        if not isinstance(nota, (int, float)):
            raise ValueError(f"Nota {nota} deve ser numérica.")
        if not (0 <= nota <= nota_maxima):
            raise ValueError(f"Nota {nota} é inválida para a escala 0-{nota_maxima}.")

        nota_normalizada = (nota / nota_maxima) * 10
        notas_normalizadas.append(nota_normalizada)

    return notas_normalizadas



