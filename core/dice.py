import random
from typing import List, Tuple

class Dado:
    def __init__(self):
        self._dado1 = 0
        self._dado2 = 0
        self._proximas_tiradas: List[Tuple[int, int]] = []
    
    def set_proximas_tiradas(self, tiradas: List[Tuple[int, int]]) -> None:
        self._proximas_tiradas = list(tiradas)

    def lanzar(self) -> Tuple[int, int]:
        if self._proximas_tiradas:
            self._dado1, self._dado2 = self._proximas_tiradas.pop(0)
        else:
            self._dado1 = random.randint(1, 6)
            self._dado2 = random.randint(1, 6)

        return (self._dado1, self._dado2)

    
    def get_valores(self) -> Tuple [int, int]:
        return (self._dado1, self._dado2)


    def es_doble(self) -> bool:
        return self._dado1 != 0 and self._dado1 == self._dado2
    
    def lanzar_dados(self) -> Tuple[int, int]:
        return self.lanzar()

    def get_proximas_tiradas(self) -> List[Tuple[int, int]]:
        return list(self._proximas_tiradas)