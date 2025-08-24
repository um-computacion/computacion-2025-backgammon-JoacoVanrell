from typing import List
from .checker import Checker

class Jugador:

    def __init__(self, id_jugador: int, nombre: str):
        if id_jugador not in (1, 2):
            raise ValueError("id_jugador debe ser 1 o 2")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("nombre no puede ser vacío")

        self.__id_jugador__ = id_jugador
        self.__nombre__ = nombre.strip()
        self.__fichas__: List[Checker] = []


    def obtener_id(self) -> int:
        return self.__id_jugador__

    def obtener_nombre(self) -> str:
        return self.__nombre__

    def agregar_ficha(self, ficha: Checker) -> None:
        if ficha.obtener_jugador() != self.__id_jugador__:
            raise ValueError("La ficha no pertenece a este jugador")
        self.__fichas__.append(ficha)

    def remover_ficha(self) -> Checker:
        if not self.__fichas__:
            raise IndexError("El jugador no tiene fichas para remover")
        return self.__fichas__.pop()

    def contar_fichas(self) -> int:
        return len(self.__fichas__)


import unittest

class TestJugador(unittest.TestCase):

    def test_inicializacion_valida(self):
        jugador = Jugador(1, "Joaquin")
        self.assertEqual(jugador.obtener_id(), 1)
        self.assertEqual(jugador.obtener_nombre(), "Joaquin")
        self.assertEqual(jugador.contar_fichas(), 0)

    def test_inicializacion_id_invalido(self):
        with self.assertRaises(ValueError):
            Jugador(3, "Agus")

    def test_inicializacion_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Jugador(1, "")

    def test_agregar_ficha_valida(self):
        jugador = Jugador(1, "Antonio")
        ficha = Checker(1)
        jugador.agregar_ficha(ficha)
        self.assertEqual(jugador.contar_fichas(), 1)

    def test_agregar_ficha_invalida(self):
        jugador = Jugador(1, "Antonio")
        ficha = Checker(2)
        with self.assertRaises(ValueError):
            jugador.agregar_ficha(ficha)

    def test_remover_ficha(self):
        jugador = Jugador(1, "Evangelina")
        ficha = Checker(1)
        jugador.agregar_ficha(ficha)
        removed_ficha = jugador.remover_ficha()
        self.assertEqual(removed_ficha.obtener_jugador(), 1)
        self.assertEqual(jugador.contar_fichas(), 0)

    def test_remover_ficha_sin_fichas(self):
        jugador = Jugador(1, "Evangelina")
        with self.assertRaises(IndexError):
            jugador.remover_ficha()

    def test_contar_fichas(self):
        jugador = Jugador(1, "Evangelina")
        self.assertEqual(jugador.contar_fichas(), 0)
        ficha1 = Checker(1)
        ficha2 = Checker(1)
        jugador.agregar_ficha(ficha1)
        jugador.agregar_ficha(ficha2)
        self.assertEqual(jugador.contar_fichas(), 2)