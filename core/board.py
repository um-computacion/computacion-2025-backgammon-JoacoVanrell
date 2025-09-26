from .checker import Ficha
from typing import List, Optional

class Board:
    CASA_BLANCA = range(1, 7)
    CASA_NEGRA = range(19, 25)

    def __init__(self) -> None:
        """Inicializa tablero con la configuración inicial de Backgammon."""
        # Índice 0 sin uso; puntos 1–24
        self._puntos: List[List[Ficha]] = [[] for _ in range(25)]
        self._configurar_posicion_inicial()

    def _configurar_posicion_inicial(self) -> None:
        """Coloca las 15 fichas de cada color en sus puntos iniciales."""
        # Blancas
        self._puntos[24] = [Ficha("blanco") for _ in range(2)]
        self._puntos[13] = [Ficha("blanco") for _ in range(5)]
        self._puntos[8]  = [Ficha("blanco") for _ in range(3)]
        self._puntos[6]  = [Ficha("blanco") for _ in range(5)]
        # Negras
        self._puntos[1]  = [Ficha("negro") for _ in range(2)]
        self._puntos[12] = [Ficha("negro") for _ in range(5)]
        self._puntos[17] = [Ficha("negro") for _ in range(3)]
        self._puntos[19] = [Ficha("negro") for _ in range(5)]
        # Ajustar posición interna de cada ficha
        for punto in range(1, 25):
            for f in self._puntos[punto]:
                f.set_posicion(punto)

    def get_punto(self, numero_punto: int) -> List[Ficha]:
        """
        Devuelve una copia de la lista de fichas en un punto.
        Lanza ValueError si el punto está fuera de 1–24.
        """
        if not 1 <= numero_punto <= 24:
            raise ValueError("El número de punto debe estar entre 1 y 24")
        return list(self._puntos[numero_punto])

    def get_cantidad_fichas(self, numero_punto: int) -> int:
        """Devuelve la cantidad de fichas en un punto (0 si fuera de rango)."""
        if not 1 <= numero_punto <= 24:
            return 0
        return len(self._puntos[numero_punto])

    def get_color_fichas(self, numero_punto: int) -> Optional[str]:
        """
        Devuelve el color de las fichas en un punto (asume todas del mismo color).
        Retorna None si está vacío o fuera de rango.
        """
        if not 1 <= numero_punto <= 24:
            return None
        fichas = self._puntos[numero_punto]
        return fichas[0].get_color() if fichas else None

    def puede_mover_a(self, punto_destino: int, color_jugador: str) -> bool:
        """
        Indica si un jugador puede mover a ese punto:
        - Vacío → True
        - Fichas propias → True
        - 1 ficha rival → True
        - Más de 1 ficha rival → False
        """
        if not 1 <= punto_destino <= 24:
            return False
        count = self.get_cantidad_fichas(punto_destino)
        color_dest = self.get_color_fichas(punto_destino)
        if count == 0 or color_dest == color_jugador:
            return True
        return count == 1 and color_dest != color_jugador

    def sacar_ficha(self, punto_origen: int) -> Ficha:
        """
        Saca y devuelve la última ficha de un punto.
        Lanza ValueError si el punto está vacío o fuera de rango.
        """
        if not 1 <= punto_origen <= 24:
            raise ValueError("El número de punto debe estar entre 1 y 24")
        if not self._puntos[punto_origen]:
            raise ValueError(f"No hay fichas en el punto {punto_origen}")
        return self._puntos[punto_origen].pop()

    def mover_ficha(self,
                   punto_origen: int,
                   punto_destino: int,
                   color_jugador: str) -> Optional[Ficha]:
        """
        Mueve una ficha propia:
        - Valida origen/destino
        - Captura rival si hay 1 en destino
        Devuelve la ficha capturada o None.
        """
        # Validaciones básicas
        if not (1 <= punto_origen <= 24 and 1 <= punto_destino <= 24):
            raise ValueError("Los puntos deben estar entre 1 y 24")
        if self.get_cantidad_fichas(punto_origen) == 0:
            raise ValueError(f"No hay fichas en el punto {punto_origen}")
        if self.get_color_fichas(punto_origen) != color_jugador:
            raise ValueError(f"No hay fichas {color_jugador} en el punto {punto_origen}")
        if not self.puede_mover_a(punto_destino, color_jugador):
            raise ValueError(f"El punto {punto_destino} está bloqueado")

        # Sacar ficha del origen
        ficha = self.sacar_ficha(punto_origen)

        # Captura de rival
        captura = None
        if (self.get_cantidad_fichas(punto_destino) == 1 and
            self.get_color_fichas(punto_destino) != color_jugador):
            captura = self.sacar_ficha(punto_destino)
            captura.mover_a_barra()

        # Colocar ficha en destino
        ficha.set_posicion(punto_destino)
        self._puntos[punto_destino].append(ficha)
        return captura

    def get_fichas_en_casa(self, color_jugador: str) -> int:
        """
        Cuenta fichas propias en la zona de bear-off (casa).
        Usa rangos CASA_BLANCA y CASA_NEGRA.
        """
        rango = (self.CASA_BLANCA
                 if color_jugador == "blanco"
                 else self.CASA_NEGRA)
        total = 0
        for p in rango:
            if self.get_color_fichas(p) == color_jugador:
                total += self.get_cantidad_fichas(p)
        return total

    def puede_bear_off(self, color_jugador: str) -> bool:
        """
        Indica si el jugador puede empezar el bear-off:
        todas las fichas propias deben estar en casa.
        """
        total_color = sum(
            self.get_cantidad_fichas(p)
            for p in range(1, 25)
            if self.get_color_fichas(p) == color_jugador
        )
        if total_color == 0:
            return False
        return self.get_fichas_en_casa(color_jugador) == total_color

    def mostrar_tablero(self) -> str:
        """
        Retorna una representación en texto del tablero completo.
        """
        tablero_str = "\nTablero de Backgammon:\n" + "=" * 50 + "\n"
        # Lado superior 13–24
        tablero_str += "13 14 15 16 17 18   19 20 21 22 23 24\n"
        for fila in range(5):
            linea = ""
            for punto in range(13, 25):
                cnt = self.get_cantidad_fichas(punto)
                if cnt > fila:
                    simbolo = ("B"
                               if self.get_color_fichas(punto) == "blanco"
                               else "N")
                    linea += f" {simbolo} "
                else:
                    linea += "   "
                if punto == 18:
                    linea += " | "
            tablero_str += linea + "\n"
        tablero_str += "-" * 50 + "\n"
        # Lado inferior 12–1
        for fila in range(4, -1, -1):
            linea = ""
            for punto in range(12, 0, -1):
                cnt = self.get_cantidad_fichas(punto)
                if cnt > fila:
                    simbolo = ("B"
                               if self.get_color_fichas(punto) == "blanco"
                               else "N")
                    linea += f" {simbolo} "
                else:
                    linea += "   "
                if punto == 7:
                    linea += " | "
            tablero_str += linea + "\n"
        tablero_str += "12 11 10  9  8  7    6  5  4  3  2  1\n"
        tablero_str += "=" * 50

        return tablero_str

