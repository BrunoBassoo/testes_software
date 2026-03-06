# Exercício 3 — Cobertura de Condição (CC)

# Grafo de Fluxo de Controle (GFC)

No Grafo de Fluxo de Controle:

- **Nós** representam blocos de comandos  
- **Arestas** representam o fluxo de execução do programa  

```mermaid
flowchart TD

A([Inicio])
B{idade >= 18 AND membro}
C[return "Permitido"]
D[return "Negado"]
E([Fim])

A --> B
B -- True --> C
B -- False --> D
C --> E
D --> E
```

---

# Complexidade Ciclomática

Fórmula:

V(G) = número de decisões + 1

Decisões no código:

1. `idade >= 18 and membro`

Portanto:

V(G) = 1 + 1  
V(G) = **2**

Logo, existem **2 caminhos independentes**.

---

# Caminhos Independentes

### Caminho 1

Inicio → condição True → "Permitido" → Fim

### Caminho 2

Inicio → condição False → "Negado" → Fim

---

# Cobertura de Condição (CC)

Cobertura de Condição exige que **cada subcondição atômica seja avaliada como verdadeira e falsa pelo menos uma vez**.

Subcondições da expressão:

1. `idade >= 18`
2. `membro`

Todas as combinações possíveis:

| CT | idade >= 18 | membro | Entrada | Resultado |
|----|-------------|--------|--------|-----------|
| CT1 | True | True | (20, True) | Permitido |
| CT2 | True | False | (20, False) | Negado |
| CT3 | False | True | (16, True) | Negado |
| CT4 | False | False | (16, False) | Negado |

Portanto, **para Cobertura de Condição (CC) são necessários 4 casos de teste**, pois existem **2² combinações possíveis das condições**.

---

# Cobertura de Ramos (C1)

Cobertura de Ramos exige que **cada decisão seja avaliada como verdadeira e falsa pelo menos uma vez**.

Como há apenas uma decisão (`idade >= 18 and membro`), precisamos de:

| CT | Entrada | Resultado |
|----|--------|-----------|
| CT1 | (20, True) | Permitido |
| CT2 | (16, True) | Negado |

Assim:

- condição avaliada como **True**
- condição avaliada como **False**

Logo, **C1 precisa de apenas 2 casos de teste**.

---

# Comparação entre CC e C1

| Critério | Número de Testes |
|--------|------------------|
| C1 (Ramos) | 2 |
| CC (Condição) | 4 |

Eles **diferem** porque:

- **C1** verifica apenas o resultado da decisão (True ou False).
- **CC** exige que **cada subcondição individual** seja testada como verdadeira e falsa.

Assim, **CC é mais forte que C1**, pois explora todas as combinações possíveis das condições.