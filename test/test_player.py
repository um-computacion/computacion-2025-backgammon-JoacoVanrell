import unittest
from core.player import Jugador

class TestJugador(unittest.TestCase):

    def test_estado_inicial(self):
        j = Jugador("Juan", "blanco")
        self.assertEqual(j.get_nombre(), "Juan")
        self.assertEqual(j.get_color(), "blanco")
        self.assertEqual(j.get_fichas_totales(), 15)

    def test_barra_sin_fichas_no_rompe(self):
        j = Jugador("Test", "blanco")
        j.sacar_de_barra()
        self.assertEqual(j.get_fichas_en_barra(), 0)

    def test_agregar_y_sacar_de_barra(self):
        j = Jugador("Test", "negro")
        j.agregar_a_barra()
        self.assertEqual(j.get_fichas_en_barra(), 1)
        j.sacar_de_barra()
        self.assertEqual(j.get_fichas_en_barra(), 0)

    def test_agregar_fuera_incrementa(self):
        j = Jugador("Test", "blanco")
        self.assertEqual(j.get_fichas_fuera(), 0)
        j.agregar_fuera()
        self.assertEqual(j.get_fichas_fuera(), 1)

if __name__ == "__main__":
    unittest.main()
