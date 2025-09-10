from .checker import Ficha
from typing import List, Optional

class Board:
    def __init__(self):
        #indice 0 sin uso
        self._puntos: List[List[Ficha]] = [[] for _ in range(25)] 
        self._configurar_posicion_inicial()
    
    def _configurar_posicion_inicial(self) -> None:
        #Blancas
        self._puntos[24] = [Ficha('blanco') for _ in range(2)]
        self._puntos[13] = [Ficha('blanco') for _ in range(5)]
        self._puntos[8] = [Ficha('blanco') for _ in range(3)]
        self._puntos[6] = [Ficha('blanco') for _ in range(5)]
        #Negras
        self._puntos[1] = [Ficha('negro') for _ in range(2)]
        self._puntos[12] = [Ficha('negro') for _ in range(5)]
        self._puntos[17] = [Ficha('negro') for _ in range(3)]
        self._puntos[19] = [Ficha('negro') for _ in range(5)]
        #seteo posicion en cada ficha
        for punto in range(1, 25):
            for f in self._puntos[punto]:
                f.set_posicion(punto)

    
    def get_punto(self, numero_punto: int) -> List[Ficha]:
        if not 1 <= numero_punto <= 24:
            raise ValueError("El número de punto debe estar entre 1 y 24")
        
        return list(self._puntos[numero_punto])
    
    def get_cantidad_fichas(self, numero_punto: int) -> int:
        if not 1 <= numero_punto <= 24:
            return 0
        
        return len(self._puntos[numero_punto])
    
    def get_color_fichas(self, numero_punto: int) -> Optional[str]:
        if not 1 <= numero_punto <= 24:
            return None
            
        fichas = self._puntos[numero_punto]
        if not fichas:
            return None
        
        return fichas[0].get_color()
    
    def puede_mover_a(self, punto_destino: int, color_jugador: str) -> bool:

        if not 1 <= punto_destino <= 24:
            return False
        
        cantidad_fichas = self.get_cantidad_fichas(punto_destino)
        if cantidad_fichas == 0:
            return True
        
        color_destino = self.get_color_fichas(punto_destino)
        if color_destino == color_jugador:
            return True
        
        if cantidad_fichas == 1 and color_destino != color_jugador:
            return True
        
        return False
    
    def mover_ficha(self, punto_origen: int, punto_destino: int, color_jugador: str) -> Optional[Ficha]:
        """
        Mueve una ficha del color. Si habia 1 del rival en destino, la captura. Devuelve la ficha o None.
        """
        if not (1 <= punto_origen <= 24 and 1 <= punto_destino <= 24):
            raise ValueError("Los puntos deben estar entre 1 y 24")
        
        if self.get_cantidad_fichas(punto_origen) == 0:
            raise ValueError(f"No hay fichas en el punto {punto_origen}")
        
        if self.get_color_fichas(punto_origen) != color_jugador:
            raise ValueError(f"No hay fichas {color_jugador} en el punto {punto_origen}")
        
        if not self.puede_mover_a(punto_destino, color_jugador):
            raise ValueError(f"El punto {punto_destino} está bloqueado")
        
        #saco la ultima
        ficha= self._puntos[punto_origen].pop()
        ficha.set_posicion(punto_destino)
        
        ficha_capturada: Optional[Ficha] = None
        if (self.get_cantidad_fichas(punto_destino) == 1 and 
            self.get_color_fichas(punto_destino) != color_jugador):
            ficha_capturada = self._puntos[punto_destino].pop()
            ficha_capturada.mover_a_barra()
        
        self._puntos[punto_destino].append(ficha)
        
        return ficha_capturada
    
    def es_movimiento_valido(self, punto_origen: int, punto_destino: int, color_jugador: str) -> bool:
        if not (1 <= punto_origen <= 24 and 1 <= punto_destino <= 24):
            return False
        if self.get_cantidad_fichas(punto_origen) == 0:
            return False
        if self.get_color_fichas(punto_origen) != color_jugador:
            return False
        
        return self.puede_mover_a(punto_destino, color_jugador)
    
    def get_fichas_en_casa(self, color_jugador: str) -> str:
        if color_jugador == 'blanco':
            puntos_casa = range(1, 7)
        else:
            puntos_casa = range(19, 25)
        
        total = 0
        for punto in puntos_casa:
            if self.get_color_fichas(punto) == color_jugador:
                total += self.get_cantidad_fichas(punto)
        
        return total
    
    def puede_bear_off(self, color_jugador: str) -> bool:
        fichas_en_casa = self.get_fichas_en_casa(color_jugador)

        total_color = 0
        for p in range(1, 25):
            if self.get_color_fichas(p) == color_jugador:
                total_color += self.get_cantidad_fichas(p)

        # Debe tener al menos 1 ficha propia en el tablero (mejor aún: 15)
        if total_color == 0:
            return False

        return fichas_en_casa == total_color
    # Si querés exigir todas las 15:
    # return total_color == 15 and fichas_en_casa == 15
    
    def mostrar_tablero(self) -> str:
        tablero_str = "\nTablero de Backgammon:\n"
        tablero_str += "=" * 50 + "\n"
        
        tablero_str += "13 14 15 16 17 18   19 20 21 22 23 24\n"
        for fila in range(5): 
            linea = ""
            for punto in range(13, 25):
                fichas = self.get_cantidad_fichas(punto)
                if fichas > fila:
                    color = self.get_color_fichas(punto)
                    simbolo = "B" if color == 'blanco' else "N"
                    linea += f" {simbolo} "
                else:
                    linea += "   "
                
                if punto == 18: 
                    linea += " | "
            tablero_str += linea + "\n"
        
        tablero_str += "-" * 50 + "\n"
        
        for fila in range(4, -1, -1):
            linea = ""
            for punto in range(12, 0, -1):
                fichas = self.get_cantidad_fichas(punto)
                if fichas > fila:
                    color = self.get_color_fichas(punto)
                    simbolo = "B" if color == 'blanco' else "N"
                    linea += f" {simbolo} "
                else:
                    linea += "   "
                
                if punto == 7:
                    linea += " | "
            tablero_str += linea + "\n"
        
        tablero_str += "12 11 10  9  8  7    6  5  4  3  2  1\n"
        tablero_str += "=" * 50
        
        return tablero_str