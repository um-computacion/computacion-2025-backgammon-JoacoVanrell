class Ficha:
    """
    Cada ficha tiene un color (pertenece a un jugador) y una posición
    en el tablero. Puede estar en el tablero, en la barra o fuera del tablero.
    """
    
    def __init__(self, color):
        """
        Constructor de la ficha.
        
        Args:
            color (str): Color de la ficha ('blanco' o 'negro')
        """
        self.__color__ = color
        self.__posicion__ = None  # None significa que no está en el tablero aún
        self.__en_barra__ = False
        self.__fuera_tablero__ = False
    
    def get_color(self):
        """
        Obtiene el color de la ficha.
        
        Returns:
            str: Color de la ficha ('blanco' o 'negro')
        """
        return self.__color__
    
    def get_posicion(self):
        """
        Obtiene la posición actual de la ficha en el tablero.
        
        Returns:
            int or None: Número del punto (1-24) donde está la ficha,
                        None si no está en el tablero
        """
        return self.__posicion__
    
    def set_posicion(self, nueva_posicion):
        """
        Establece la posición de la ficha en el tablero.
        
        Args:
            nueva_posicion (int): Número del punto donde colocar la ficha (1-24)
        """
        self.__posicion__ = nueva_posicion
        self.__en_barra__ = False
        self.__fuera_tablero__ = False
    
    def esta_en_barra(self):
        """
        Verifica si la ficha está en la barra.
        
        Returns:
            bool: True si la ficha está en la barra
        """
        return self.__en_barra__
    
    def mover_a_barra(self):
        """
        Mueve la ficha a la barra cuando es capturada.
        """
        self.__posicion__ = None
        self.__en_barra__ = True
        self.__fuera_tablero__ = False
    
    def esta_fuera_tablero(self):
        """
        Verifica si la ficha ya salió del tablero (bear-off).
        
        Returns:
            bool: True si la ficha está fuera del tablero
        """
        return self.__fuera_tablero__
    
    def mover_fuera_tablero(self):
        """
        Saca la ficha del tablero (bear-off).
        """
        self.__posicion__ = None
        self.__en_barra__ = False
        self.__fuera_tablero__ = True
    
    def esta_en_tablero(self):
        """
        Verifica si la ficha está actualmente en el tablero.
        
        Returns:
            bool: True si la ficha tiene una posición válida en el tablero
        """
        return self.__posicion__ is not None and not self.__en_barra__ and not self.__fuera_tablero__
    
    def __str__(self):
        """
        Representación de la ficha como cadena de texto.
        
        Returns:
            str: Descripción del estado actual de la ficha
        """
        if self.__fuera_tablero__:
            return f"Ficha {self.__color__} (fuera del tablero)"
        elif self.__en_barra__:
            return f"Ficha {self.__color__} (en barra)"
        elif self.__posicion__ is not None:
            return f"Ficha {self.__color__} (posición {self.__posicion__})"
        else:
            return f"Ficha {self.__color__} (sin posición)"
    
    def __eq__(self, otra_ficha):
        """
        Compara si dos fichas son iguales.
        
        Args:
            otra_ficha (Ficha): Otra ficha para comparar
            
        Returns:
            bool: True si tienen el mismo color y están en el mismo estado
        """
        if not isinstance(otra_ficha, Ficha):
            return False
        
        return (self.__color__ == otra_ficha.__color__ and
                self.__posicion__ == otra_ficha.__posicion__ and
                self.__en_barra__ == otra_ficha.__en_barra__ and
                self.__fuera_tablero__ == otra_ficha.__fuera_tablero__)