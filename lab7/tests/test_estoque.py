"""
Suite de testes do estoque — metodologia TDD (Aula 07).

Cada bloco abaixo segue a sequência pedida no enunciado:
  RED    → escrever o teste primeiro (falha até a funcionalidade existir);
  GREEN  → implementar o mínimo em `src/estoque.py` para passar;
  REFACTOR → melhorar design sem quebrar testes (comentários também em estoque.py).

A ordem dos testes reflete a ordem sugerida de desenvolvimento orientado a testes.
"""
import sys
import unittest
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
_src = str(_root / "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

from estoque import Estoque  # noqa: E402


class TestEstoqueTDD(unittest.TestCase):
    # -------------------------------------------------------------------------
    # Ciclo 1 — adicionar_produto + consultar_quantidade (produto novo)
    # RED: falha até existir classe Estoque e métodos mínimos.
    # GREEN: __init__, adicionar_produto, consultar_quantidade.
    # REFACTOR: consolidar dict interno e validações nos ciclos seguintes.
    # -------------------------------------------------------------------------
    def test_adicionar_produto_novo_consulta_quantidade(self):
        e = Estoque()
        e.adicionar_produto("caneta", 10)
        self.assertEqual(e.consultar_quantidade("caneta"), 10)

    # -------------------------------------------------------------------------
    # Ciclo 2 — consultar produto inexistente retorna 0 (regra do enunciado)
    # RED: falha se consultar levantar exceção ou não retornar 0.
    # GREEN: consultar_quantidade usa .get(nome, 0).
    # -------------------------------------------------------------------------
    def test_consultar_produto_inexistente_retorna_zero(self):
        e = Estoque()
        self.assertEqual(e.consultar_quantidade("inexistente"), 0)

    # -------------------------------------------------------------------------
    # Ciclo 3 — adicionar ao produto já existente incrementa (não substitui)
    # RED: segundo adicionar não pode zerar/substituir quantidade anterior.
    # GREEN: usar acumulação self._itens[nome] = anterior + q.
    # -------------------------------------------------------------------------
    def test_adicionar_produto_existente_incrementa_quantidade(self):
        e = Estoque()
        e.adicionar_produto("papel", 5)
        e.adicionar_produto("papel", 3)
        self.assertEqual(e.consultar_quantidade("papel"), 8)

    # -------------------------------------------------------------------------
    # Ciclo 4 — não permitir adicionar quantidade <= 0
    # RED: espera ValueError para quantidade zero ou negativa.
    # GREEN: validação no início de adicionar_produto.
    # REFACTOR: método _validar_quantidade_positiva compartilhado com remover.
    # -------------------------------------------------------------------------
    def test_adicionar_quantidade_zero_levanta_valueerror(self):
        e = Estoque()
        with self.assertRaises(ValueError):
            e.adicionar_produto("x", 0)

    def test_adicionar_quantidade_negativa_levanta_valueerror(self):
        e = Estoque()
        with self.assertRaises(ValueError):
            e.adicionar_produto("x", -1)

    # -------------------------------------------------------------------------
    # Ciclo 5 — remover_produto reduz quantidade
    # RED: falha até existir remover_produto.
    # GREEN: decrementar e remover chave se zerar (listar só > 0).
    # -------------------------------------------------------------------------
    def test_remover_produto_diminui_quantidade(self):
        e = Estoque()
        e.adicionar_produto("clipes", 20)
        e.remover_produto("clipes", 7)
        self.assertEqual(e.consultar_quantidade("clipes"), 13)

    # -------------------------------------------------------------------------
    # Ciclo 5b — remover todas as unidades: consulta volta a 0 e listagem esvazia
    # GREEN/REFACTOR: ao zerar, remover a chave interna mantém invariantes de listar/consultar.
    # -------------------------------------------------------------------------
    def test_remover_todo_estoque_consulta_zero_e_lista_vazia(self):
        e = Estoque()
        e.adicionar_produto("lapis", 4)
        e.remover_produto("lapis", 4)
        self.assertEqual(e.consultar_quantidade("lapis"), 0)
        self.assertEqual(e.listar_produtos(), [])

    # -------------------------------------------------------------------------
    # Ciclo 6 — não remover mais do que o disponível
    # RED: remover excesso deve falhar (ValueError).
    # GREEN: comparar quantidade com disponível antes de alterar estado.
    # -------------------------------------------------------------------------
    def test_remover_mais_que_disponivel_levanta_valueerror(self):
        e = Estoque()
        e.adicionar_produto("borracha", 2)
        with self.assertRaisesRegex(
            ValueError,
            "Não é possível remover mais unidades do que o disponível",
        ):
            e.remover_produto("borracha", 5)

    # -------------------------------------------------------------------------
    # Ciclo 7 — remover quantidade <= 0 não permitido
    # RED: mesmo contrato de adicionar para valores não positivos.
    # GREEN: reutilizar validação positiva em remover_produto.
    # -------------------------------------------------------------------------
    def test_remover_quantidade_zero_levanta_valueerror(self):
        e = Estoque()
        e.adicionar_produto("a", 1)
        with self.assertRaises(ValueError):
            e.remover_produto("a", 0)

    # -------------------------------------------------------------------------
    # Ciclo 8 — remover de produto inexistente (disponível = 0)
    # RED: qualquer remoção > 0 sem estoque deve falhar.
    # GREEN: disponivel = self._itens.get(nome, 0).
    # -------------------------------------------------------------------------
    def test_remover_produto_inexistente_levanta_valueerror(self):
        e = Estoque()
        with self.assertRaises(ValueError):
            e.remover_produto("fantasma", 1)

    # -------------------------------------------------------------------------
    # Ciclo 9 — listar_produtos: apenas quantidade > 0; estoque vazio -> []
    # RED: listar vazio; após remover tudo, produto some da listagem.
    # GREEN: filtrar itens com q > 0; ordenar para ordem estável nos testes.
    # -------------------------------------------------------------------------
    def test_listar_produtos_vazio(self):
        self.assertEqual(Estoque().listar_produtos(), [])

    def test_listar_produtos_apenas_com_estoque_positivo(self):
        e = Estoque()
        e.adicionar_produto("b", 1)
        e.adicionar_produto("a", 2)
        self.assertEqual(e.listar_produtos(), ["a", "b"])
        e.remover_produto("b", 1)
        self.assertEqual(e.listar_produtos(), ["a"])

    # -------------------------------------------------------------------------
    # Ciclo 10 — produto_mais_estocado: None se vazio; nome correto caso contrário
    # RED: estoque vazio retorna None; com vários, retorna o de maior q.
    # GREEN: max sobre valores; REFACTOR: desempate lexicográfico em estoque.py.
    # -------------------------------------------------------------------------
    def test_produto_mais_estocado_estoque_vazio_retorna_none(self):
        self.assertIsNone(Estoque().produto_mais_estocado())

    def test_produto_mais_estocado_retorna_nome_maior_quantidade(self):
        e = Estoque()
        e.adicionar_produto("p1", 10)
        e.adicionar_produto("p2", 40)
        e.adicionar_produto("p3", 25)
        self.assertEqual(e.produto_mais_estocado(), "p2")

    def test_produto_mais_estocado_empate_escolhe_lexicografico(self):
        e = Estoque()
        e.adicionar_produto("zebra", 5)
        e.adicionar_produto("abacaxi", 5)
        self.assertEqual(e.produto_mais_estocado(), "abacaxi")


if __name__ == "__main__":
    unittest.main()
