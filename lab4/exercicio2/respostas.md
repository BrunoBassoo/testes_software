# Exercício 2 — Cobertura de Comandos e Ramos


# Grafo de Fluxo de Controle (GFC)

No Grafo de Fluxo de Controle:

- **Nós** representam blocos de comandos  
- **Arestas** representam o fluxo de execução do programa  

```mermaid
flowchart TD

A([Inicio])
B{x > 100}
C[return "Alto"]
D{x > 50}
E[return "Medio"]
F[return "Baixo"]
G([Fim])

A --> B
B -- True --> C
B -- False --> D
C --> G
D -- True --> E
D -- False --> F
E --> G
F --> G
```

---

# Complexidade Ciclomática

A complexidade ciclomática mede o número de caminhos independentes do programa.

Fórmula:

V(G) = número de decisões + 1

Decisões no código:

1. `if x > 100`
2. `if x > 50`

Cálculo:

V(G) = 2 + 1  
V(G) = **3**

Portanto existem **3 caminhos independentes**.

---

# Caminhos Independentes

Um caminho independente introduz pelo menos uma nova aresta no grafo.

Como **V(G) = 3**, existem **3 caminhos independentes**.

### Caminho 1

Inicio → x > 100 → "Alto" → Fim

### Caminho 2

Inicio → x > 100 (False) → x > 50 → "Medio" → Fim

### Caminho 3

Inicio → x > 100 (False) → x > 50 (False) → "Baixo" → Fim

---

# Casos de Teste

## Cobertura de Comandos (C0)

Cobertura de comandos exige que **todos os comandos do programa sejam executados pelo menos uma vez**.

Comandos a serem executados:

- `return "Alto"`
- `return "Medio"`
- `return "Baixo"`

Conjunto mínimo de testes:

| Caso de Teste | Entrada | Saída Esperada |
|---|---|---|
| CT1 | x = 120 | "Alto" |
| CT2 | x = 60 | "Medio" |
| CT3 | x = 30 | "Baixo" |

Portanto, para **C0 são necessários 3 testes**, pois cada retorno precisa ser executado ao menos uma vez.

---

## Cobertura de Ramos (C1) -- true e false (ir pela logica do if)

Cobertura de ramos exige que **cada decisão lógica seja avaliada como verdadeira e falsa pelo menos uma vez**.

Decisões:

1. `x > 100`
2. `x > 50`

Para cobrir todos os ramos:

| Caso de Teste | x > 100 | x > 50 | Saída |
|---|---|---|---|
| CT1 | True | — | Alto |
| CT2 | False | True | Medio |
| CT3 | False | False | Baixo |

Assim:

- `x > 100` é testado como **True e False**
- `x > 50` é testado como **True e False**

Logo, **o número mínimo de casos de teste para C1 é 3**, que é igual à **complexidade ciclomática V(G) = 3**.

---