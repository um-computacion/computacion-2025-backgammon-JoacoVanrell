import unittest
from core.dice import Dado

class TestDado(unittest.TestCase):
    def test_estado_inicial(self):
        d = Dado()
        self.assertEqual(d.get_proximas_tiradas(), [])
        self.assertEqual(d.get_resultado_dados(), (0, 0))
        self.assertFalse(d.es_doble())

    def test_lanzar_dados_devuelve_valores_validos(self):
        d = Dado()
        vals = d.lanzar_dados()
        self.assertIn(len(vals), (2, 4))
        for v in vals:
            self.assertGreaterEqual(v, 1)
            self.assertLessEqual(v, 6)
        r1, r2 = d.get_resultado_dados()
        self.assertTrue(1 <= r1 <= 6)
        self.assertTrue(1 <= r2 <= 6)

    def test_es_doble_coincide_con_longitud(self):
        d = Dado()
        vals = d.lanzar_dados()
        if len(vals) == 4:
            self.assertTrue(d.es_doble())
        else:
            self.assertFalse(d.es_doble())

    def test_usar_lanzada_respeta_cantidad(self):
        d = Dado()
        vals = d.lanzar_dados()
        v = vals[0]
        # siempre debería poder usarse al menos una vez
        self.assertTrue(d.usar_lanzada(v))
        if len(vals) == 2:
            # si no es doble, ya no debería poder usarse de nuevo
            self.assertFalse(d.usar_lanzada(v))
        else:
            # si es doble, se puede usar hasta 4 veces
            self.assertTrue(d.usar_lanzada(v))   # 2da
            self.assertTrue(d.usar_lanzada(v))   # 3ra
            self.assertTrue(d.usar_lanzada(v))   # 4ta
            self.assertFalse(d.usar_lanzada(v))  # 5ta ya no

if __name__ == "__main__":
    unittest.main()
