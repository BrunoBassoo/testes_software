# Laboratório 7 — Test-Driven Development (TDD)

Implementação da **atividade prática da Aula 07** (CC8550): classe `Estoque` desenvolvida **estritamente no espírito do TDD** — teste como especificação executável, ciclos **RED → GREEN → REFACTOR** comentados em `tests/test_estoque.py` e referências em `src/estoque.py`.

## Estrutura

```text
lab7/
├── src/
│   └── estoque.py          # Classe Estoque (produção)
├── tests/
│   └── test_estoque.py     # Suíte (≥ 10 testes; comentários TDD)
├── requirements.txt
├── README.md
└── relatorio.md
```

## Execução

Na pasta `lab7`:

```powershell
python -m unittest discover -s tests -p "test*.py" -v
```

(Não há dependências externas obrigatórias; `requirements.txt` está reservado para extensões opcionais, por exemplo `coverage`.)

---

## Como a Aula 07 orienta esta resolução

### Motivação e custo de defeito

Os slides mostram que defeitos encontrados tarde custam muito mais; o TDD antecipa a detecção **no momento da codificação**. A suíte `test_estoque.py` funciona como rede de segurança para refatorar (`_validar_quantidade_positiva`, remoção de chave ao zerar, ordenação em `listar_produtos`).

### Ciclo RED — GREEN — REFACTOR

1. **RED:** um teste novo que falha até a funcionalidade existir (falha “pela razão certa”).
2. **GREEN:** código **mínimo** em `Estoque` para passar (YAGNI).
3. **REFACTOR:** melhorar design (DRY, nomes, estrutura) **sem** quebrar testes — como no exemplo do IMC (validações consolidadas) e da `ContaBancaria` (`_validar_valor_positivo` nos slides).

Cada bloco em `test_estoque.py` descreve qual requisito do enunciado aquele ciclo cobre.

### Regras de negócio implementadas (enunciado)

| Regra | Onde aparece nos testes |
|--------|-------------------------|
| Não remover mais do que o disponível | `test_remover_mais_que_disponivel_*`, `test_remover_produto_inexistente_*` |
| Adicionar produto existente **incrementa** | `test_adicionar_produto_existente_incrementa_quantidade` |
| Adicionar/remover com quantidade ≤ 0 inválido | `test_adicionar_quantidade_*`, `test_remover_quantidade_zero_*` |
| `produto_mais_estocado()` → `None` se vazio | `test_produto_mais_estocado_estoque_vazio_retorna_none` |
| Consulta a inexistente → `0` | `test_consultar_produto_inexistente_retorna_zero` |

### Conexão com o restante da aula

- **TDD e design:** dificuldade de testar → sinal de acoplamento/coesão ruim; aqui a API é simples e determinística.
- **Dependências externas (slide):** não há SMTP/DB; se evoluíssemos para persistência, o caminho seria **injeção de dependência + mock**, como `ServicoNotificacao` na aula.
- **Pirâmide de testes:** esta atividade reforça a **base** (muitos testes unitários rápidos).

### Observação: desempate em `produto_mais_estocado`

O PDF não define desempate quando duas quantidades são máximas e iguais. Na implementação final usamos **`min(candidatos)`** (ordem lexicográfica) para manter o comportamento **reprodutível** nos testes — documentado no código e no `relatorio.md`.
