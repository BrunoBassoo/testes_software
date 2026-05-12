import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock

_root = Path(__file__).resolve().parent.parent
_src = str(_root / "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

from calculadora import Calculadora  # noqa: E402


class TestEntradaSaida(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_soma_retorna_valor_correto(self):
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    def test_subtrair_retorna_valor_correto(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)

    def test_subtrair_atualiza_ultimo_resultado(self):
        self.calc.subtrair(10, 4)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 6)

    def test_multiplicar_retorna_valor_correto(self):
        self.assertEqual(self.calc.multiplicar(6, 7), 42)

    def test_multiplicar_atualiza_ultimo_resultado(self):
        self.calc.multiplicar(6, 7)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 42)

    def test_dividir_retorna_valor_correto(self):
        self.assertEqual(self.calc.dividir(20, 4), 5.0)

    def test_dividir_atualiza_ultimo_resultado(self):
        self.calc.dividir(20, 4)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 5.0)

    def test_potencia_retorna_valor_correto(self):
        self.assertEqual(self.calc.potencia(2, 8), 256)

    def test_potencia_atualiza_ultimo_resultado(self):
        self.calc.potencia(2, 8)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 256)

    def test_extra_entrada_saida_soma_negativos(self):
        self.assertEqual(self.calc.somar(-3, -2), -5)


class TestTipagem(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_tipagem_string_rejeitada(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_tipagem_none_rejeitado(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)

    def test_tipagem_subtrair_primeiro_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair("x", 1)

    def test_tipagem_subtrair_segundo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(1, [])

    def test_tipagem_multiplicar(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar(1, {1: 2})

    def test_tipagem_dividir(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(1.0, "2")

    def test_tipagem_potencia(self):
        with self.assertRaises(TypeError):
            self.calc.potencia(None, 2)

    def test_bool_e_aceito_por_ser_subclasse_de_int(self):
        self.assertEqual(self.calc.somar(True, 3), 4)

    def test_extra_tipagem_lista_rejeitada_em_ambos(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar([1], [2])


class TestLimites(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_limite_float_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_float_grande(self):
        import sys

        grande = sys.float_info.max / 2
        resultado = self.calc.somar(grande, grande)
        self.assertFalse(resultado == float("inf"))

    def test_dividir_divisor_muito_pequeno(self):
        r = self.calc.dividir(1.0, 1e-300)
        self.assertGreater(r, 1e299)

    def test_potencia_expoente_negativo(self):
        self.assertAlmostEqual(self.calc.potencia(2, -1), 0.5)

    def test_potencia_expoente_fracionario(self):
        self.assertAlmostEqual(self.calc.potencia(4, 0.5), 2.0)

    def test_extra_limite_subtrair_zero(self):
        self.assertEqual(self.calc.subtrair(0, 0), 0)


class TestValoresForaDoIntervalo(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_divisao_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_extra_divisao_por_zero_com_negativo(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(-5, 0)


class TestMensagensDeErro(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.somar("x", 1)

    def test_mensagem_tipo_invalido_subtrair(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.subtrair(1, "a")

    def test_mensagem_tipo_invalido_multiplicar(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.multiplicar(object(), 1)

    def test_mensagem_tipo_invalido_potencia(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.potencia("2", 2)


class TestFluxosDeControle(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_caminho_divisao_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_caminho_divisao_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_caminho_tipagem_divisao(self):
        with self.assertRaises(TypeError):
            self.calc.dividir("10", 2)

    def test_potencia_expoente_zero_ramifica_retorno(self):
        self.assertEqual(self.calc.potencia(5, 0), 1)

    def test_extra_fluxo_multiplicar_por_zero(self):
        self.assertEqual(self.calc.multiplicar(100, 0), 0)


if __name__ == "__main__":
    unittest.main()
