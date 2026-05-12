import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

_root = Path(__file__).resolve().parent.parent
_src = str(_root / "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

from calculadora import Calculadora  # noqa: E402


class TestComStub(unittest.TestCase):
    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)

    def test_extra_stub_subtrair_sem_persistencia_real(self):
        self.calc.subtrair(9, 4)
        self.stub_repo.salvar.assert_called()


class TestComMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_nao_chamado_em_excecao(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)
        self.mock_repo.salvar.assert_not_called()

    def test_mock_subtrair_string_salvar(self):
        self.calc.subtrair(7, 2)
        self.mock_repo.salvar.assert_called_once_with("7 - 2 = 5")

    def test_mock_multiplicar_string_salvar(self):
        self.calc.multiplicar(3, 4)
        self.mock_repo.salvar.assert_called_once_with("3 * 4 = 12")

    def test_mock_dividir_string_salvar(self):
        self.calc.dividir(8, 2)
        self.mock_repo.salvar.assert_called_once_with("8 / 2 = 4.0")

    def test_mock_potencia_string_correta_apos_correcao(self):
        self.calc.potencia(2, 3)
        self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")

    def test_mock_potencia_detecta_operador_no_historico(self):
        self.calc.potencia(5, 2)
        args, _ = self.mock_repo.salvar.call_args
        linha = args[0]
        self.assertIn("**", linha)
        self.assertNotRegex(linha, r"5 \* 2 = 25")

    def test_mock_dividir_nao_salva_em_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(1, 0)
        self.mock_repo.salvar.assert_not_called()

    def test_extra_mock_multiplicar_nao_chama_salvar_em_typeerror(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar("a", 1)
        self.mock_repo.salvar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
