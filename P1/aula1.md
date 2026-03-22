# 🧠 Resumo – Simulação e Teste de Software (Aula 01)

## 🎯 Por que testar software
- Bugs geram prejuízo financeiro, perda de dados e até risco de vida
- Corrigir erro em produção pode custar até 100x mais
- Teste é a principal forma de garantir qualidade

👉 Insight importante  
Se você só testa no final, já está fazendo errado (isso conecta com “shift-left”).

---

## 🧩 Conceito-chave (cai MUITO em prova)

### 🔁 Cadeia do problema
Erro → Defeito → Falha

- Erro (humano) alguém escreveu errado  
- Defeito (bug) erro virou código errado  
- Falha usuário percebe o problema  

👉 Pegadinha clássica  
Nem todo defeito vira falha (às vezes nunca é executado).

---

## ✅ Qualidade de Software (ISOIEC 25010)

### Externas (visíveis ao usuário)
- Funcionalidade
- Confiabilidade
- Usabilidade

### Internas (engenharia)
- Eficiência
- Manutenibilidade
- Portabilidade

👉 Tradução prática  
Não adianta “funcionar” se for lento, difícil de manter ou impossível de escalar.

---

## ⚖️ Verificação vs Validação (clássico de prova)

- Verificação  
  → “Estou construindo certo”  
  → Foco requisitos, design  

- Validação  
  → “Estou construindo a coisa certa”  
  → Foco necessidade do usuário  

👉 Diferença estratégica  
Você pode passar na verificação e falhar na validação (software correto… mas inútil).

---

## 🧪 Classificação de Testes

### 1. Funcionais vs Não-Funcionais
- Funcional → o sistema faz o que deve  
- Não-funcional → como ele se comporta (performance, segurança)

---

### 2. Níveis de Teste
- Unidade → funçãoclasse isolada  
- Integração → comunicação entre módulos  
- Sistema → sistema completo  
- Aceitação → valida com o cliente  

👉 Insight
Quanto mais alto o nível, mais caro e lento o teste.

---

### 3. Técnicas de Teste
- Caixa-preta → não olha código  
- Caixa-branca → olha lógica interna  
- Caixa-cinza → mistura os dois  

👉 Prova gosta de
- Caixa-preta = foco em entradasaída  
- Caixa-branca = cobertura de código

---

### 4. Tipos de Teste
- Regressão → garantir que nada quebrou  
- Fumaça → teste básico (“liga”)  
- Sanidade → valida correção específica  
- Exploratório → sem roteiro  

---

## ⚠️ Testes Positivos vs Negativos

- Positivo entrada válida → funciona  
- Negativo entrada inválida → sistema reage corretamente  

👉 Muito importante
Testes negativos são essenciais pra segurança e robustez.

---

## 🔄 STLC (Ciclo de Teste)

1. Planejamento  
2. Design dos testes  
3. Execução  
4. Análise  

👉 Conexão importante
Acontece em paralelo com o desenvolvimento (não é etapa final).

---

## 🚀 Conceitos modernos (alto valor)

### Shift-Left
- Testar o mais cedo possível
- Reduz custo de bugs

### Continuous Testing
- Testes automáticos em CICD
- Feedback rápido

👉 Isso aqui é MUITO cobrado em entrevista também.

---

## 📊 Métricas de Teste

- Cobertura de código  
- Bugs encontrados  
- Bugs em produção  
- Tempo de execução  

### Regra SMART
- Específica
- Mensurável
- Alcançável
- Relevante
- Temporal

👉 Pegadinha
100% cobertura ≠ qualidade garantida.

---

## 🐍 pytest (parte prática)

### Estrutura
