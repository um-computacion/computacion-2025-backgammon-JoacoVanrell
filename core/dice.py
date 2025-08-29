import random

class Dado:
    """
    Maneja la lógica de tirar dos dados y determinar
    si hay valores dobles.
    """
    
    def __init__(self):
        """
        Constructor de los dados.
        
        Los dados comienzan sin valores hasta que se lance.
        """
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__proximas_tiradas__ = []
    
    def lanzar_dados(self):
        """
        Lanza los dos dados y guarda los valores.
        
        Returns:
            list: Lista con los valores de los dados. Si hay doble,
                 devuelve 4 valores (ej: [3, 3, 3, 3])
        """
        self.__dado1__ = random.randint(1, 6)
        self.__dado2__ = random.randint(1, 6)

        # Si el valor de los dados se repite, se pueden usar 4 movimientos
        if self.__dado1__ == self.__dado2__:
            self.__proximas_tiradas__ = [self.__dado1__] * 4
        else:
            self.__proximas_tiradas__ = [self.__dado1__, self.__dado2__]  #guarda los valores distintos

        return self.__proximas_tiradas__.copy()

    def get_proximas_tiradas(self):
        """
        Obtiene la última tirada realizada.
        
        Returns:
            list: Lista con los valores de la última tirada
        """
        return self.__proximas_tiradas__.copy()
    
    def usar_lanzada(self, value):
        """
        Usa un movimiento disponible de la tirada actual.
        
        Args:
            value (int): Valor del dado a usar (1-6)
            
        Returns:
            bool: True si se pudo usar el movimiento, False si no estaba disponible
        """
        if value in self.__proximas_tiradas__:
            self.__proximas_tiradas__.remove(value)
            return True
        return False
    
    def get_resultado_dados(self):
        """
        Obtiene los valores individuales de cada dado.
        
        Returns:
            tuple: Tupla con (dado1, dado2)
        """
        return (self.__dado1__, self.__dado2__)


    def es_doble(self):
        """
        Verifica si la última tirada fue doble.
        
        Returns:
            bool: True si ambos dados tienen el mismo valor
        """
        return self.__dado1__ != 0 and self.__dado1__ == self.__dado2__