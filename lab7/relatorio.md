# Relatório — Laboratório 7 (Aula 07 / Atividade Estoque)

## Entregáveis do enunciado

| Item | Status |
|------|--------|
| `estoque.py` com classe `Estoque` | `src/estoque.py` |
| `test_estoque.py` com suíte de testes | `tests/test_estoque.py` |
| Ao menos **10** testes (normais e erro) | **15** testes |
| Todos os testes passando | Sim (`python -m unittest discover -s tests -p "test*.py" -v`) |
| Critério TDD: teste antes do código, fases comentadas | Comentários **RED / GREEN / REFACTOR** nos blocos da suíte e notas em `estoque.py` |

## Resumo da API

- `adicionar_produto(nome, quantidade)` — quantidade obrigatoriamente **> 0**; produto existente **soma** à quantidade.
- `remover_produto(nome, quantidade)` — quantidade **> 0**; não permite remover acima do disponível (inexistente = 0 disponível); ao chegar a zero, o item deixa de ocupar o dicionário interno.
- `consultar_quantidade(nome)` — **0** se o produto não existir.
- `listar_produtos()` — nomes com quantidade **> 0**, em ordem **alfabética** (refino de REFACTOR para estabilidade).
- `produto_mais_estocado()` — **`None`** se não houver itens; caso contrário, nome entre os de **maior** quantidade; em empate, escolha **lexicográfica** (`min`).

## Evidência do TDD

A ordem dos métodos na suíte segue uma narrativa de construção: primeiro inclusão e consulta, depois regras de acumulação e validação de quantidade, remoções e erros, listagem e, por fim, produto mais estocado — cada bloco comentado com **RED → GREEN → REFACTOR**, alinhado aos exemplos da aula (IMC e conta bancária).

## Desempate em `produto_mais_estocado`

Não especificado no slide da atividade. Foi adotada regra **determinística** (`min` dos nomes empatados em quantidade máxima) para evitar testes instáveis e documentar decisão de projeto no `README.md`.
