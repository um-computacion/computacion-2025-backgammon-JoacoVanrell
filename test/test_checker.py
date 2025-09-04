"""
Tests unitarios para la clase Ficha del juego de Backgammon.
"""
import unittest
from core.checker import Ficha


class TestFicha(unittest.TestCase):

    def test_estado_inicial(self):
        f = Ficha("blanco")
        self.assertEqual(f.get_color(), "blanco")
        self.assertIsNone(f.get_posicion())
        self.assertFalse(f.esta_en_barra())
        self.assertFalse(f.esta_fuera_tablero())

    def test_set_posicion(self):
        f = Ficha("negro")
        f.set_posicion(10)
        self.assertEqual(f.get_posicion(), 10)
        self.assertTrue(f.esta_en_tablero())

    def test_mover_a_barra(self):
        f = Ficha("blanco")
        f.set_posicion(5)
        f.mover_a_barra()
        self.assertTrue(f.esta_en_barra())
        self.assertIsNone(f.get_posicion())

    def test_mover_fuera_tablero(self):
        f = Ficha("negro")
        f.mover_fuera_tablero()
        self.assertTrue(f.esta_fuera_tablero())
        self.assertIsNone(f.get_posicion())

    def test_transiciones_basicas(self):
        f = Ficha("blanco")
        f.set_posicion(8)
        self.assertTrue(f.esta_en_tablero())
        
        f.mover_a_barra()
        self.assertTrue(f.esta_en_barra())
        
        f.set_posicion(12)
        self.assertTrue(f.esta_en_tablero())
        self.assertFalse(f.esta_en_barra())


if __name__ == "__main__":
    unittest.main()