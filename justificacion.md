# JUSTIFICACION

## Resumen del diseño general
Separación en capas:
- `core/`: lógica pura (Board, Game, Player, Dice, Checker).
- `cli/`: interfaz de texto.
- `pygame_ui/`: (a completar) interfaz gráfica.
**Objetivo:** que la lógica sea testeable sin depender de la UI.

## Clases y responsabilidades
- **Board**: estado del tablero (24 puntos), validación de bloqueos/capturas, (a integrar) barra y borne-off.
- **Game**: orquesta turnos, dados, reglas de movimiento (entrada desde barra, bear-off), fin de juego.
- **Player**: metadatos del jugador (color, nombre) y contadores (barra, fuera).
- **Dice**: tiradas reproducibles y soporte para dobles.
- **Checker**: estado de una ficha (tablero, barra, fuera).

## Justificación de atributos
- Board mantiene listas por punto para facilitar conteo, color y pop/push O(1).
- Game guarda dados “pendientes” para reflejar regla de dobles/orden de uso.
- Player lleva contadores simples como vista rápida (se sincroniza con Board).

## Decisiones de diseño relevantes
- **Inmutabilidad de color** en `Ficha` y `Jugador`.
- **Separación core/UI** para test y futura Pygame.
- **Dados reproducibles**: `set_proximas_tiradas` para pruebas deterministas.

## Excepciones y manejo de errores
- Validaciones de rango (1..24), bloqueo de puntos, dirección por color.
- `ValueError` con mensajes claros cuando la regla lo impide.

## Estrategia de testing y cobertura
- Unit tests de `Dice` (dobles y cola de tiradas).
- Tests de `Game` (captura, barra, reingreso, bear-off, pasar turno).
- Smoke test de CLI (arranque y una jugada simple sin crashear).


