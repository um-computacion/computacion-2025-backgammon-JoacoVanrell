import unittest
from core.board import Board
from core.checker import Ficha


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.b = Board()

    def test_iniciales_colores_y_cantidades(self):
        self.assertEqual(self.b.get_color_fichas(24), "blanco")
        self.assertEqual(self.b.get_cantidad_fichas(24), 2)
        self.assertEqual(self.b.get_color_fichas(13), "blanco")
        self.assertEqual(self.b.get_cantidad_fichas(13), 5)

        self.assertEqual(self.b.get_color_fichas(1), "negro")
        self.assertEqual(self.b.get_cantidad_fichas(1), 2)
        self.assertEqual(self.b.get_color_fichas(12), "negro")
        self.assertEqual(self.b.get_cantidad_fichas(12), 5)

    def test_puede_mover_a_vacio(self):
        # hago vacío el punto 10
        self.b._puntos[10] = []
        self.assertTrue(self.b.puede_mover_a(10, "blanco"))
        self.assertTrue(self.b.puede_mover_a(10, "negro"))

    def test_puede_mover_a_mismo_color(self):
        # garantizo que 24 tiene blancas
        self.assertEqual(self.b.get_color_fichas(24), "blanco")
        self.assertTrue(self.b.puede_mover_a(24, "blanco"))

    def test_puede_mover_a_un_rival_capturable(self):
        # punto 5 con 1 negra
        self.b._puntos[5] = [Ficha("negro")]
        self.assertTrue(self.b.puede_mover_a(5, "blanco"))

    def test_bloqueado_por_dos_o_mas_rivales(self):
        # punto 7 con 2 negras
        self.b._puntos[7] = [Ficha("negro"), Ficha("negro")]
        self.assertFalse(self.b.puede_mover_a(7, "blanco"))

    def test_mover_ficha_y_capturar(self):
        # preparo: blanco en 6, negro solo en 5
        self.b._puntos[6] = [Ficha("blanco")]
        self.b._puntos[6][0].set_posicion(6)
        self.b._puntos[5] = [Ficha("negro")]
        self.b._puntos[5][0].set_posicion(5)

        capt = self.b.mover_ficha(6, 5, "blanco")
        self.assertIsNotNone(capt)
        self.assertEqual(self.b.get_color_fichas(5), "blanco")
        self.assertEqual(self.b.get_cantidad_fichas(5), 1)

    def test_mover_falla_origen_vacio(self):
        self.b._puntos[9] = []
        with self.assertRaises(ValueError):
            self.b.mover_ficha(9, 10, "blanco")

    def test_mover_falla_origen_de_otro_color(self):
        # 1 es de negras por inicial
        with self.assertRaises(ValueError):
            self.b.mover_ficha(1, 2, "blanco")

    def test_mover_falla_destino_bloqueado(self):
        # destino 5 bloqueado por 2 negras
        self.b._puntos[6] = [Ficha("blanco")]
        self.b._puntos[6][0].set_posicion(6)
        self.b._puntos[5] = [Ficha("negro"), Ficha("negro")]
        for f in self.b._puntos[5]:
            f.set_posicion(5)

        with self.assertRaises(ValueError):
            self.b.mover_ficha(6, 5, "blanco")

    def test_es_movimiento_valido(self):
        # vacío 10 y pongo un blanco en 9 para mover a 10
        self.b._puntos[9] = [Ficha("blanco")]
        self.b._puntos[9][0].set_posicion(9)
        self.b._puntos[10] = []

        self.assertTrue(self.b.es_movimiento_valido(9, 10, "blanco"))
        self.assertFalse(self.b.es_movimiento_valido(9, 10, "negro"))
        self.assertFalse(self.b.es_movimiento_valido(25, 10, "blanco"))
        self.assertFalse(self.b.es_movimiento_valido(9, 0, "blanco"))

    def test_puede_bear_off(self):
        # todas las blancas en casa 1..6 y ninguna blanca fuera de 1..6
        self.b._puntos = [[] for _ in range(25)]
        # 15 blancas distribuidas en casa
        self.b._puntos[6] = [Ficha("blanco") for _ in range(5)]
        self.b._puntos[5] = [Ficha("blanco") for _ in range(5)]
        self.b._puntos[1] = [Ficha("blanco") for _ in range(5)]
        for p in (6, 5, 1):
            for f in self.b._puntos[p]:
                f.set_posicion(p)
        self.assertTrue(self.b.puede_bear_off("blanco"))
        self.assertFalse(self.b.puede_bear_off("negro"))

import unittest
from core.board import Board


class TestBoardExtra(unittest.TestCase):
    def setUp(self):
        self.b = Board()

    # Cobertura: get_punto fuera de rango (lanzas ValueError)
    def test_get_punto_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            self.b.get_punto(0)
        with self.assertRaises(ValueError):
            self.b.get_punto(25)

    # Cobertura: get_cantidad_fichas / get_color_fichas fuera de rango
    def test_cantidad_y_color_fuera_de_rango(self):
        self.assertEqual(self.b.get_cantidad_fichas(0), 0)
        self.assertEqual(self.b.get_cantidad_fichas(25), 0)
        self.assertIsNone(self.b.get_color_fichas(0))
        self.assertIsNone(self.b.get_color_fichas(25))

    # Cobertura: puede_mover_a fuera de rango (retorna False)
    def test_puede_mover_a_fuera_de_rango(self):
        self.assertFalse(self.b.puede_mover_a(0, "blanco"))
        self.assertFalse(self.b.puede_mover_a(25, "negro"))

    # Cobertura: mostrar_tablero (recorre ambas mitades y líneas)
    def test_mostrar_tablero_formato_basico(self):
        s = self.b.mostrar_tablero()
        self.assertIsInstance(s, str)
        # encabezados y separadores presentes
        self.assertIn("Tablero de Backgammon", s)
        self.assertIn("13 14 15 16 17 18", s)
        self.assertIn("12 11 10", s)
        self.assertIn("|", s)
        self.assertIn("=" * 50, s)

if __name__ == "__main__":
    unittest.main()
