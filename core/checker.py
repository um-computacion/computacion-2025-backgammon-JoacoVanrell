from typing import Optional

class Ficha:
    def __init__(self, color: str) -> None:
        self._color: str = color
        self._posicion:Optional[int] = None 
        self._en_barra: bool = False
        self._fuera_tablero: bool = False
    
    def get_color(self) -> str:
        return self._color
    
    def get_posicion(self) -> Optional[int]:
        return self._posicion
    
    def set_posicion(self, nueva_posicion: int) -> None:
        """
        Coloca la ficha en un punto del tablero. No va a validar
        reglas del juego; solo seteo el estado
        """
        self._posicion = nueva_posicion
        self._en_barra = False
        self._fuera_tablero = False
    
    def esta_en_barra(self) -> None:
        return self._en_barra
    
    def mover_a_barra(self) -> None:
        self._posicion = None
        self._en_barra = True
        self._fuera_tablero = False
    
    def esta_fuera_tablero(self) -> bool:
        return self._fuera_tablero
    
    def mover_fuera_tablero(self) -> None:
        self._posicion = None
        self._en_barra = False
        self._fuera_tablero = True
    
    def esta_en_tablero(self) -> bool:
        return self._posicion is not None and not self._en_barra and not self._fuera_tablero
    
    def __str__(self) -> str:
        if self._fuera_tablero:
            return f"Ficha {self._color} (fuera del tablero)"
        elif self._en_barra:
            return f"Ficha {self._color} (en barra)"
        elif self._posicion is not None:
            return f"Ficha {self._color} (posición {self._posicion})"
        else:
            return f"Ficha {self._color} (sin posición)"
    
    def __eq__(self, otra_ficha: object) -> bool:
        if not isinstance(otra_ficha, Ficha):
            return False
        
        return (self._color == otra_ficha._color and
                self._posicion == otra_ficha._posicion and
                self._en_barra == otra_ficha._en_barra and
                self._fuera_tablero == otra_ficha._fuera_tablero)