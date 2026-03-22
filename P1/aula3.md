# 🧠 Resumo – Simulação e Teste de Software (Aula 03)

## 🎯 Objetivo da Aula

Aprender **técnicas de teste caixa-preta** para selecionar casos de teste de forma eficiente:

* Particionamento em classes de equivalência
* Análise de valor limite
* Tabelas de decisão
* Pairwise testing
* Property-based testing (Hypothesis)

👉 Insight:
Aqui você aprende a **testar melhor com menos testes**.

---

## ⚠️ Problema da Exaustividade

* Testar todas as combinações é impossível
* Exemplo: 3 parâmetros de 32 bits → ~10²⁸ combinações

👉 Conclusão:
Precisamos de técnicas para **reduzir casos mantendo cobertura**

---

## 🧪 Teste Caixa-Preta

### Características:

* Baseado na **especificação**
* Não olha o código
* Foco no comportamento externo

### Quando usar:

* Requisitos funcionais
* APIs
* Teste de aceitação

👉 Analogia:
Testar um carro sem abrir o motor

---

## 🧩 Classes de Equivalência

### Conceito:

Dividir entradas em grupos onde o comportamento é igual

* Testa **1 valor por classe**
* Reduz drasticamente o número de testes

### Tipos:

* **Válidas** → comportamento esperado
* **Inválidas** → erro esperado

---

### 📌 Exemplo (idade):

* < 0 → inválida
* 0–17 → 0%
* 18–64 → 10%
* 65+ → 20%

👉 Estratégia:
Testar um valor de cada classe (ex: -5, 10, 30, 70)

---

## 🧠 Como identificar classes

### Regras práticas:

* Intervalos → dividir por faixa
* Enum → um por valor
* Boolean → verdadeiro/falso
* Strings:

  * vazia
  * tamanho normal
  * muito longa
  * inválida

---

## ⚠️ Análise de Valor Limite

### Ideia:

Erros acontecem nas bordas

### Regra:

Para intervalo [A, B], testar:

* A-1
* A
* A+1
* B-1
* B
* B+1

👉 Isso pega erros tipo:

* `<` vs `<=`
* off-by-one

---

### 📌 Exemplo (nota 0–10):

* -0.1 → inválido
* 0.0 → mínimo
* 0.1 → válido
* 9.9 → válido
* 10.0 → máximo
* 10.1 → inválido

---

## 🔄 Estratégia Completa

1. Identificar classes
2. Testar:

   * 1 valor representativo
   * valores limite
3. Testar inválidos

👉 Resultado:
Alta cobertura com poucos testes

---

## 📊 Tabela de Decisão

### Quando usar:

* Muitas condições
* Regras combinadas

### Estrutura:

* Condições (entrada)
* Ações (resultado)
* Regras (combinações)

---

### 📌 Exemplo (empréstimo):

Aprova se:

* idade ≥ 18
* renda ≥ 3000
* score ≥ 600

👉 Combinações → várias regras

---

### 💡 Don’t Care (X)

* Algumas condições não importam
* Reduz número de casos

👉 Exemplo:
Se idade < 18 → resto não importa

---

## 🔗 Pairwise Testing

### Problema:

Muitas combinações

### Solução:

Testar todas combinações **2 a 2**

👉 Observação:

* Maioria dos bugs → interação de 2 variáveis

---

### 📌 Exemplo:

* SO: Windows, Linux, Mac
* Browser: Chrome, Firefox
* Idioma: PT, EN

Total: 12
Pairwise: 6

👉 Redução de 50%

---

## 🤖 Property-Based Testing

### Diferença:

**Tradicional:**

* Testa casos específicos

**Property-based:**

* Testa propriedades gerais

---

### 📌 Exemplo:

Tradicional:

```python id="l0a3pp"
assert somar(2, 3) == 5
```

Property:

```python id="0xpnzz"
assert somar(a, b) == somar(b, a)
```

👉 Insight:
Você testa **regras universais**, não casos isolados

---

## 🧪 Hypothesis

### O que faz:

* Gera dados automaticamente
* Testa centenas de cenários

### Exemplo:

```python id="n7t3pi"
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers())
def test_exemplo(x):
    assert x == x
```

---

## 🔢 Strategies (geração de dados)

* integers()
* floats()
* text()
* lists()
* booleans()

Com restrições:

```python id="ndh5q4"
st.integers(min_value=0, max_value=100)
```

---

## 📌 Exemplo Real (ordenação)

```python id="j7bqzz"
@given(st.lists(st.integers()))
def test_ordenar(lista):
    ordenada = sorted(lista)

    assert len(ordenada) == len(lista)
    assert set(ordenada) == set(lista)

    for i in range(len(ordenada)-1):
        assert ordenada[i] <= ordenada[i+1]
```

👉 Testa automaticamente vários cenários

---

## 🐛 Descobrindo Bugs

Exemplo:

```python id="kklq3y"
def calcular_media(numeros):
    return sum(numeros) / len(numeros)
```

👉 Problema:
Lista vazia → erro

Property-based encontra isso sozinho

---

# 🔥 O que você PRECISA decorar

1. O que é **caixa-preta**
2. **Classes de equivalência**
3. **Valores limite (A-1, A, A+1…)**
4. Diferença entre válido e inválido
5. **Tabela de decisão**
6. Conceito de **don’t care**
7. **Pairwise testing**
8. Diferença:

   * exemplo vs propriedade
9. O que é **Hypothesis**

---

# ⚠️ Visão estratégica

* Teste exaustivo é impossível → escolha inteligente é tudo
* Classes de equivalência economizam MUITO esforço
* Bugs vivem nas bordas → valor limite é obrigatório
* Pairwise resolve explosão combinatória
* Property-based encontra bugs que você nem imaginou

👉 Mentalidade correta:
Testar bem não é testar tudo — é testar **o que mais importa**
