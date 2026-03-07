# Exercício 1 — Caminhos Independentes

# Grafo de Fluxo de Controle (GFC)

No Grafo de Fluxo de Controle:

- **Nós** representam blocos de comandos  
- **Arestas** representam o fluxo de execução do programa  

```mermaid
flowchart TD

A([Início])
B{"n > 0?"}
C{"n % 2 == 0?"}
D["return Par positivo"]
E["return Ímpar positivo"]
F{"n < 0?"}
G["return Negativo"]
H["return Zero"]
I([Fim])

A --> B
B -- Sim --> C
C -- Sim --> D
C -- Não --> E
B -- Não --> F
F -- Sim --> G
F -- Não --> H

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
