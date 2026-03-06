# Exercício Aula 05 – Testes de Mutação (tema: Fórmula 1)

## Objetivo

Avaliar a **efetividade da suíte de testes** do módulo `formula1.py` usando **testes de mutação**: primeiro **manualmente** (mutantes criados à mão) e depois com a ferramenta **mutmut**, para comparar a **taxa de acerto** (mutation score) nos dois casos.

---

## Métrica: Taxa de Mutação (Mutation Score)

\[
\text{Taxa de Mutação} = \frac{\text{mutantes mortos}}{\text{mutantes totais}} \times 100\%
\]

- **Mutante morto** = pelo menos um teste falhou (a suíte detectou o defeito).
- **Mutante sobrevivente** = todos os testes passaram (a suíte não detectou).

Quanto **maior** a taxa, mais eficaz é a suíte. Mutantes equivalentes podem ser excluídos do total na fórmula.

---

# Parte 1 – Mutação MANUAL

Criamos **5 mutantes** à mão (um defeito por vez) na pasta `mutantes_manuais/`. Cada arquivo é uma cópia do `formula1.py` com **uma única alteração**.

## Tabela dos mutantes manuais

| # | Arquivo        | Função               | Alteração (mutação)              | Resultado esperado | Morto? (preencher) |
|---|----------------|----------------------|----------------------------------|--------------------|--------------------|
| 1 | formula1_m1.py | pontos_por_posicao   | `posicao <= 10` → `posicao < 10` | posição 10 retorna 0 | Sim (test_pontos_decimo_lugar) | 
| 2 | formula1_m2.py | tempo_total_pit_stop | `+ 4` → `- 4`                    | pit com troca retorna valor errado | Sim (test_pit_stop_com_troca) |
| 3 | formula1_m3.py | velocidade_media_kmh | `tempo_horas <= 0` → `tempo_horas < 0` | tempo=0 não retorna 0.0, dá erro | Sim (test_velocidade_media_tempo_zero) |
| 4 | formula1_m4.py | volta_valida         | `<=` → `<`                       | volta no limite retorna False | Sim (test_volta_valida_no_limite) |
| 5 | formula1_m5.py | diferenca_tempo      | `-` → `+`                        | diferença errada | Sim (test_diferenca_*) |

## Como fazer a mutação manual

### Opção A – Usando o script (recomendado)

Na pasta `lab5`:

```bash
python rodar_mutantes_manuais.py
```

O script substitui temporariamente o `formula1.py` por cada mutante, roda os testes e restaura o original. No final ele mostra quantos mutantes foram **mortos** e a **taxa de mutação manual**.

### Opção B – À mão

1. Faça backup do `formula1.py`.
2. Para cada mutante (M1 a M5):
   - Copie o conteúdo de `mutantes_manuais/formula1_mN.py` para `formula1.py`.
   - Rode: `python -m pytest test_formula1.py -v`
   - Se **algum teste falhou** → mutante **MORTO**. Se **todos passaram** → mutante **SOBREVIVEU**.
3. Restaure o `formula1.py` original.

## Resultado – Parte 1 (manual)

Preencha após rodar:

- **Mutantes mortos (manual):** _____ / 5  
- **Taxa de mutação (manual):** _____ %

---

# Parte 2 – Mutação com MUTMUT

A ferramenta **mutmut** gera **muitos** mutantes automaticamente (troca de operadores, constantes, etc.) e roda a suíte para cada um.

## Instalação e execução

Na pasta `lab5`:

```bash
pip install mutmut pytest
python -m mutmut run
```

Para ver o resumo (quantos mortos, sobreviventes, equivalentes):

```bash
python -m mutmut results
```

Para ver o código de um mutante (ex.: o de número 5):

```bash
python -m mutmut show 5
```

## Resultado – Parte 2 (mutmut)

Preencha após rodar `mutmut run` e `mutmut results`:

- **Total de mutantes (mutmut):** _____  
- **Mortos:** _____  
- **Sobreviventes:** _____  
- **Equivalentes (se houver):** _____  
- **Taxa de mutação (mutmut):** _____ %  
  (use: mortos / (total - equivalentes) × 100)

---

# Comparação e conclusão

| Métrica              | Mutação manual | Mutação mutmut |
|----------------------|----------------|----------------|
| Nº de mutantes       | 5              | _____          |
| Mutantes mortos      | _____          | _____          |
| Taxa de mutação      | _____ %        | _____ %        |

**Conclusão (preencher):**

- Na **mutação manual** só avaliamos 5 mutantes escolhidos; a taxa tende a ser _____ porque _____.
- O **mutmut** gera dezenas/centenas de mutantes; a taxa reflete _____.
- A diferença entre as duas taxas mostra que _____.

(Exemplo de conclusão: a mutação manual dá uma amostra pequena e controlada; o mutmut explora muitas mais variações e pode revelar pontos fracos da suíte onde mutantes sobrevivem.)

---

## Referência rápida – Interpretação mutmut

- **Killed** = mutante detectado (bom).
- **Survived** = nenhum teste detectou (candidato a criar novo teste).
- **Equivalent** = mutante igual em comportamento ao original (excluir do cálculo).
- **Suspicious** = timeout ou indeterminado.

Com isso você faz a **mutação manual**, depois a **mutação com mutmut**, e compara as **taxas de acerto** entre as duas abordagens.
