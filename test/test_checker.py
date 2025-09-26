import unittest
from core.checker import Ficha

class TestFicha(unittest.TestCase):

    def test_posicion_y_estado(self):
        f = Ficha("blanco")
        self.assertFalse(f.esta_en_tablero())
        f.set_posicion(5)
        self.assertTrue(f.esta_en_tablero())
        self.assertEqual(f.get_posicion(), 5)

    def test_mover_a_barra_y_fuera(self):
        f = Ficha("negro")
        f.mover_a_barra()
        self.assertTrue(f.esta_en_barra())
        f.mover_fuera_tablero()
        self.assertTrue(f.esta_fuera_tablero())
        self.assertFalse(f.esta_en_tablero())

    def test_eq_y_str(self):
        f1 = Ficha("blanco")
        f2 = Ficha("blanco")
        self.assertEqual(str(f1), "Ficha blanco (sin posición)")
        f1.set_posicion(2)
        f2.set_posicion(2)
        self.assertEqual(f1, f2)

if __name__ == "__main__":

