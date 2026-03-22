# 🧠 Resumo – Simulação e Teste de Software (Aula 05)

## 🎯 Objetivo da Aula

Aprender como **avaliar a qualidade dos testes**, usando:

* Teste de mutação (mutation testing)
* Métricas de eficácia
* Teste baseado em defeitos
* Ferramentas práticas

👉 Insight:
Aqui você deixa de focar só no código e passa a avaliar:
**“meus testes são realmente bons?”**

---

## 🧪 Teste de Mutação

### O que é:

* Técnica de **caixa-branca**
* Avalia a qualidade da suíte de testes

👉 Ideia central:
Se o teste não detecta erros simples, não detecta erros reais.

---

## ⚙️ Como funciona

### 1. Criar mutantes

* Pequenas mudanças no código

Exemplos:

* `a + b → a - b`
* `x == y → x != y`
* `true → false`
* `i < n → i <= n`

---

### 2. Executar testes

* Rodar os testes em cada mutante

---

### 3. Classificar resultados

* **Mutante morto (killed)**
  → teste detectou erro (bom)

* **Mutante sobrevivente (survived)**
  → teste não detectou erro (problema)

---

👉 Insight:
Mutante sobrevivente = falha na sua suíte de testes

---

## 🧩 Tipos de Mutantes

### 1. Mutantes válidos

* Alteram comportamento
* Devem ser detectados

---

### 2. Mutantes equivalentes

* Não alteram comportamento
* Não podem ser detectados

👉 Problema:
Atrapalham a análise

---

## ⚠️ Mutantes Equivalentes

### Desafio:

* Testes não conseguem identificar

### Soluções:

* Análise manual
* Heurísticas automáticas
* Abordagem híbrida

👉 Insight:
Isso é uma limitação real da técnica

---

## 🔧 Operadores de Mutação

Simulam erros comuns:

* Aritméticos (`+ → -`)
* Relacionais (`> → >=`)
* Lógicos (`&& → ||`)
* Outros (valores, chamadas, etc.)

---

## 🔥 Mutação de Ordem Superior

### O que é:

* Aplicar múltiplas mutações ao mesmo tempo

👉 Vantagem:

* Simula erros mais complexos

👉 Problema:

* Difícil de analisar

---

## 📊 Taxa de Mutação

### Fórmula:

```id="dxr5ue"
Taxa = (mutantes mortos / mutantes totais) * 100
```

👉 Observação:

* Exclui mutantes equivalentes

---

### Interpretação:

* Alta taxa → testes bons
* Baixa taxa → testes fracos

---

## 📈 Mutation Score (formal)

```id="5w3nsr"
MS(P, T) = |mutantes mortos| / (total - equivalentes) * 100
```

👉 Mede efetividade da suíte de testes

---

## 📊 Classificação dos Resultados

| Resultado   | Significado   | Ação         |
| ----------- | ------------- | ------------ |
| killed      | Detectado     | OK           |
| survived    | Não detectado | Criar testes |
| equivalent  | Igual         | Ignorar      |
| timeout     | Loop infinito | Investigar   |
| incompetent | Não compila   | Descartar    |

---

## ⚖️ Vantagens vs Desvantagens

### ✅ Vantagens:

* Mede qualidade real dos testes
* Identifica pontos fracos
* Melhora cobertura prática

---

### ❌ Desvantagens:

* Alto custo computacional
* Mutantes equivalentes
* Complexidade em sistemas grandes

---

## 🧠 Teste Baseado em Defeitos

### Ideia:

* Criar testes focados em erros comuns

👉 Baseado em:

* Modelos de falha (fault models)

---

### Relação com mutação:

* Cada mutação = um tipo de erro

---

## 🔬 Hipóteses Fundamentais

### 1. Programador Competente

* Código é quase correto
* Erros são pequenos

👉 Justifica mutações simples

---

### 2. Efeito de Acoplamento

* Testes que pegam erros simples → pegam erros complexos

👉 Muito cobrado em prova

---

## 🔍 Visão Formal

* P = programa
* M = mutantes
* T = testes

👉 Mutante morto se:

* Resultado diferente do original

---

## 📊 Comparação com Outros Testes

| Critério            | Foco            | Limitação                |
| ------------------- | --------------- | ------------------------ |
| Cobertura de linhas | Executar código | Não garante qualidade    |
| Cobertura de ramos  | Decisões        | Pode ignorar valores     |
| Caixa-preta         | Entrada/saída   | Depende da especificação |
| Mutação             | Detectar erros  | Alto custo               |

---

👉 Insight forte:
Cobertura alta ≠ testes bons
Mutação mede qualidade real

---

## 🧪 Ferramenta: mutmut

### O que faz:

* Gera mutantes automaticamente
* Executa testes
* Mostra relatório

---

### Saída:

* Quantos mutantes criados
* Quantos mortos
* Quais sobreviveram

👉 Uso:
Pode integrar com CI/CD

---

## 🔗 Aplicações Avançadas

* Mutação de interface
* Defeitos históricos
* Mutação de protocolo
* Injeção de falhas

👉 Muito usado em sistemas complexos

---

# 🔥 O que você PRECISA decorar

1. O que é teste de mutação
2. Conceito de mutante morto vs sobrevivente
3. Mutante equivalente
4. Fórmula da taxa de mutação
5. O que é mutation score
6. Operadores de mutação
7. Hipótese do programador competente
8. Efeito de acoplamento
9. Diferença entre cobertura e mutação
10. Ferramenta mutmut

---

# ⚠️ Visão estratégica

* Cobertura de código pode enganar → mutação não
* Teste bom é o que detecta erro, não o que roda
* Mutação expõe falhas reais na suíte
* Alto custo → usar com estratégia (não em tudo)
* Ideal: combinar com outros testes

👉 Mentalidade correta:
Não basta testar — você precisa garantir que seus testes **realmente pegam erros**
