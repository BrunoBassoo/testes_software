# Exercício 1 — Caminhos Independentes

## Código

```python
def verificar(n):
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"
```

---

# Grafo de Fluxo de Controle (GFC)

No Grafo de Fluxo de Controle:

- **Nós** representam blocos de comandos  
- **Arestas** representam o fluxo de execução do programa  

```mermaid
flowchart TD

A([Inicio])
B{n > 0}
C{n % 2 == 0}
D[return "Par positivo"]
E[return "Impar positivo"]
F{n < 0}
G[return "Negativo"]
H[return "Zero"]
I([Fim])

A --> B
B -- True --> C
C -- True --> D
C -- False --> E
B -- False --> F
F -- True --> G
F -- False --> H

D --> I
E --> I
G --> I
H --> I
```

---

# Complexidade Ciclomática

A complexidade ciclomática mede o número de caminhos independentes do programa.

Fórmula utilizada:

V(G) = número de decisões + 1

Decisões presentes no código:

1. `if n > 0`
2. `if n % 2 == 0`
3. `elif n < 0`

Cálculo:

V(G) = 3 + 1  
V(G) = **4**

Portanto, existem **4 caminhos independentes** no grafo.

---

# Caminhos Independentes

Um caminho independente é aquele que introduz pelo menos uma nova aresta no grafo de fluxo de controle.

Como V(G) = 4, existem **4 caminhos independentes**.

### Caminho 1

Inicio → n > 0 → n % 2 == 0 → "Par positivo" → Fim

### Caminho 2

Inicio → n > 0 → n % 2 != 0 → "Impar positivo" → Fim

### Caminho 3

Inicio → n > 0 (False) → n < 0 → "Negativo" → Fim

### Caminho 4

Inicio → n > 0 (False) → n < 0 (False) → "Zero" → Fim

---