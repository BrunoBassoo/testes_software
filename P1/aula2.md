# 🧠 Resumo – Simulação e Teste de Software (Aula 02)

## 🎯 Objetivo da Aula

Aprofundar em **testes unitários com pytest**, saindo do básico para um nível mais profissional:

* Princípios FIRST
* Padrão AAA
* Fixtures
* Parametrização
* Testes de exceções
* Organização de testes

👉 Insight:
Aqui começa a diferença entre **saber testar** e **testar bem de verdade**.

---

## 🧪 O que é um Bom Teste Unitário?

Um teste de qualidade deve ser:

* **Rápido** → executa em milissegundos
* **Isolado** → não depende de outros testes
* **Repetível** → sempre o mesmo resultado
* **Auto-verificável** → passa/falha automaticamente
* **Oportuno** → escrito junto ou antes do código

---

## 🧠 Princípios FIRST

* **F**ast
* **I**ndependent
* **R**epeatable
* **S**elf-validating
* **T**imely

👉 Tradução prática:
Se seu teste é lento, depende de banco ou API… ele já está errado.

---

## 📐 Padrão AAA (Arrange - Act - Assert)

Todo teste deve ter:

1. **Arrange** → preparar dados
2. **Act** → executar ação
3. **Assert** → verificar resultado

### Exemplo:

```python
# Arrange
x, y = 10, 5

# Act
resultado = dividir(x, y)

# Assert
assert resultado == 2
```

👉 Insight:
Código de teste desorganizado = difícil de manter.

---

## 🔎 Assertions

Tipos comuns:

```python
assert x == 5
assert y != 0
assert idade >= 18
assert "Python" in linguagens
assert not is_expired
```

👉 Regra:
Evite asserts vagos → sempre compare com valor esperado.

---

## ⚠️ Testando Exceções

### Exemplo:

```python
import pytest

with pytest.raises(ZeroDivisionError):
    dividir(10, 0)
```

### Validando mensagem:

```python
with pytest.raises(ValueError) as exc:
    validar_cpf("123")

assert "inválido" in str(exc.value)
```

👉 Insight:
Testar erro é tão importante quanto testar sucesso.

---

## 🔢 Problema com Float

Erro comum:

```python
assert calcular_media([1, 2]) == 1.5
```

Solução:

```python
assert resultado == pytest.approx(1.5)
```

👉 Motivo:
Problemas de precisão de ponto flutuante.

---

## 🔁 Fixtures

### O que são:

Funções que fornecem dados/setup para testes.

### Exemplo:

```python
@pytest.fixture
def usuario():
    return {"nome": "João"}
```

Uso:

```python
def test_usuario(usuario):
    assert usuario["nome"] == "João"
```

👉 Vantagens:

* Evita repetição
* Código mais limpo
* Setup automático

---

## ⏱️ Escopo de Fixtures

* `function` → novo a cada teste
* `class` → por classe
* `module` → por arquivo
* `session` → uma vez só

👉 Insight:
Escopo errado pode quebrar isolamento.

---

## 🔄 Setup e Teardown

```python
@pytest.fixture
def conexao():
    conn = conectar()

    yield conn

    conn.close()
```

👉 Antes do `yield` = setup
👉 Depois = limpeza automática

---

## 📁 Fixture pronta (tmp_path)

```python
def test_arquivo(tmp_path):
    arquivo = tmp_path / "dados.txt"
```

👉 Vantagem:
Não precisa gerenciar arquivos temporários.

---

## 🔁 Parametrização de Testes

### Problema:

Vários testes iguais com dados diferentes

### Solução:

```python
@pytest.mark.parametrize("entrada, esperado", [
    (2, 4),
    (3, 9),
])
def test_quadrado(entrada, esperado):
    assert quadrado(entrada) == esperado
```

👉 Insight:
Um teste → vários cenários

---

## 🏷️ IDs customizados

```python
@pytest.mark.parametrize("cpf,valido", [...],
ids=["valido", "invalido"])
```

👉 Melhora leitura do resultado no pytest

---

## 🔗 Parametrização + Fixture

```python
def test_somar(calc, a, b, esperado):
    assert calc.somar(a, b) == esperado
```

👉 Combinação poderosa → muito usada em projeto real

---

## 🧱 Organização com Classes

```python
class TestCarrinho:
    def test_vazio(self):
        ...
```

👉 Usado para agrupar testes relacionados

---

## 📦 conftest.py

* Arquivo para compartilhar fixtures
* Disponível para todos os testes

Estrutura:

```
tests/
  conftest.py
  test_x.py
```

👉 Muito usado em projetos grandes

---

## 🏷️ Nomes de Testes

Ruim:

* test_1()
* test_funcao()

Bom:

* test_divisao_por_zero_levanta_excecao()

👉 Regra:
Nome = comportamento + resultado esperado

---

## 🚨 Test Smells

* Testes Dependentes:
Um teste depende do resultado de outro - viola princípio Independent

* Testes Lentos:
Leva segundos/minutos - viola princípio Fast

* Setup Excessivo:
Muitas linhas de preparação - use fixtures!

* Assertions Vagas:
assert x vs assert x == valor_esperado

* Teste Testando Múltiplas Coisas:
Dificulta identificar o que falhou - divida em testes menores

👉 Se aparecer isso → refatora

---

## ⚖️ Um Assert por Teste?

* **Pró:** mais claro
* **Contra:** pode gerar repetição

👉 Melhor regra:
**Um comportamento por teste**, não necessariamente um assert

---

## 🧪 Exercício importante (CPF)

Você precisa saber:

* Validar CPF
* Testar com:

  * Fixtures
  * Parametrização
  * Exceções
  * AAA

👉 Isso aqui é praticamente prova prática

---

# 🔥 O que você PRECISA decorar

1. Princípios **FIRST**
2. Padrão **AAA**
3. Como usar `pytest.raises`
4. Diferença entre assert comum e `approx`
5. **Fixtures** (conceito + uso)
6. **Escopos de fixture**
7. **Parametrização**
8. Arquivo `conftest.py`
9. O que são **test smells**
10. Boa nomenclatura de testes

---

# ⚠️ Visão estratégica

* Teste bom = rápido + isolado + confiável
* Fixtures mal usadas → testes frágeis
* Parametrização → reduz código e aumenta cobertura
* Teste que depende de banco/API → erro de design
* Código de teste também precisa ser bem escrito

👉 Mentalidade correta:
Teste não é só validação — é **design de qualidade do sistema**
