import unittest
from core.player import Jugador

class TestJugador(unittest.TestCase):

    def test_estado_inicial_y_getters(self):
        j = Jugador("blanco", "Juan")
        self.assertEqual(j.get_color(), "blanco")
        self.assertEqual(j.get_nombre(), "Juan")
        self.assertEqual(j.get_fichas_en_barra(), 0)
        self.assertEqual(j.get_fichas_fuera(), 0)
        self.assertFalse(j.ha_ganado())

    def test_agregar_y_sacar_de_barra(self):
        j = Jugador("negro")
        j.agregar_a_barra()
        self.assertEqual(j.get_fichas_en_barra(), 1)
        j.sacar_de_barra()
        self.assertEqual(j.get_fichas_en_barra(), 0)

    def test_agregar_fuera_y_condicion_victoria(self):
        j = Jugador("blanco")
        for _ in range(Jugador.TOTAL_FICHAS):
            j.agregar_fuera()
        self.assertTrue(j.ha_ganado())
        self.assertEqual(j.get_fichas_fuera(), Jugador.TOTAL_FICHAS)
    
    def test_sacar_de_barra_sin_fichas(self):
        j = Jugador("blanco")
        # Sacar cuando no hay fichas en barra no debe bajarlo de 0
        j.sacar_de_barra()
        self.assertEqual(j.get_fichas_en_barra(), 0)

    def test_agregar_fuera_no_excede_total(self):
        j = Jugador("negro")
        # Intentar agregar más fichas fuera que TOTAL_FICHAS
        for _ in range(Jugador.TOTAL_FICHAS + 5):
            j.agregar_fuera()
        self.assertEqual(j.get_fichas_fuera(), Jugador.TOTAL_FICHAS)

if __name__ == "__main__":
    unittest.main()
