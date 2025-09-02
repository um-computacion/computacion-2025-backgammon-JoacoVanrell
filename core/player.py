class Jugador:
    """
    Cada jugador tiene un nombre, color de fichas y maneja el estado
    de sus fichas durante el juego (en tablero, en barra, fuera del tablero).
    """
    
    def __init__(self, nombre, color):
        """
        Constructor del jugador.
        
        Args:
            nombre (str): Nombre del jugador
            color (str): Color de las fichas ('blanco' o 'negro')
        """
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fichas_totales__ = 15
        self.__fichas_en_barra__ = 0
        self.__fichas_fuera__ = 0  # fichas ya retiradas del tablero
    
    def get_nombre(self):
        """
        Obtiene el nombre del jugador.
        
        Returns:
            str: Nombre del jugador
        """
        return self.__nombre__
    
    def get_color(self):
        """
        Obtiene el color de las fichas del jugador.
        
        Returns:
            str: Color de las fichas ('blanco' o 'negro')
        """
        return self.__color__
    
    def get_fichas_totales(self):
        """
        Obtiene el número total de fichas del jugador.
        
        Returns:
            int: Cantidad total de fichas (siempre 15)
        """
        return self.__fichas_totales__
    
    def get_fichas_en_barra(self):
        """
        Obtiene el número de fichas capturadas en la barra.
        
        Returns:
            int: Cantidad de fichas en la barra
        """
        return self.__fichas_en_barra__
    
    def get_fichas_fuera(self):
        """
        Obtiene el número de fichas que salieron del tablero (bear-off).
        
        Returns:
            int: Cantidad de fichas fuera del tablero
        """
        return self.__fichas_fuera__
    
    def agregar_a_barra(self):
        """
        Agrega una ficha a la barra cuando es capturada por el oponente.
        """
        self.__fichas_en_barra__ += 1
    
    def sacar_de_barra(self):
        """
        Saca una ficha de la barra para reingresarla al juego.
        
        Solo reduce el contador si hay fichas en la barra.
        """
        if self.__fichas_en_barra__ > 0:
            self.__fichas_en_barra__ -= 1
    
    def agregar_fuera(self):
        """
        Saca una ficha del tablero (bear-off) cuando llega al final.
        """
        self.__fichas_fuera__ += 1
    
    def ha_ganado(self):
        """
        Verifica si el jugador ha ganado la partida.
        
        Un jugador gana cuando todas sus 15 fichas están fuera del tablero.
        
        Returns:
            bool: True si el jugador ganó, False en caso contrario
        """
        return self.__fichas_fuera__ == 15
    
    def __str__(self):
        """
        Representación del jugador como cadena de texto.
        
        Returns:
            str: Descripción del jugador con nombre y color
        """
        return f"Jugador: {self.__nombre__} ({self.__color__})"