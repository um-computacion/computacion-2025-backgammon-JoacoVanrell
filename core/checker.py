class Checker:
    def __init__(self, id_jugador: int):
        self.__id_jugador__ = id_jugador

    def obtener_jugador(self) -> int:
        return self.__id_jugador__
    
import unittest    

class TestChecker(unittest.TestCase):
    def test_guarda_id_jugador_1(self):
        checker = Checker(1)
        self.assertEqual(checker.obtener_jugador(), 1)

    def test_guarda_id_jugador_2(self):
        checker = Checker(2)
        self.assertEqual(checker.obtener_jugador(), 2)

    def test_tipo_retorno_entero(self):
        checker = Checker(1)
        self.assertIsInstance(checker.obtener_jugador(), int)

    def test_instancias_independientes(self):
        a = Checker(1)
        b = Checker(2)
        self.assertEqual(a.obtener_jugador(), 1)
        self.assertEqual(b.obtener_jugador(), 2)


if __name__ == "__main__":
    unittest.main()
