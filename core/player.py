class Jugador:
    TOTAL_FICHAS = 15

    def __init__(self, color: str, nombre: str | None = None) -> None:
        """
        Inicializa un jugador con un color y un nombre opcional.
        Si no se provee nombre, se usa el color capitalizado.
        """
        self._color = color
        self._nombre = nombre or color.title()
        self._en_barra = 0
        self._fuera = 0

    def get_color(self) -> str:
        """Devuelve el color del jugador."""
        return self._color

    def get_nombre(self) -> str:
        """Devuelve el nombre del jugador."""
        return self._nombre

    def get_fichas_en_barra(self) -> int:
        """Devuelve cuántas fichas tiene en la barra."""
        return self._en_barra

    def sacar_de_barra(self) -> None:
        """Quita una ficha de la barra, si hay alguna."""
        if self._en_barra > 0:
            self._en_barra -= 1

    def agregar_a_barra(self) -> None:
        """Agrega una ficha a la barra."""
        self._en_barra += 1

    def get_fichas_fuera(self) -> int:
        """Devuelve cuántas fichas ha sacado del tablero."""
        return self._fuera

    def agregar_fuera(self) -> None:
        """
        Agrega una ficha fuera del tablero.
        No excede TOTAL_FICHAS para no sobrecontar.
        """
        if self._fuera < self.TOTAL_FICHAS:
            self._fuera += 1

    def ha_ganado(self) -> bool:
        """Indica si el jugador ha ganado (todas sus fichas fuera)."""

