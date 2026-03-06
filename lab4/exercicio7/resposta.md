# Exercício 7 – Fluxo de Dados

# 1. Definições e Usos das Variáveis

Na análise de **fluxo de dados**, identificamos:

- **Def (Definition)** → ponto onde a variável recebe valor  
- **Use (Usage)** → ponto onde a variável é utilizada

Os usos podem ser:

- **C-use** → uso computacional  
- **P-use** → uso em condição (predicado)

---

## Variável `preco`

### Definição

```
preco → parâmetro da função
```

### Usos

```
total = preco
desconto = preco * 0.2
total = preco - desconto
```

Todos são **C-use**.

---

## Variável `cliente_vip`

### Definição

```
cliente_vip → parâmetro da função
```

### Uso

```
if cliente_vip
```

Tipo:

```
P-use
```

---

## Variável `desconto`

### Definição

```
desconto = preco * 0.2
```

### Uso

```
total = preco - desconto
```

Tipo:

```
C-use
```

---

## Variável `total`

### Definições

```
total = preco
total = preco - desconto
total = 50
```

### Usos

```
if total < 50
return total
```

Tipos:

```
if total < 50 → P-use
return total → C-use
```

---

# 2. Pares Def-Use (DU-Pairs)

Agora listamos os pares **Def → Use** possíveis sem redefinição intermediária.

---

## Para `preco`

```
(preco parâmetro) → total = preco
(preco parâmetro) → desconto = preco * 0.2
(preco parâmetro) → total = preco - desconto
```

---

## Para `cliente_vip`

```
(cliente_vip parâmetro) → if cliente_vip
```

---

## Para `desconto`

```
desconto = preco * 0.2 → total = preco - desconto
```

---

## Para `total`

```
total = preco → if total < 50
total = preco → return total

total = preco - desconto → if total < 50
total = preco - desconto → return total

total = 50 → return total
```

---

# 3. Casos de Teste para All-Defs

O critério **All-Defs** exige que **cada definição alcance pelo menos um uso**.

### Casos mínimos

| CT | preco | cliente_vip | Caminho | Resultado |
|---|---|---|---|---|
| CT1 | 100 | False | sem desconto | 100 |
| CT2 | 100 | True | aplica desconto | 80 |
| CT3 | 40 | False | ativa mínimo 50 | 50 |

Cobertura obtida:

- definição `total = preco`
- definição `desconto = preco * 0.2`
- definição `total = preco - desconto`
- definição `total = 50`

---

# 4. Casos de Teste para All-Uses

O critério **All-Uses** exige que **cada definição seja ligada a todos os seus usos possíveis**.

### Conjunto de testes

| CT | preco | cliente_vip | Fluxo | Saída esperada |
|---|---|---|---|---|
| CT1 | 100 | False | total=preco → return | 100 |
| CT2 | 100 | True | desconto aplicado | 80 |
| CT3 | 40 | False | total redefine para 50 | 50 |
| CT4 | 40 | True | desconto + limite mínimo | 50 |

Esses testes exercitam:

- caminho com desconto
- caminho sem desconto
- caminho com limite mínimo
- caminho com desconto e limite mínimo

---

# 5. Pares Def-Use não cobertos por Cobertura de Ramos (C1)

Cobertura de **ramos (C1)** garante apenas que cada decisão seja executada como **true** e **false**.

Decisões existentes:

```
if cliente_vip
if total < 50
```

Mesmo cobrindo ambos os ramos, **alguns fluxos Def-Use podem não ser garantidos**.

### Exemplo

O fluxo:

```
total = preco - desconto → return total
```

pode não ocorrer se:

```
preco grande o suficiente para evitar total < 50
```

Assim, **C1 não garante cobertura completa de fluxo de dados**.

Isso ocorre porque:

- cobertura de ramos analisa **controle**
- análise def-use analisa **fluxo de dados**

Logo, **critérios de fluxo de dados são mais rigorosos que cobertura de ramos**.
