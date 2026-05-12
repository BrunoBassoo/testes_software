import sys
import unittest
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
_src = str(_root / "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

from calculadora import Calculadora  # noqa: E402
from repositorio import HistoricoRepositorio  # noqa: E402


class TestIntegracao(unittest.TestCase):
    def setUp(self):
        self.repo = HistoricoRepositorio()
        self.calc = Calculadora(self.repo)

    def test_operacoes_sequenciais(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(self.calc.obter_ultimo_resultado(), 4)
        self.calc.dividir(self.calc.obter_ultimo_resultado(), 2)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 10)
        self.assertEqual(self.repo.total(), 3)

    def test_historico_registra_formato_correto(self):
        self.calc.somar(2, 3)
        self.calc.multiplicar(4, 5)
        registros = self.repo.listar()
        self.assertIn("2 + 3 = 5", registros)
        self.assertIn("4 * 5 = 20", registros)

    def test_limpar_historico(self):
        self.calc.somar(1, 1)
        self.repo.limpar()
        self.assertEqual(self.repo.total(), 0)

    def test_extra_integracao_potencia_no_historico(self):
        self.calc.potencia(2, 3)
        self.assertIn("2 ** 3 = 8", self.repo.listar())
        self.assertEqual(self.repo.total(), 1)

    def test_extra_sequencia_com_subtracao(self):
        self.calc.somar(10, 5)
        self.calc.subtrair(self.calc.obter_ultimo_resultado(), 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 12)
        self.assertEqual(self.repo.total(), 2)


if __name__ == "__main__":
    unittest.main()
