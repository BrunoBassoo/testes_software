# Laboratório 6 — Testes de unidade, integração e test doubles

## Contexto, objetivo e tecnologias (guia para apresentação oral)

**Contexto:** o sistema é uma **calculadora** que, além de calcular, **registra o histórico** das operações em um **repositório em memória**. O laboratório simula um cenário real em que dois módulos precisam “conversar” com um **contrato** (formato da string salva, ordem das chamadas).

**Para que serve:** exercitar **níveis de teste** da pirâmide — **unidade** (calculadora isolada), **integração** (calculadora + repositório reais) e **test doubles** (stub vs mock com `MagicMock`), além de **cobertura** em `calculadora.py`. A ideia da Aula 06 é mostrar que erros aparecem também na **interface entre módulos**, não só na lógica interna.

**Tecnologias:** **Python 3**, **`unittest`** (descoberta de testes, `TestCase`, `setUp`), **`unittest.mock.MagicMock`** (substituir o repositório), **`coverage.py`** (medir linhas cobertas). Não há framework web: é lógica pura + testes.

**Se o professor perguntar:** “*Stub* fornece resposta controlada sem exigir I/O real; *mock* verifica **se** e **como** `salvar` foi chamado. Integração usa o repositório **de verdade** para pegar erros de contrato entre classes.”

---

Este laboratório implementa a **Atividade 06** (calculadora com repositório de histórico) em alinhamento com a **Aula 06** — *Teste de integração (e outros) e test doubles* (CC8550).

## Estrutura do projeto

```text
lab6/
├── src/
│   ├── calculadora.py    # Lógica da calculadora (usa o repositório)
│   └── repositorio.py    # Persistência em memória do histórico
├── tests/
│   ├── test_unidade.py   # Parte 1: isolamento com MagicMock como stub
│   ├── test_integracao.py# Parte 2: módulos reais integrados
│   └── test_doubles.py   # Parte 3: stub vs mock (comportamento)
├── requirements.txt
├── README.md             # Este guia
└── relatorio.md          # Resultados, cobertura e reflexão
```

## Como executar

## Resultado dos testes (local)

- Execução local: 57 testes passaram (57 passed).
- Para rodar os testes rapidamente:

```bash
cd lab6
pytest -q
```

Para gerar relatório de cobertura (opcional):

```bash
python -m coverage run -m pytest
python -m coverage report -m --include="*/src/calculadora.py"
python -m coverage html
```

## Como executar

Na pasta `lab6`:

```bash
pip install -r requirements.txt
pytest -q
```

Cobertura em `calculadora.py`:

```powershell
python -m coverage run -m unittest discover -s tests -p "test*.py"
python -m coverage report -m --include="*/src/calculadora.py"
python -m coverage html
```

(O relatório HTML fica em `htmlcov/index.html`.)

---

## Relação com a Aula 06 (slides)

### Níveis de teste (modelo em V e visão geral)

A aula posiciona o **teste de unidade** como verificação de cada unidade (função, classe, módulo) com base no projeto, e o **teste de integração** como busca de falhas ao **juntar módulos** — em especial **erros de interface** (contratos incompatíveis entre componentes).

Nesta atividade:

- **Unidade (`test_unidade.py`)**: testamos só a `Calculadora`, **sem** depender do `HistoricoRepositorio` real. O PDF sugere `MagicMock()` como **stub**: o foco é *o que a calculadora faz com as respostas/comportamento simulado do repositório* (retorno numérico, `resultado`, exceções).
- **Integração (`test_integracao.py`)**: usamos **repositório real + calculadora real** e verificamos **comunicação** — ordem das operações, formato das strings no histórico, `total()` após sequências e `limpar()`.

O exemplo da aula (autenticação retornando `bool` vs `"Aprovado"`) ilustra **erro de integração por contrato**. Aqui, o defeito intencional era outro: **string de histórico inconsistente com a operação** em `potencia` (ver `relatorio.md`).

### Test doubles (taxonomia de Meszaros)

Os slides apresentam *dummy, stub, spy, mock, fake* e enfatizam:

| | **Stub** | **Mock** |
|---|-----------|----------|
| Pergunta principal | “O que o módulo faz **com** esta resposta / sem esta dependência?” | “O módulo **chamou** a dependência **como** esperado?” |
| Verificação típica | Estado / resultado da unidade sob teste | Chamadas, argumentos, quantidade |

- Em **`TestComStub`** (`test_doubles.py`), o `MagicMock` age como **substituto passivo**: não precisamos de persistência real; a calculadora segue o fluxo e nós assertamos **valores de retorno**.
- Em **`TestComMock`**, usamos o mesmo tipo (`MagicMock`), mas com **asserções de interação**: `assert_called_once_with(...)`, `assert_not_called()` quando uma exceção deve impedir `salvar()`.

Isso corresponde exatamente à distinção dos slides: *stub controla estado*; *mock verifica comportamento*.

### Tipos de teste de unidade citados na aula e onde aparecem

- **Entrada e saída / interface**: retorno de cada operação e `obter_ultimo_resultado()`.
- **Tipagem**: `TypeError` para tipos não numéricos; caso **`bool`** — em Python `bool` é subclasse de `int`, então `somar(True, 3)` é aceito; o teste documenta esse comportamento.
- **Condições de limite**: zeros, floats pequenos/grandes, divisor próximo de zero, expoente negativo e fracionário.
- **Valores fora do intervalo (domínio da operação)**: divisão por zero → `ValueError`.
- **Mensagens de erro**: `assertRaisesRegex` para não “passar silencioso” se a exceção não for lançada.
- **Fluxos de controle**: ramos de `dividir` (normal vs zero vs tipo inválido) e outros caminhos.

---

## Resolução da atividade (passo a passo)

1. **Implementar módulos** em `src/` conforme o enunciado.
2. **Parte 1**: em cada classe de teste, `setUp` cria `MagicMock()` e `Calculadora(self.repo)`. Cobrir **subtrair, multiplicar, dividir, potência** com pelo menos dois casos de E/S cada, além dos extras pedidos.
3. **Parte 2**: `HistoricoRepositorio()` real no `setUp`; validar encadeamento (`somar` → `multiplicar` com último resultado → `dividir`), contagem no repositório e formatos em `listar()`.
4. **Parte 3**: separar mentalmente **stub** (foco no resultado) e **mock** (foco em `salvar`). Implementar `assert_called_once_with` para **todas** as operações; o teste de `potencia` revela o operador errado no histórico se o bug ainda existir.
5. **Correção do bug**: em `potencia`, a linha de histórico deve refletir a operação `**`, não `*`.
6. **Cobertura**: rodar `coverage` até **100%** das linhas de `calculadora.py` (documentado no `relatorio.md`).

---

## Referências rápidas

- Slides: Aula 06 — integração, níveis de teste, Meszaros, exemplos `unittest.mock`.
- Enunciado: Atividade 06 — calculadora + repositório, tarefas e estrutura de entrega.
