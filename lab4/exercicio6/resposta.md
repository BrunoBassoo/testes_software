# Exercício 6 – Teste Completo (Integrador)

# 1. Grafo de Fluxo de Controle (GFC)

```mermaid
flowchart TD

A[Início] --> B[total = 0]
B --> C[for n in numeros]

C --> D{n > 0 e n % 2 == 0?}

D -->|Sim| E[total += n]
D -->|Não| F{n < 0?}

F -->|Sim| G[total -= 1]
F -->|Não| H[continue]

H --> C

E --> I{total > 10?}
G --> I

I -->|Sim| J[return "Acima"]
I -->|Não| C

C --> K[Fim do loop]
K --> L[return "Abaixo"]
```

---

# 2. Complexidade Ciclomática

A complexidade ciclomática mede a quantidade de caminhos independentes existentes no código.

Fórmula utilizada:

```
V(G) = número de decisões + 1
```

Decisões presentes no código:

1. Estrutura `for`
2. Condição `if n > 0 and n % 2 == 0`
3. Condição `elif n < 0`
4. Condição `if total > 10`

Portanto:

```
V(G) = 4 + 1
V(G) = 5
```

Logo, **existem 5 caminhos independentes possíveis no programa.**

---

# 3. Caminhos Independentes

Os caminhos independentes representam execuções diferentes do programa que percorrem partes distintas do fluxo.

### Caminho 1 – Lista vazia (loop não executa)

```
Início → total=0 → for não executa → return "Abaixo"
```

---

### Caminho 2 – Número positivo par que não ultrapassa o limite

```
Início → total=0 → for → n positivo par → total += n → total ≤ 10 → loop termina → return "Abaixo"
```

Exemplo:

```
[2,4]
```

---

### Caminho 3 – Número negativo

```
Início → total=0 → for → n < 0 → total -= 1 → total ≤ 10 → loop continua → return "Abaixo"
```

Exemplo:

```
[-3]
```

---

### Caminho 4 – Número que ativa o continue

```
Início → total=0 → for → n positivo ímpar → continue → volta ao loop → return "Abaixo"
```

Exemplo:

```
[3]
```

---

### Caminho 5 – Soma ultrapassa 10

```
Início → total=0 → for → n positivo par → total += n → total > 10 → return "Acima"
```

Exemplo:

```
[6,6]
```

---

# 4. Casos de Teste

## Objetivo
Cobrir:

- Cobertura de comandos (C0)
- Cobertura de ramos (C1)
- Cobertura de condição (CC)
- Comportamento do laço (0, 1 e várias iterações)

---

## Casos de Teste Propostos

| CT | Entrada | Caminho coberto | Saída esperada |
|---|---|---|---|
| CT1 | [] | loop não executa | "Abaixo" |
| CT2 | [2,4] | positivo par sem ultrapassar limite | "Abaixo" |
| CT3 | [-1] | número negativo | "Abaixo" |
| CT4 | [3] | caminho do continue | "Abaixo" |
| CT5 | [6,6] | soma ultrapassa 10 | "Acima" |

Esses testes cobrem:

- todos os ramos das condições
- todos os comandos do código
- diferentes comportamentos do laço

---

# 5. Def-Use (Fluxo de Dados)

Variável principal analisada: **total**

### Definições (Def)

```
total = 0
total += n
total -= 1
```

### Usos (Use)

```
if total > 10
return "Abaixo"
```

### Fluxos principais

1. `total = 0` → usado na condição `total > 10`
2. `total += n` → usado em `total > 10`
3. `total -= 1` → usado em `total > 10`

Os casos de teste CT2, CT3 e CT5 garantem cobertura desses fluxos de dados.
