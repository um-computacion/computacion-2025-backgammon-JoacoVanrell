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

    def test_usar_lanzada_respeta_cantidad(self):
        d = Dado()
        vals = d.lanzar_dados()
        v = vals[0]
        self.assertTrue(d.usar_lanzada(v))
        if len(vals) == 2:
            self.assertFalse(d.usar_lanzada(v))
        else:
            # si es doble, se puede usar hasta 4 veces
            self.assertTrue(d.usar_lanzada(v))  
            self.assertTrue(d.usar_lanzada(v))   
            self.assertTrue(d.usar_lanzada(v))   
            self.assertFalse(d.usar_lanzada(v))  

if __name__ == "__main__":
    unittest.main()
