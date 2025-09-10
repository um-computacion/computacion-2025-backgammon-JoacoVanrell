import unittest
from core.checker import Ficha


class TestFicha(unittest.TestCase):
    def test_estado_inicial(self):
        f = Ficha("blanco")
        self.assertEqual(f.get_color(), "blanco")
        self.assertIsNone(f.get_posicion())
        self.assertFalse(f.esta_en_barra())
        self.assertFalse(f.esta_fuera_tablero())
        self.assertFalse(f.esta_en_tablero())

    def test_set_posicion(self):
        f = Ficha("negro")
        f.set_posicion(12)
        self.assertEqual(f.get_posicion(), 12)
        self.assertTrue(f.esta_en_tablero())
        self.assertFalse(f.esta_en_barra())
        self.assertFalse(f.esta_fuera_tablero())

    def test_mover_a_barra(self):
        f = Ficha("blanco")
        f.set_posicion(6)
        f.mover_a_barra()
        self.assertTrue(f.esta_en_barra())
        self.assertIsNone(f.get_posicion())
        self.assertFalse(f.esta_fuera_tablero())
        self.assertFalse(f.esta_en_tablero())

    def test_mover_fuera_tablero(self):
        f = Ficha("negro")
        f.set_posicion(2)
        f.mover_fuera_tablero()
        self.assertTrue(f.esta_fuera_tablero())
        self.assertIsNone(f.get_posicion())
        self.assertFalse(f.esta_en_barra())
        self.assertFalse(f.esta_en_tablero())

    def test_str_representacion(self):
        f = Ficha("blanco")
        self.assertIn("sin posición", str(f))
        f.set_posicion(24)
        self.assertIn("posición 24", str(f))
        f.mover_a_barra()
        self.assertIn("en barra", str(f))
        f.mover_fuera_tablero()
        self.assertIn("fuera del tablero", str(f))

import unittest
from core.checker import Ficha


class TestCheckerExtra(unittest.TestCase):
    # Cobertura: __eq__ con mismo estado
    def test_eq_mismo_estado(self):
        a = Ficha("blanco")
        b = Ficha("blanco")
        self.assertTrue(a == b)

    # Cobertura: __eq__ contra objeto de otro tipo
    def test_eq_objeto_distinto(self):
        a = Ficha("negro")
        self.assertFalse(a == 123)  # debe ser False, no excepción

    # Cobertura: __eq__ con distinto estado
    def test_eq_distinto_estado(self):
        a = Ficha("blanco")
        b = Ficha("blanco")
        a.set_posicion(6)
        self.assertFalse(a == b)


if __name__ == "__main__":
    unittest.main()
