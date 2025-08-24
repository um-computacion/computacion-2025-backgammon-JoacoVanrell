import random

class Dado:

    def __init__(self):
        self.__caras__ = 6

    def lanzar(self) -> int:
        return random.randint(1, self.__caras__)


class Dados:

    def __init__(self):
        self.__dado1__ = Dado()
        self.__dado2__ = Dado()

    def lanzar(self) -> tuple[int, int]:
        return self.__dado1__.lanzar(), self.__dado2__.lanzar()

import unittest

class TestDado(unittest.TestCase):
    def test_valor_en_rango(self):
        d = Dado()
        for _ in range(100):
            val = d.lanzar()
            self.assertGreaterEqual(val, 1)
            self.assertLessEqual(val, 6)

    def test_tipo_entero(self):
        d = Dado()
        self.assertIsInstance(d.lanzar(), int)


class TestDados(unittest.TestCase):
    def test_devuelve_tupla(self):
        dados = Dados()
        valores = dados.lanzar()
        self.assertIsInstance(valores, tuple)
        self.assertEqual(len(valores), 2)

    def test_valores_en_rango(self):
        dados = Dados()
        for _ in range(100):
            v1, v2 = dados.lanzar()
            self.assertIn(v1, range(1, 7))
            self.assertIn(v2, range(1, 7))


if __name__ == "__main__":
    unittest.main(verbosity=2)
