from typing import Optional

class Ficha:
    def __init__(self, color: str) -> None:
        """
        Representa una ficha con un color y su estado (barra, tablero, fuera).
        """
        self._color = color
        self._posicion: Optional[int] = None
        self._en_barra = False
        self._fuera_tablero = False

    def get_color(self) -> str:
        """Devuelve el color de la ficha."""
        return self._color

    def get_posicion(self) -> Optional[int]:
        """Devuelve el punto del tablero donde está, o None."""
        return self._posicion

    def set_posicion(self, nueva_posicion: int) -> None:
        """
        Coloca la ficha en un punto del tablero.
        No valida reglas de juego; solo actualiza estado.
        """
        self._posicion = nueva_posicion
        self._en_barra = False
        self._fuera_tablero = False

    def esta_en_barra(self) -> bool:
        """Indica si la ficha está en la barra."""
        return self._en_barra

    def mover_a_barra(self) -> None:
        """Mueve la ficha a la barra."""
        self._posicion = None
        self._en_barra = True
        self._fuera_tablero = False

    def esta_fuera_tablero(self) -> bool:
        """Indica si la ficha está fuera del tablero."""
        return self._fuera_tablero

    def mover_fuera_tablero(self) -> None:
        """Mueve la ficha fuera del tablero."""
        self._posicion = None
        self._en_barra = False
        self._fuera_tablero = True

    def esta_en_tablero(self) -> bool:
        """Indica si la ficha está en un punto válido del tablero."""
        return (self._posicion is not None
                and not self._en_barra
                and not self._fuera_tablero)

    def __str__(self) -> str:
        """Cadena legible según el estado de la ficha."""
        if self._fuera_tablero:
            estado = "fuera del tablero"
        elif self._en_barra:
            estado = "en barra"
        elif self._posicion is not None:
            estado = f"posición {self._posicion}"
        else:
            estado = "sin posición"
        return f"Ficha {self._color} ({estado})"

    def __eq__(self, otra: object) -> bool:
        """Compara ficha por color y estado interno."""
        if not isinstance(otra, Ficha):
            return False
        return (self._color == otra._color
                and self._posicion == otra._posicion
                and self._en_barra == otra._en_barra

                and self._fuera_tablero == otra._fuera_tablero)

