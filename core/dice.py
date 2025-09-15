import random
from typing import List, Tuple

class Dado:
    def __init__(self) -> None:
        """
        Controla tiradas de dados.
        _proximas_tiradas solo se usa para tests.
        """
        self._dado1 = 0
        self._dado2 = 0
        self._proximas_tiradas: List[Tuple[int, int]] = []

    def set_proximas_tiradas(self, tiradas: List[Tuple[int, int]]) -> None:
        """Define una lista de pares (dado1, dado2) para uso en tests."""
        self._proximas_tiradas = list(tiradas)

    def lanzar(self) -> Tuple[int, int]:
        """
        Realiza una tirada.
        Si hay prox. tiradas predefinidas, las consume en orden.
        """
        if self._proximas_tiradas:
            self._dado1, self._dado2 = self._proximas_tiradas.pop(0)
        else:
            self._dado1 = random.randint(1, 6)
            self._dado2 = random.randint(1, 6)
        return (self._dado1, self._dado2)

    def get_valores(self) -> Tuple[int, int]:
        """Devuelve el último par de valores lanzados."""
        return (self._dado1, self._dado2)

    def es_doble(self) -> bool:
        """Indica si la última tirada fue un doble."""
        return self._dado1 != 0 and self._dado1 == self._dado2

    lanzar_dados = lanzar