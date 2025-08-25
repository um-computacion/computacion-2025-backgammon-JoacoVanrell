from typing import List, Dict
from .checker import Ficha
import unittest


class Tablero:
    def __init__(self) -> None:
        self.__puntos__: List[List[Ficha]] = [[] for _ in range(24)]
        self.__barra__: Dict[int, List[Ficha]] = {1: [], 2: []}
        self.__fuera__: Dict[int, List[Ficha]] = {1: [], 2: []}

    def _forzar_en_barra(self, id_jugador: int, ficha: Ficha) -> None:
        if id_jugador not in (1, 2):
            raise ValueError("id_jugador debe ser 1 o 2")
        self.__barra__[id_jugador].append(ficha)

    def contar_puntos(self) -> int:
        return len(self.__puntos__)

    def obtener_punto(self, indice: int) -> List[Ficha]:
        if not 0 <= indice < 24:
            raise IndexError("índice de punto fuera de rango [0..23]")
        return self.__puntos__[indice]

    def obtener_barra(self, id_jugador: int) -> List[Ficha]:
        if id_jugador not in (1, 2):
            raise ValueError("id_jugador debe ser 1 o 2")
        return self.__barra__[id_jugador]

    def obtener_fuera(self, id_jugador: int) -> List[Ficha]:
        if id_jugador not in (1, 2):
            raise ValueError("id_jugador debe ser 1 o 2")
        return self.__fuera__[id_jugador]

    def colocar_ficha(self, indice: int, ficha: Ficha) -> None:
        if not 0 <= indice < 24:
            raise IndexError("índice de punto fuera de rango [0..23]")
        self.__puntos__[indice].append(ficha)

    def quitar_de_punto(self, indice: int) -> Ficha:
        punto = self.obtener_punto(indice)
        if not punto:
            raise IndexError("no hay fichas en el punto")
        return punto.pop()

    def contar_en_punto(self, indice: int) -> int:
        return len(self.obtener_punto(indice))

    def cima_duenio(self, indice: int) -> int | None:
        punto = self.obtener_punto(indice)
        return punto[-1].obtener_jugador() if punto else None

    def puede_colocar_en(self, indice: int, id_jugador: int) -> bool:
        punto = self.obtener_punto(indice)
        if not punto:
            return True
        duenio = punto[-1].obtener_jugador()
        if duenio == id_jugador:
            return True
        return len(punto) == 1

    def inicializar_tablero_estandar(self) -> None:
        self.__puntos__ = [[] for _ in range(24)]
        self.__barra__ = {1: [], 2: []}
        self.__fuera__ = {1: [], 2: []}

        for _ in range(2):
            self.colocar_ficha(23, Ficha(1))
        for _ in range(5):
            self.colocar_ficha(12, Ficha(1))
        for _ in range(3):
            self.colocar_ficha(7, Ficha(1))
        for _ in range(5):
            self.colocar_ficha(5, Ficha(1))

        for _ in range(2):
            self.colocar_ficha(0, Ficha(2))
        for _ in range(5):
            self.colocar_ficha(11, Ficha(2))
        for _ in range(3):
            self.colocar_ficha(16, Ficha(2))
        for _ in range(5):
            self.colocar_ficha(18, Ficha(2))

    # --- Movimientos ---
    def mover_simple(self, origen: int, destino: int, id_jugador: int) -> None:
        ficha = self.quitar_de_punto(origen)
        if ficha.obtener_jugador() != id_jugador:
            self.__puntos__[origen].append(ficha)
            raise ValueError("la ficha superior no pertenece al jugador")

        punto_dest = self.obtener_punto(destino)
        if punto_dest and punto_dest[-1].obtener_jugador() != id_jugador and len(punto_dest) == 1:
            rival = punto_dest.pop()
            self.__barra__[rival.obtener_jugador()].append(rival)

        if not self.puede_colocar_en(destino, id_jugador):
            self.__puntos__[origen].append(ficha)
            raise ValueError("movimiento no permitido por ocupación del destino")

        punto_dest.append(ficha)

    def hay_en_barra(self, id_jugador: int) -> bool:
        if id_jugador not in (1, 2):
            raise ValueError("id_jugador debe ser 1 o 2")
        return len(self.__barra__[id_jugador]) > 0

    def reingresar_desde_barra(self, destino: int, id_jugador: int) -> None:
        if id_jugador not in (1, 2):
            raise ValueError("id_jugador debe ser 1 o 2")
        if not self.hay_en_barra(id_jugador):
            raise IndexError("no hay fichas en barra para reingresar")
        if not self.puede_colocar_en(destino, id_jugador):
            raise ValueError("no se puede reingresar en un punto bloqueado")

        ficha = self.__barra__[id_jugador].pop()
        dest = self.obtener_punto(destino)
        if dest and dest[-1].obtener_jugador() != id_jugador and len(dest) == 1:
            rival = dest.pop()
            self.__barra__[rival.obtener_jugador()].append(rival)

        dest.append(ficha)


class TestTablero(unittest.TestCase):
    def test_tiene_24_puntos(self):
        self.assertEqual(Tablero().contar_puntos(), 24)

    def test_inicializacion_estandar(self):
        t = Tablero()
        t.inicializar_tablero_estandar()
        total = sum(len(t.obtener_punto(i)) for i in range(24))
        self.assertEqual(total, 30)
        self.assertEqual(len(t.obtener_punto(23)), 2)
        self.assertEqual(len(t.obtener_punto(12)), 5)
        self.assertEqual(len(t.obtener_punto(7)), 3)
        self.assertEqual(len(t.obtener_punto(5)), 5)
        self.assertEqual(len(t.obtener_punto(0)), 2)
        self.assertEqual(len(t.obtener_punto(11)), 5)
        self.assertEqual(len(t.obtener_punto(16)), 3)
        self.assertEqual(len(t.obtener_punto(18)), 5)


class TestTableroBasico(unittest.TestCase):
    def test_colocar_y_quitar_ficha(self):
        t = Tablero(); f = Ficha(1)
        t.colocar_ficha(0, f)
        self.assertEqual(t.contar_en_punto(0), 1)
        sacada = t.quitar_de_punto(0)
        self.assertIs(sacada, f)

    def test_cima_duenio(self):
        t = Tablero(); f = Ficha(2)
        t.colocar_ficha(5, f)
        self.assertEqual(t.cima_duenio(5), 2)
        self.assertIsNone(t.cima_duenio(6))

    def test_puede_colocar_en(self):
        t = Tablero()
        self.assertTrue(t.puede_colocar_en(0, 1))
        t.colocar_ficha(0, Ficha(1))
        self.assertTrue(t.puede_colocar_en(0, 1))
        self.assertTrue(t.puede_colocar_en(0, 2))
        t.colocar_ficha(0, Ficha(2))
        self.assertFalse(t.puede_colocar_en(0, 1))


class TestTableroMovimientos(unittest.TestCase):
    def test_mover_simple_y_captura(self):
        t = Tablero()
        t.colocar_ficha(0, Ficha(1))
        t.colocar_ficha(1, Ficha(2))  # blot
        t.mover_simple(0, 1, 1)
        self.assertEqual(t.cima_duenio(1), 1)
        self.assertEqual(len(t.obtener_barra(2)), 1)

    def test_mover_simple_invalido_destino_bloqueado(self):
        t = Tablero()
        t.colocar_ficha(0, Ficha(1))
        t.colocar_ficha(1, Ficha(2)); t.colocar_ficha(1, Ficha(2))
        with self.assertRaises(ValueError):
            t.mover_simple(0, 1, 1)

    def test_mover_simple_ficha_ajena(self):
        t = Tablero()
        t.colocar_ficha(0, Ficha(2))
        with self.assertRaises(ValueError):
            t.mover_simple(0, 1, 1)


class TestTableroErrores(unittest.TestCase):
    def test_quitar_de_punto_vacio(self):
        t = Tablero()
        with self.assertRaises(IndexError):
            t.quitar_de_punto(0)

    def test_mover_origen_destino_fuera_rango(self):
        t = Tablero(); f = Ficha(1)
        t.colocar_ficha(0, f)
        with self.assertRaises(IndexError):
            t.mover_simple(0, 24, 1)
        with self.assertRaises(IndexError):
            t.mover_simple(24, 0, 1)

    def test_obtener_barra_y_fuera_id_invalido(self):
        t = Tablero()
        with self.assertRaises(ValueError):
            t.obtener_barra(3)
        with self.assertRaises(ValueError):
            t.obtener_fuera(0)


class TestTableroBarra(unittest.TestCase):
    def test_hay_en_barra_y_reingreso(self):
        t = Tablero()
        t.colocar_ficha(0, Ficha(1))
        t.colocar_ficha(1, Ficha(2))
        t.mover_simple(0, 1, 1)
        self.assertTrue(t.hay_en_barra(2))
        t.reingresar_desde_barra(5, 2)
        self.assertFalse(t.hay_en_barra(2))
        self.assertEqual(t.cima_duenio(5), 2)

    def test_reingreso_sin_barra(self):
        t = Tablero()
        with self.assertRaises(IndexError):
            t.reingresar_desde_barra(0, 1)

    def test_reingreso_en_bloqueado(self):
        t = Tablero()
        t._forzar_en_barra(1, Ficha(1))
        t.colocar_ficha(5, Ficha(2))
        t.colocar_ficha(5, Ficha(2))
        with self.assertRaises(ValueError):
            t.reingresar_desde_barra(5, 1)


if __name__ == "__main__":
    unittest.main()

