from typing import List, Optional, Tuple
from .board import Board
from .dice import Dado
from .player import Jugador
from .checker import Ficha

Color = str  # 'blanco' | 'negro'

class Game:
    """
    Lógica principal de Backgammon:
    turnos, dados, movimientos, captura y bear-off básico.
    """

    def __init__(self,
                 nombre_blanco: str = "Blanco",
                 nombre_negro: str = "Negro") -> None:
        self.tablero = Board()
        self.dados = Dado()
        self.blanco = Jugador("blanco", nombre_blanco)
        self.negro = Jugador("negro", nombre_negro)
        self.turno: Color = "blanco"
        self._mov_pendientes: List[int] = []

    def jugador_actual(self) -> Jugador:
        """Devuelve el objeto Jugador cuyo turno es."""
        return self.blanco if self.turno == "blanco" else self.negro

    def jugador_rival(self) -> Jugador:
        """Devuelve el objeto Jugador rival."""
        return self.negro if self.turno == "blanco" else self.blanco

    def ha_terminado(self) -> bool:
        """Indica si la partida ha terminado."""
        return self.blanco.ha_ganado() or self.negro.ha_ganado()

    def get_ganador(self) -> Optional[str]:
        """Devuelve el nombre del ganador o None."""
        if self.blanco.ha_ganado():
            return self.blanco.get_nombre()
        if self.negro.ha_ganado():
            return self.negro.get_nombre()
        return None

    def iniciar_turno(self) -> Tuple[int, int]:
        """
        Tira los dados y carga _mov_pendientes:
        dobles → 4 movimientos; sino dos valores.
        """
        d1, d2 = self.dados.lanzar()
        if d1 == d2:
            self._mov_pendientes = [d1] * 4
        else:
            self._mov_pendientes = [v for v in (d1, d2) if v > 0]
        return (d1, d2)

    def movimientos_disponibles(self) -> List[int]:
        """Lista de valores pendientes de uso en el turno."""
        return list(self._mov_pendientes)

    def sin_movimientos(self) -> bool:
        """Indica si ya se usaron todos los valores del turno."""
        return len(self._mov_pendientes) == 0

    def terminar_turno(self) -> None:
        """Limpia los movimientos y cambia el turno."""
        self._mov_pendientes.clear()
        self.turno = "negro" if self.turno == "blanco" else "blanco"

    def _dir(self, color: Color) -> int:
        """Dirección de movimiento según color."""
        return -1 if color == "blanco" else +1

    def _destino(self, origen: int, pasos: int) -> int:
        """Calcula el punto destino a partir de origen, pasos y turno."""
        return origen + self._dir(self.turno) * pasos

    def _puede_bear_off_desde(self, origen: int, pasos: int) -> bool:
        """
        Verifica si es un bear-off válido desde un punto con ese dado.
        """
        if not self.tablero.puede_bear_off(self.turno):
            return False
        # punto debe estar en casa
        casa = self.tablero.CASA_BLANCA if self.turno == "blanco" else self.tablero.CASA_NEGRA
        if origen not in casa:
            return False
        destino = self._destino(origen, pasos)
        return destino < 1 or destino > 24

    def _consumir(self, pasos: int) -> bool:
        """
        Quita el valor de dado usado de la lista.
        Retorna False si el valor no estaba disponible.
        """
        try:
            self._mov_pendientes.remove(pasos)
            return True
        except ValueError:
            return False

    def intentar_mover(self, origen: int, pasos: int) -> None:
        """
        Intenta mover una ficha.
        Lanza ValueError con mensaje en cualquier error.
        """
        if pasos <= 0:
            raise ValueError("Los pasos deben ser positivos")
        if pasos not in self._mov_pendientes:
            raise ValueError("Ese valor de dado no está disponible")
        if not 1 <= origen <= 24:
            raise ValueError("El punto de origen debe estar entre 1 y 24")
        if self.tablero.get_cantidad_fichas(origen) == 0:
            raise ValueError(f"No hay fichas en el punto {origen}")
        if self.tablero.get_color_fichas(origen) != self.turno:
            raise ValueError(f"No hay fichas {self.turno} en el punto {origen}")

        # Bear-off
        if self._puede_bear_off_desde(origen, pasos):
            ficha = self.tablero.sacar_ficha(origen)
            ficha.mover_fuera_tablero()
            self.jugador_actual().agregar_fuera()
            self._consumir(pasos)
            return

        destino = self._destino(origen, pasos)
        if not 1 <= destino <= 24:
            raise ValueError("Destino fuera del tablero y no es bear-off válido")
        if not self.tablero.puede_mover_a(destino, self.turno):
            raise ValueError(f"El punto {destino} está bloqueado")

        captura = self.tablero.mover_ficha(origen, destino, self.turno)
        if captura:
            self.jugador_rival().agregar_a_barra()

        self._consumir(pasos)

    def lanzar_dados(self) -> Tuple[int, int]:
        """
        Alias para CLI: si no hay movimientos pendientes, inicia turno;
        si ya hay, devuelve un recordatorio de dos valores.
        """
        if self.sin_movimientos():
            return self.iniciar_turno()
        movs = self.movimientos_disponibles()
        return (movs[0], movs[1] if len(movs) > 1 else 0)

    def mover(self, origen: int, destino: int) -> None:
        """
        Alias CLI: calcula pasos según color, llama intentar_mover
        y termina turno si no quedan movimientos.
        """
        pasos = (origen - destino) if self.turno == "blanco" else (destino - origen)
        if pasos <= 0:
            raise ValueError("Dirección inválida para este color")
        self.intentar_mover(origen, pasos)
        if self.sin_movimientos() and not self.ha_terminado():
            self.terminar_turno()

    def mostrar_tablero(self) -> str:
        """Alias CLI: devuelve la cadena de tablero actual."""
        return self.tablero.mostrar_tablero()