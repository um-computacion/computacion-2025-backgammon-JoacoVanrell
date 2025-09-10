class Jugador:

    TOTAL_FICHAS: int = 15

    def __init__(self, color: str) -> None:
        self._color: str = color
        self._en_barra: int = 0
        self._fuera: int = 0

    def get_color(self) -> str:
        return self._color
    
    def agregar_a_barra(self) -> None:
        self._en_barra += 1

    def quitar_de_barra(self) -> None:
        if self._en_barra > 0:
            self._en_barra -= 1
    
    def agregar_fuera(self) -> None:
        #cuando ficha sale del tablero
        if self._fuera < self.TOTAL_FICHAS:
            self._fuera += 1
        
    def en_barra(self) -> int:
        return self._en_barra
    
    def fuera(self) -> int:
        return self._fuera
    
    def ha_ganado(self) -> bool:
        return self._fuera == self.TOTAL_FICHAS
    
