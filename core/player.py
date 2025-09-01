class Jugador:
    """gi
    Representa a un jugador de Backgammon.
    """
    
    def __init__(self, nombre, color):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fichas_totales__ = 15
        self.__fichas_en_barra__ = 0
        self.__fichas_fuera__ = 0  # fichas ya retiradas del tablero
    
    def get_nombre(self):
        return self.__nombre__
    
    def get_color(self):
        return self.__color__
    
    def get_fichas_totales(self):
        return self.__fichas_totales__
    
    def get_fichas_en_barra(self):
        return self.__fichas_en_barra__
    
    def get_fichas_fuera(self):
        return self.__fichas_fuera__
    
    def agregar_a_barra(self):
        self.__fichas_en_barra__ += 1
    
    def sacar_de_barra(self):
        if self.__fichas_en_barra__ > 0:
            self.__fichas_en_barra__ -= 1
    
    def agregar_fuera(self):
        self.__fichas_fuera__ += 1
    
    def __str__(self):
        return f"Jugador: {self.__nombre__} ({self.__color__})"