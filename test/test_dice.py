import unittest
from unittest.mock import patch
from core.dice import Dado


class TestDado(unittest.TestCase):
    def test_estado_inicial(self):
        d = Dado()
        self.assertEqual(d.get_valores(), (0, 0))
        self.assertFalse(d.es_doble())

    def test_lanzar_con_inyectadas(self):
        d = Dado()
        d.set_proximas_tiradas([(1, 2), (3, 3)])
        v1 = d.lanzar()
        v2 = d.lanzar()
        self.assertEqual(v1, (1, 2))
        self.assertEqual(v2, (3, 3))
        self.assertTrue(d.es_doble())

    def test_usar_lanzadas_respetando_fifo(self):
        d = Dado()
        d.set_proximas_tiradas([(2, 5), (6, 1), (4, 4)])
        self.assertEqual(d.lanzar(), (2, 5))
        self.assertEqual(d.lanzar(), (6, 1))
        self.assertEqual(d.lanzar(), (4, 4))
        self.assertTrue(d.es_doble())

    @patch("core.dice.random.randint", side_effect=[6, 2])
    def test_lanzar_random_rango(self, _mock_randint):
        d = Dado()
        v = d.lanzar()
        self.assertEqual(v, (6, 2))
        self.assertFalse(d.es_doble())

import unittest
from core.dice import Dado


class TestDiceExtra(unittest.TestCase):
    # Cobertura: alias lanzar_dados y get_proximas_tiradas
    def test_aliases_y_copia_de_lista(self):
        d = Dado()
        d.set_proximas_tiradas([(1, 1)])
        self.assertEqual(d.get_proximas_tiradas(), [(1, 1)])  # alias getter
        # lanzar_dados debe usar el mismo flujo que lanzar
        self.assertEqual(d.lanzar_dados(), (1, 1))
        # la lista devuelta por el getter es copia (no afecta interno)
        lista = d.get_proximas_tiradas()
        lista.append((6, 6))
        self.assertEqual(d.get_proximas_tiradas(), [])


if __name__ == "__main__":
    unittest.main()
