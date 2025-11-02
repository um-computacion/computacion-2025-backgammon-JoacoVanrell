# JUSTIFICACION# JUSTIFICACION


## Resumen del diseño general

Separación en capas:Separación en capas:

- `core/`: lógica pura (Board, Game, Player, Dice, Checker).
- `cli/`: interfaz de texto completamente funcional.

- `pygame_ui/`: interfaz gráfica implementada con arquitectura modular.

**Objetivo:** que la lógica sea testeable sin depender de la UI.


## Clases y responsabilidades

### Módulo Core

- **Game**: orquesta turnos, dados, reglas de movimiento (entrada desde barra, bear-off), fin de juego.

- **Board**: estado del tablero (24 puntos), validación de bloqueos/capturas, barra y bear-off completamente implementados. Mantiene configuración inicial oficial de Backgammon.

- **Game**: orquesta turnos, dados, reglas de movimiento (entrada desde barra, bear-off), fin de juego. Incluye validación de movimientos posibles y gestión de movimientos pendientes.

- **Player**: metadatos del jugador (color, nombre) y contadores (barra, fuera). Implementa lógica de victoria cuando todas las fichas están fuera.

- **Dice**: tiradas aleatorias con soporte para dobles (4 movimientos). Sistema de movimientos pendientes que se consumen conforme se usan.

- **Checker**: estado de una ficha (en tablero, barra, fuera).## Justificación de atributos

- Board mantiene listas por punto para facilitar conteo, color y pop/push O(1).

### Módulo CLI- Game guarda dados “pendientes” para reflejar regla de dobles/orden de uso.

- **CLI.py**: interfaz completa de línea de comandos con loop de juego, visualización del tablero en texto, entrada de usuario para movimientos, manejo de errores y opción de salir.- Player lleva contadores simples como vista rápida (se sincroniza con Board).



### Módulo Pygame UI## Decisiones de diseño relevantes

- **main.py**: coordinador principal del juego gráfico. Maneja el game loop, eventos de mouse para selección de fichas, lanzamiento de dados por clic, y pantalla de victoria con opción de reinicio.- **Inmutabilidad de color** en `Ficha` y `Jugador`.

- **drawing.py**: funciones de renderizado del tablero, fichas, dados y mensajes. Incluye sistema de coordenadas para mapear puntos a posiciones en pantalla.- **Separación core/UI** para test y futura Pygame.

- **constants.py**: centraliza todas las constantes (colores, dimensiones, configuración visual).- **Dados reproducibles**: `set_proximas_tiradas` para pruebas deterministas.



## Justificación de atributos## Excepciones y manejo de errores

- Board mantiene listas por punto para facilitar conteo, color y pop/push O(1).- Validaciones de rango (1..24), bloqueo de puntos, dirección por color.

- Game guarda dados "pendientes" (`_mov_pendientes`) para reflejar regla de dobles/orden de uso. Se limpian al terminar turno.- `ValueError` con mensajes claros cuando la regla lo impide.

- Player lleva contadores simples como vista rápida (fichas en barra, fichas fuera).

- Game incluye método `_validar_movimientos_posibles()` que verifica si hay movimientos legales antes de permitir jugar, evitando turnos imposibles.## Estrategia de testing y cobertura

- Unit tests de `Dice` (dobles y cola de tiradas).

## Decisiones de diseño relevantes- Tests de `Game` (captura, barra, reingreso, bear-off, pasar turno).

- **Inmutabilidad de color** en `Ficha` y `Jugador`: el color se define en construcción y no cambia.- Smoke test de CLI (arranque y una jugada simple sin crashear).

- **Separación core/UI** para testing independiente: el core no conoce pygame ni CLI, solo lógica pura.

- **Direcciones de movimiento**: blanco se mueve de 24→1 (-1), negro de 1→24 (+1). Esto se encapsula en `_dir()` en Game.

- **Sistema de turnos**: Game maneja el turno actual y cambia automáticamente cuando se termina el turno con `terminar_turno()`.
- **Bear-off**: implementado con validación estricta de que todas las fichas deben estar en casa antes de poder sacar.
- **Reingreso desde barra**: prioridad obligatoria - si hay fichas en barra, solo se permiten reingresos.

## Mejoras implementadas en pygame_ui

### Separación modular
En lugar de un archivo monolítico, pygame_ui ahora tiene:
- **main.py**: solo lógica de juego y eventos
- **drawing.py**: todo el renderizado visual
- **constants.py**: configuración centralizada

Esto facilita el mantenimiento y permite cambiar la UI sin tocar la lógica.

### Interactividad completa
- **Selección visual**: cuando seleccionas una ficha de origen, se muestra con borde destacado
- **Mensajes informativos**: el usuario siempre sabe qué está pasando (errores, movimientos, turno)
- **Clic para lanzar dados**: cuando no hay movimientos pendientes, cualquier clic lanza los dados
- **Pantalla de victoria**: al terminar la partida, se muestra ganador y opción de jugar de nuevo

### Manejo de casos especiales
- **Fichas en barra**: si tienes fichas capturadas, solo puedes hacer reingresos hasta liberarlas todas
- **Sin movimientos**: si los dados no permiten movimientos legales, el turno se pasa automáticamente
- **Validación en tiempo real**: cada intento de movimiento se valida contra las reglas del core

## Excepciones y manejo de errores
- Validaciones de rango (1..24), bloqueo de puntos, dirección por color.
- `ValueError` con mensajes claros cuando la regla lo impide.
- En CLI: try-except para capturar errores y mostrarlos al usuario sin crashear.
- En Pygame: los errores se capturan y se muestran como mensajes en pantalla.

## Estrategia de testing y cobertura
- **54 tests unitarios** distribuidos en 5 archivos:
  - `test_dice.py`: lanzamiento de dados, dobles, uso de valores
  - `test_player.py`: jugadores, barra, bear-off, victoria
  - `test_checker.py`: estado de fichas
  - `test_board.py`: configuración inicial, movimientos, validaciones, bear-off
  - `test_game.py`: flujo de juego, turnos, captura, reingreso, victoria
- **Cobertura >90%** en módulo core usando coverage.py
- **Pylint**: validación de calidad de código con score mínimo 8.0/10

## Integración entre capas
El flujo de una jugada es:
1. **Usuario** (CLI o Pygame) → solicita movimiento
2. **Game** → valida que sea el turno correcto y haya dados disponibles
3. **Board** → valida reglas específicas (bloqueos, capturas)
4. **Game** → ejecuta movimiento, actualiza contadores de jugador
5. **Game** → consume dado usado de `_mov_pendientes`
6. **UI** → recibe confirmación o error y actualiza visualización

Esta separación permite que el mismo core funcione para ambas interfaces sin modificación.

## Diagrama UML de Clases

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              PAQUETE: core                                  │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────┐
│         «class»              │
│           Ficha              │
├──────────────────────────────┤
│ - _color: str                │
│ - _posicion: Optional[int]   │
│ - _en_barra: bool            │
│ - _fuera_tablero: bool       │
├──────────────────────────────┤
│ + __init__(color: str)       │
│ + get_color(): str           │
│ + get_posicion(): int?       │
│ + set_posicion(pos: int)     │
│ + esta_en_barra(): bool      │
│ + mover_a_barra()            │
│ + esta_fuera_tablero(): bool │
│ + mover_fuera_tablero()      │
│ + esta_en_tablero(): bool    │
└──────────────────────────────┘
         △
         │
         │ gestiona (0..30)
         │
┌──────────────────────────────┐         ┌──────────────────────────────┐
│         «class»              │         │         «class»              │
│          Jugador             │         │           Dado               │
├──────────────────────────────┤         ├──────────────────────────────┤
│ + TOTAL_FICHAS: int = 15     │         │ - _dado1: int                │
│ - _color: str                │         │ - _dado2: int                │
│ - _nombre: str               │         │ - _proximas_tiradas: list    │
│ - _en_barra: int             │         ├──────────────────────────────┤
│ - _fuera: int                │         │ + __init__()                 │
├──────────────────────────────┤         │ + lanzar(): tuple            │
│ + __init__(color, nombre?)   │         │ + get_valores(): tuple       │
│ + get_color(): str           │         │ + es_doble(): bool           │
│ + get_nombre(): str          │         │ + set_proximas_tiradas()     │
│ + get_fichas_en_barra(): int │         └──────────────────────────────┘
│ + sacar_de_barra()           │                     △
│ + agregar_a_barra()          │                     │
│ + get_fichas_fuera(): int    │                     │ contiene (1)
│ + agregar_fuera()            │                     │
│ + ha_ganado(): bool          │         ┌───────────┴──────────────────┐
└──────────────────────────────┘         │                              │
         △                               │                              │
         │                               │                              │
         │ contiene (2)                  │                              │
         │                               │                              │
┌────────┴──────────────────────────────┴────────────────────────────────────┐
│                            «class» Game                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ + tablero: Board                                                            │
│ + dados: Dado                                                               │
│ + blanco: Jugador                                                           │
│ + negro: Jugador                                                            │
│ + turno: str                                                                │
│ - _mov_pendientes: List[int]                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ + __init__(nombre_blanco: str, nombre_negro: str)                           │
│ + jugador_actual(): Jugador                                                 │
│ + jugador_rival(): Jugador                                                  │
│ + ha_terminado(): bool                                                      │
│ + get_ganador(): str?                                                       │
│ + iniciar_turno(): tuple                                                    │
│ + lanzar_dados(): tuple                                                     │
│ + movimientos_disponibles(): list                                           │
│ + sin_movimientos(): bool                                                   │
│ + terminar_turno()                                                          │
│ - _dir(color: str): int                                                     │
│ - _destino(origen: int, pasos: int): int                                    │
│ - _puede_bear_off_desde(origen: int, pasos: int): bool                      │
│ - _validar_movimientos_posibles(): bool                                     │
│ - _consumir(pasos: int): bool                                               │
│ + mover(origen: int, destino: int): bool                                    │
│ + intentar_mover(origen: int, destino: int, pasos: int): bool               │
│ + reingresar_ficha(pasos: int): bool                                        │
│ + bear_off(origen: int, pasos: int): bool                                   │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         │ contiene (1)
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            «class» Board                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ + CASA_BLANCA: range(1, 7)                                                  │
│ + CASA_NEGRA: range(19, 25)                                                 │
│ - _puntos: List[List[Ficha]]                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ + __init__()                                                                │
│ - _configurar_posicion_inicial()                                            │
│ + get_punto(numero_punto: int): List[Ficha]                                 │
│ + get_cantidad_fichas(numero_punto: int): int                               │
│ + get_color_fichas(numero_punto: int): str?                                 │
│ + puede_mover_a(punto_destino: int, color_jugador: str): bool               │
│ + sacar_ficha(punto_origen: int): Ficha                                     │
│ + poner_ficha(punto_destino: int, ficha: Ficha)                             │
│ + mover_ficha(origen: int, destino: int, color: str): bool                  │
│ + capturar_ficha(punto: int): Ficha                                         │
│ + get_fichas_en_casa(color: str): int                                       │
│ + puede_bear_off(color: str): bool                                          │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         PAQUETE: cli                                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────┐
│         «class»              │
│            CLI               │
├──────────────────────────────┤
│ (módulo funcional)           │
├──────────────────────────────┤
│ + main()                     │
└──────────────────────────────┘
              │
              │ usa
              ▼
         (Game del core)

┌─────────────────────────────────────────────────────────────────────────────┐
│                      PAQUETE: pygame_ui                                     │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────┐    ┌──────────────────────────────┐
│       «constants»            │    │        «drawing»             │
│        Constants             │    │         Drawing              │
├──────────────────────────────┤    ├──────────────────────────────┤
│ + WIDTH: int                 │    │ + dibujar_todo()             │
│ + HEIGHT: int                │    │ + dibujar_tablero()          │
│ + COLOR_FONDO: tuple         │    │ + dibujar_fichas()           │
│ + COLOR_PUNTO_CLARO: tuple   │    │ + dibujar_info()             │
│ + COLOR_PUNTO_OSCURO: tuple  │    │ + get_punto_from_coords()    │
│ + COLOR_BLANCO: tuple        │    └──────────────────────────────┘
│ + COLOR_NEGRO: tuple         │                 │
└──────────────────────────────┘                 │ usa
              △                                  │
              │ usa                              │
              │                                  │
┌─────────────┴──────────────────────────────────┴───────────────────────────┐
│                          «main» Main                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ + mostrar_pantalla_final(screen, ganador): bool                             │
│ + main()                                                                    │
└─────────────────────────────────────────────────────────────────────────────┘
              │
              │ usa
              ▼
         (Game del core)

═══════════════════════════════════════════════════════════════════════════════

RELACIONES:

  ◆────▶  Composición (contiene, ciclo de vida compartido)
  ◇────▶  Agregación (gestiona, ciclo de vida independiente)
  ────▶   Dependencia (usa)
  ─ ─ ▶   Dependencia débil

Game ◆──── Board       (Game contiene un Board)
Game ◆──── Dado        (Game contiene un Dado)
Game ◆──── Jugador(2)  (Game contiene 2 Jugadores)
Board ◇──── Ficha(*)   (Board gestiona 0 a 30 Fichas)
CLI ─ ─ ─▶ Game        (CLI usa Game)
Main ─ ─ ─▶ Game       (Main usa Game)
Main ─ ─ ─▶ Drawing    (Main usa Drawing)
Main ─ ─ ─▶ Constants  (Main usa Constants)
Drawing ─ ─ ─▶ Constants (Drawing usa Constants)

═══════════════════════════════════════════════════════════════════════════════
```

### Notas sobre el diseño:

1. **Game** es el orquestador principal que coordina tablero, dados y jugadores
2. **Board** gestiona el tablero de 24 puntos y valida movimientos según reglas
3. **Ficha** representa fichas individuales que pueden estar en tablero, barra o fuera
4. **Separación de capas**: core/ no depende de cli/ ni pygame_ui/
5. **Reutilización**: CLI y Pygame usan el mismo core sin modificarlo
