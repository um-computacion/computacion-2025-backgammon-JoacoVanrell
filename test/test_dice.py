import unittest
from core.dice import Dado

class TestDado(unittest.TestCase):

    def test_setear_y_lanzar_predefinido(self):
        d = Dado()
        d.set_proximas_tiradas([(3,3), (1,4)])
        # primer lanzamiento
        self.assertEqual(d.lanzar(), (3,3))
        self.assertTrue(d.es_doble())
        self.assertEqual(d.get_valores(), (3,3))
        # segundo lanzamiento
        self.assertEqual(d.lanzar(), (1,4))
        self.assertFalse(d.es_doble())
        self.assertEqual(d.get_valores(), (1,4))

    def test_lanzar_valores_random(self):
        d = Dado()
        valores = d.lanzar()
        self.assertIn(valores[0], range(1,7))
        self.assertIn(valores[1], range(1,7))

if __name__ == "__main__":
    unittest.main()
