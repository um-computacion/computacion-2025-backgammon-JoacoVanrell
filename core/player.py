class Jugador:
    """
    Cada jugador tiene nombre, color de fichas y maneja sus fichas básicas.
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
        self.__fichas_totales__ = 15  # Cada jugador tiene 15 fichas
    
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
            str: Color de las fichas
        """
        return self.__color__
    
    def get_fichas_totales(self):
        """
        Obtiene la cantidad total de fichas del jugador.
        
        Returns:
            int: Número total de fichas (siempre 15)
        """
        return self.__fichas_totales__
    
    def __str__(self):
        """
        Representación del jugador como texto.
        
        Returns:
            str: Descripción del jugador
        """
        return f"Jugador: {self.__nombre__} (Fichas {self.__color__})"