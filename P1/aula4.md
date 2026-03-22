# 🧠 Resumo – Simulação e Teste de Software (Aula 04)

## 🎯 Objetivo da Aula

Aprender **técnicas de teste caixa-branca**, focando em:

* Cobertura estrutural
* Caminhos independentes
* Complexidade ciclomática
* Critérios de cobertura (C0, C1, CC, etc.)
* Fluxo de dados
* Testes de laço (ciclos)

👉 Insight:
Aqui você sai do “o sistema funciona?” e vai para **“o código foi totalmente exercitado?”**

---

## 🧪 Teste de Caixa-Branca

### Definição:

* Baseado na **estrutura interna do código**
* O testador conhece a implementação

### O que verifica:

* Caminhos do código
* Decisões (if/else)
* Laços
* Estruturas internas

👉 Quando combinado com caixa-preta → aumenta muito a qualidade

---

## 🔗 Grafo de Fluxo de Controle (GFC)

* **Nós** → blocos de código
* **Arestas** → fluxo de execução

👉 Base para análise estrutural

---

## 🎯 Objetivo dos Testes

* Executar todos os caminhos independentes
* Testar decisões como verdadeiro e falso
* Validar laços (0, 1, n iterações)
* Verificar dados internos

---

## 📊 Critérios de Cobertura

### Principais:

| Critério       | O que cobre        |
| -------------- | ------------------ |
| C0             | Comandos           |
| C1             | Ramos              |
| CC             | Condições          |
| D/C            | Decisão + condição |
| CMC            | Todas combinações  |
| Fluxo de dados | Def-uso            |

---

## 🧠 Hierarquia (importante)

Mais forte → mais completo:

* CMC
* D/C
* CC
* C1
* C0

👉 Importante:

* C1 cobre C0
* CC NÃO garante C1

---

## 🧩 Caminhos Independentes

### Definição:

Caminho que introduz uma nova parte do código

👉 Nem todo caminho possível é necessário

---

## 🔢 Complexidade Ciclomática

### Fórmula:

```
V(G) = E - N + 2
```

Ou:

```
V(G) = número de decisões + 1
```

👉 Resultado:

* Número de **caminhos independentes**
* Número mínimo de testes

---

## 📌 Exemplo:

2 decisões →
V(G) = 3 → precisa de 3 testes

👉 Insight:
Mais if → mais complexidade → mais testes

---

## 🧪 Cobertura de Comandos (C0)

### O que faz:

* Executa todos os comandos pelo menos 1 vez

### Problema:

* Pode ignorar caminhos importantes

👉 Exemplo:
if nunca testado como falso

---

## 🌿 Cobertura de Ramos (C1)

### O que faz:

* Testa cada decisão como:

  * verdadeiro
  * falso

👉 Garante:

* Todas as arestas do grafo

👉 Importante:

* Subsume C0
* Mínimo de testes = V(G)

---

## ⚠️ Cobertura de Condição (CC)

### O que faz:

* Testa cada condição individualmente

Exemplo:

```python id="3vwspl"
if (a > 0 and b < 10):
```

👉 Testa:

* a > 0 → V/F
* b < 10 → V/F

---

### ⚠️ Pegadinha:

CC NÃO garante C1

👉 Por isso existe:

---

## 🔗 Decisão/Condição (D/C)

* Combina:

  * C1 (ramos)
  * CC (condições)

👉 Mais confiável

---

## 🔥 Condição Múltipla (CMC)

* Testa TODAS combinações possíveis

Exemplo:

* 2 condições → 4 casos

👉 Muito caro → pouco usado em sistemas grandes

---

## 🔄 Fluxo de Dados

### Ideia:

Testar como valores percorrem o código

---

### Conceitos:

* **Definição (def)** → variável recebe valor
* **Uso (use)** → variável é usada

Tipos:

* c-use → cálculo
* p-use → condição

---

### Par Def-Uso:

* Ligação entre definição e uso sem redefinição

---

## 📊 Critérios de Fluxo

* **All-Defs** → cada definição usada
* **All-Uses** → todos pares cobertos
* **All-DU-Paths** → todos caminhos entre def-uso

👉 Hierarquia:
All-DU > All-Uses > All-Defs > C1

---

## ⚠️ Por que fluxo de dados é importante?

Detecta erros que C1 não pega:

* Variável não usada
* Valor errado propagado
* Bug em cálculo

👉 Exemplo clássico:
cálculo errado mas fluxo executado corretamente

---

## 🔁 Teste de Ciclo (Loops)

### Objetivo:

Validar comportamento de laços

---

### Casos importantes:

* 0 iterações
* 1 iteração
* 2 iterações
* n-1, n, n+1

👉 Detecta erros de limite

---

## 🔗 Tipos de ciclos

### 1. Simples

* Um loop

### 2. Aninhado

* Loop dentro de loop
  👉 Testar de dentro pra fora

### 3. Concatenado

* Loops separados
  👉 Testar individualmente

---

## 📊 Resumo dos Critérios

| Critério       | Garante           | Custo |
| -------------- | ----------------- | ----- |
| C0             | Comandos          | Baixo |
| C1             | Ramos             | Médio |
| CC             | Condições         | Médio |
| D/C            | Ramos + condições | Médio |
| CMC            | Todas combinações | Alto  |
| Fluxo de dados | Def-uso           | Alto  |

---

# 🔥 O que você PRECISA decorar

1. Diferença caixa-preta vs caixa-branca
2. O que é GFC
3. Fórmula da complexidade ciclomática
4. Diferença entre C0, C1, CC
5. Por que CC ≠ C1
6. O que é D/C
7. Conceito de fluxo de dados (def/use)
8. Casos de teste de loops (0,1,n…)
9. Hierarquia de cobertura

---

# ⚠️ Visão estratégica

* C0 sozinho é fraco → não confie
* C1 já é padrão mínimo aceitável
* CC pode enganar → cuidado em prova
* Complexidade ciclomática indica risco do código
* Fluxo de dados encontra bugs mais “profundos”
* Teste de loop evita erros clássicos de borda

👉 Mentalidade correta:
Testar bem não é só validar saída — é garantir que **toda lógica interna foi exercitada**
