import unittest
from core.board import Board
from core.checker import Ficha

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_configuracion_inicial(self):
        # Blancas en puntos 6, 8, 13, 24
        self.assertEqual(self.board.get_cantidad_fichas(6), 5)
        self.assertEqual(self.board.get_color_fichas(6), "blanco")
        # Negras en 1, 12, 17, 19
        self.assertEqual(self.board.get_cantidad_fichas(1), 2)
        self.assertEqual(self.board.get_color_fichas(1), "negro")

    def test_get_punto_fuera_rango(self):
        with self.assertRaises(ValueError):
            self.board.get_punto(0)
        self.assertEqual(self.board.get_cantidad_fichas(25), 0)
        self.assertIsNone(self.board.get_color_fichas(25))

    def test_puede_mover_y_captura(self):
        # vacío → True
        self.assertTrue(self.board.puede_mover_a(5, "blanco"))
        # bloqueo con 2 rivales
        self.board._puntos[7] = [Ficha("negro"), Ficha("negro")]
        self.assertFalse(self.board.puede_mover_a(7, "blanco"))
        # captura con 1 rival
        self.board._puntos[8] = [Ficha("negro")]
        self.assertTrue(self.board.puede_mover_a(8, "blanco"))
        # mover sin captura
        capt = self.board.mover_ficha(6,5,"blanco")
        self.assertIsNone(capt)
        # mover con captura
        # preparar ficha negra en 2
        self.board._puntos[2] = [Ficha("negro")]
        cap = self.board.mover_ficha(6,2,"blanco")
        self.assertIsNotNone(cap)
        self.assertTrue(cap.esta_en_barra())

    def test_puede_bear_off(self):
        # vaciar todos menos casa blanca
        for p in range(7,25):
            self.board._puntos[p] = []
        self.board._puntos[1] = [Ficha("blanco") for _ in range(15)]
        self.assertTrue(self.board.puede_bear_off("blanco"))
        self.assertFalse(self.board.puede_bear_off("negro"))

    def test_get_punto_valido_devuelve_lista_independiente(self):
        punto_6 = self.board.get_punto(6)
        self.assertIsInstance(punto_6, list)
        # Modifico la copia y no afecta al tablero original
        original = self.board.get_cantidad_fichas(6)
        punto_6.clear()
        self.assertEqual(self.board.get_cantidad_fichas(6), original)

    def test_get_punto_fuera_rango_levanta_error(self):
        with self.assertRaises(ValueError):
            self.board.get_punto(0)
        with self.assertRaises(ValueError):
            self.board.get_punto(25)

    def test_get_cantidad_y_color_fuera_rango(self):
        # get_cantidad_fichas fuera de rango devuelve 0
        self.assertEqual(self.board.get_cantidad_fichas(0), 0)
        self.assertEqual(self.board.get_cantidad_fichas(25), 0)
        # get_color_fichas fuera de rango devuelve None
        self.assertIsNone(self.board.get_color_fichas(0))
        self.assertIsNone(self.board.get_color_fichas(25))

    def test_get_color_fichas_en_punto_vacio(self):
        # asegurarse que un punto sin fichas retorna None
        # punto 5 está vacío en la configuración inicial
        self.assertEqual(self.board.get_cantidad_fichas(5), 0)
        self.assertIsNone(self.board.get_color_fichas(5))

    def test_puede_mover_a_distintas_condiciones(self):
        # destino fuera de tablero
        self.assertFalse(self.board.puede_mover_a(0, "blanco"))
        self.assertFalse(self.board.puede_mover_a(25, "negro"))
        # punto vacío → True
        self.assertTrue(self.board.puede_mover_a(5, "blanco"))
        # punto con fichas propias → True
        self.assertTrue(self.board.puede_mover_a(6, "blanco"))
        # punto con una ficha rival → True
        self.board._puntos[7] = [Ficha("negro")]
        self.assertTrue(self.board.puede_mover_a(7, "blanco"))
        # punto con dos fichas rivales → False
        self.board._puntos[8] = [Ficha("negro"), Ficha("negro")]
        self.assertFalse(self.board.puede_mover_a(8, "blanco"))

    def test_sacar_ficha_y_error_en_punto_vacío(self):
        # sacar ficha de un punto con fichas
        inicial = self.board.get_cantidad_fichas(6)
        ficha = self.board.sacar_ficha(6)
        self.assertIsInstance(ficha, Ficha)
        self.assertEqual(self.board.get_cantidad_fichas(6), inicial - 1)
        # intentar sacar de punto vacío → ValueError
        # vacío: punto 5
        with self.assertRaises(ValueError):
            self.board.sacar_ficha(5)

    def test_mover_ficha_rutas_varias(self):
        # mover sin captura
        inicial6 = self.board.get_cantidad_fichas(6)
        self.board._puntos[5] = []  # aseguramos destino vacío
        capt = self.board.mover_ficha(6, 5, "blanco")
        self.assertIsNone(capt)
        self.assertEqual(self.board.get_cantidad_fichas(6), inicial6 - 1)
        self.assertEqual(self.board.get_cantidad_fichas(5), 1)
        # preparar captura
        # pongo una ficha negra en 4
        self.board._puntos[4] = [Ficha("negro")]
        inicial_barra = 0
        capt2 = self.board.mover_ficha(5, 4, "blanco")
        self.assertIsInstance(capt2, Ficha)
        # la ficha capturada va a barra
        self.assertTrue(capt2.esta_en_barra())
        # y en destino queda la ficha blanca
        self.assertEqual(self.board.get_color_fichas(4), "blanco")

    def test_get_fichas_en_casa_y_puede_bear_off(self):
        # configuración inicial: no puede bear-off
        self.assertFalse(self.board.puede_bear_off("blanco"))
        self.assertFalse(self.board.puede_bear_off("negro"))
        # lleno solo casa blanca y vacío fuera de casa
        for p in range(1, 7):
            self.board._puntos[p] = [Ficha("blanco")] * 3
        for p in range(7, 25):
            self.board._puntos[p] = []
        self.assertEqual(self.board.get_fichas_en_casa("blanco"), 3 * 6)
        self.assertTrue(self.board.puede_bear_off("blanco"))
        # caso negro: lleno casa negra
        for p in range(19, 25):
            self.board._puntos[p] = [Ficha("negro")] * 2
        for p in range(1, 19):
            self.board._puntos[p] = []
        self.assertEqual(self.board.get_fichas_en_casa("negro"), 2 * 6)
        self.assertTrue(self.board.puede_bear_off("negro"))

    def test_mostrar_tablero_formato(self):
        salida = self.board.mostrar_tablero()
        # Debe contener cabecera y pie
        self.assertIn("Tablero de Backgammon", salida)
        self.assertIn("13 14 15 16 17 18", salida)
        self.assertIn("12 11 10  9  8  7", salida)


if __name__ == "__main__":
    unittest.main()