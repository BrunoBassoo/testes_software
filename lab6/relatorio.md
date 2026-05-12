# Relatório — Laboratório 6 (Atividade 06)

## 1. Execução dos testes

Comando:

```text
python -m unittest discover -s tests -p "test*.py" -v
```

**Resultado:** todos os testes passaram (57 testes na última execução local).

Arquivos:

- `tests/test_unidade.py` — Parte 1 (unidade com stub / `MagicMock`).
- `tests/test_integracao.py` — Parte 2 (integração com repositório real).
- `tests/test_doubles.py` — Parte 3 (stub e mock explícitos).

---

## 2. Cobertura (`coverage.py`)

Comandos:

```text
python -m coverage run -m unittest discover -s tests -p "test*.py"
python -m coverage report -m --include="*/src/calculadora.py"
```

**Resultado:** `src/calculadora.py` com **100%** das linhas cobertas (0 linhas em falta).

**Linhas não cobertas:** nenhuma, para o escopo de `calculadora.py`.

**Justificativa:** a suíte exercita todos os métodos públicos, os ramos de validação de tipo, o ramo de divisão por zero e os fluxos em que `salvar` é ou não chamado (via testes com mock e exceções).

---

## 3. Bug intencional — descoberta e correção

### Sintoma

No histórico persistido por `salvar()`, a operação de **potência** era registrada com o operador de **multiplicação** (`*`) em vez do operador de **potência** (`**`), gerando mensagens semanticamente incorretas (por exemplo, sugerindo `2 * 3` quando o cálculo foi `2 ** 3`).

### Como os testes revelaram

Os testes de **mock** em `test_doubles.py` fixam o contrato da string passada a `repositorio.salvar()`. Ao exigir `"2 ** 3 = 8"` (e ao rejeitar o padrão antigo `5 * 2 = 25` como representação de potência), a falha aparece de forma objetiva.

### Correção aplicada

Em `potencia`, a chamada foi ajustada para registrar o operador correto no *f-string* de histórico, alinhando **interface textual** entre módulos com a **semântica** da operação.

---

## 4. Stub vs mock na prática (reflexão)

- **Stub (como usamos na Parte 1):** o `MagicMock` substitui o repositório para a calculadora **não depender** de I/O real. O que importa é o **resultado** da operação e o estado `resultado` — não validamos *como* o stub foi tocado, apenas que a unidade se comportou bem em isolamento.

- **Mock (Parte 3):** usamos as mesmas APIs (`assert_called_once_with`, `assert_not_called`) para garantir **comportamento**: após `somar(4, 6)`, `salvar` deve ter sido chamado **uma vez** com a string exata; em erro de tipagem ou divisão por zero, `salvar` **não** deve ser chamado.

Na integração (Parte 2), não usamos essas asserções de chamada: testamos o **efeito conjunto** no repositório real (lista e contagem), típico de teste de integração focado em **contrato e estado compartilhado**.

---

## 5. Observação sobre `bool` em Python

O enunciado pede ao menos um caso com `bool`. Em Python, `bool` é subclasse de `int`, portanto passa em `isinstance(x, (int, float))`. O teste `test_bool_e_aceito_por_ser_subclasse_de_int` documenta que esse comportamento **é esperado** dado o contrato atual da calculadora; rejeitar `bool` exigiria validação explícita adicional (não exigida pelo enunciado).
