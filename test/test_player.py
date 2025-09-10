import unittest
from core.player import Jugador


class TestJugador(unittest.TestCase):
    def test_estado_inicial(self):
        j = Jugador("blanco")
        self.assertEqual(j.get_color(), "blanco")
        self.assertEqual(j.en_barra(), 0)
        self.assertEqual(j.fuera(), 0)
        self.assertFalse(j.ha_ganado())

    def test_agregar_y_sacar_de_barra(self):
        j = Jugador("negro")
        j.agregar_a_barra()
        j.agregar_a_barra()
        self.assertEqual(j.en_barra(), 2)
        j.quitar_de_barra()
        self.assertEqual(j.en_barra(), 1)

    def test_barra_sin_fichas_no_rompe(self):
        j = Jugador("blanco")
        j.quitar_de_barra()
        self.assertEqual(j.en_barra(), 0)

    def test_agregar_fuera_incrementa_y_ganar(self):
        j = Jugador("blanco")
        for _ in range(Jugador.TOTAL_FICHAS):
            j.agregar_fuera()
        self.assertEqual(j.fuera(), Jugador.TOTAL_FICHAS)
        self.assertTrue(j.ha_ganado())
        # no pasa de 15
        j.agregar_fuera()
        self.assertEqual(j.fuera(), Jugador.TOTAL_FICHAS)


if __name__ == "__main__":
    unittest.main()

