# Changelog

Todos los cambios importantes de este proyecto serán documentados en este archivo.  
El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Liberado] - 2025-10-14

### Agregado
- Interactividad completa con mouse en pygame (`pygame_ui/main.py`):
  - Detección de clics en todas las fichas del tablero.
  - Feedback visual con borde rojo cuando una ficha está seleccionada.
  - Borde más grueso (4px) para destacar fichas seleccionadas.
  - Variables de estado para tracking de selección (`ficha_seleccionada`).
- Configuración inicial completa del Backgammon (30 fichas):
  - **Fichas blancas**: punto 24 (2), punto 13 (5), punto 8 (3), punto 6 (5).
  - **Fichas negras**: punto 1 (2), punto 12 (5), punto 17 (3), punto 19 (5).
  - Posicionamiento correcto según reglas oficiales del Backgammon.
  - Espaciado adecuado entre fichas apiladas (25 píxeles).
- Funciones helper para código más limpio:
  - `dibujar_ficha()`: Renderizado uniforme de fichas con selección.
  - `clic_en_ficha()`: Detección de clics simplificada.
- Sistema de nombres únicos para cada ficha (ej: `blanca_13_2`, `negra_17_1`).

### Mejorado
- Interfaz de información del juego optimizada:
  - Texto de fichas seleccionadas más conciso (`"Seleccionada: Blanca P13"`).
  - Mejor distribución del espacio en pantalla (sin superposiciones).
  - Espaciado corregido entre elementos informativos.
- Código más mantenible con funciones reutilizables.
- Todas las 30 fichas del juego son completamente interactivas.

### Corregido
- Posicionamiento correcto de fichas según numeración del Backgammon.
- Mapeo correcto entre puntos del tablero y posiciones visuales.
- Detección de clics sincronizada con posiciones reales de las fichas.
- Texto informativo que no se sale de los límites de la pantalla.

---

## [Liberado] - 2025-10-10

### Agregado
- Fichas básicas en la interfaz pygame (`pygame_ui/main.py`):
  - Fichas representadas como círculos con bordes negros.
  - Colores diferenciados: fichas blancas y fichas negras.
  - Posicionamiento inicial de ejemplo en puntos 1 y 24.
  - Radio de ficha configurable (15 píxeles).
- Información del juego en pantalla:
  - Indicador de turno actual del jugador.
  - Visualización de valores de dados (valores fijos temporales).
  - Instrucciones básicas para el usuario.
  - Fuente configurada para texto legible.

### Mejorado
- Interfaz pygame con elementos informativos para mejor experiencia de usuario.
- Organización visual del tablero con elementos de juego básicos.

---

## [Liberado] - 2025-10-08

### Agregado
- Interfaz gráfica básica con pygame (`pygame_ui/`):
  - Ventana de juego de 800x600 píxeles funcional.
  - Tablero visual con los 24 puntos representados como triángulos.
  - Colores alternados para puntos claros y oscuros.
  - Barra central separando ambos lados del tablero.
  - Layout simétrico siguiendo las reglas del Backgammon.
- Dependencia pygame agregada a `requirements.txt`.

---

## [Liberado] - 2025-10-03

### Fixed
- Corrección del test `test_captura_aumenta_barra_del_rival` en `test/test_game.py`:
  - Agregado método `puede_bear_off()` faltante en el stub `_BoardStubCaptura`.
  - El stub ahora devuelve `False` para simular que no es una situación de bear-off.
  - Todos los 46 tests ahora pasan correctamente.

---

## [Liberado] - 2025-10-01

### Agregado
- Documentación completa del proyecto:
  - `README.md` con descripción detallada del proyecto, estructura y características.
  - `requirements.txt` con dependencias del proyecto (coverage).
  - `justificacion.md` con justificación técnica del proyecto.
- Archivos de documentación de desarrollo:
  - `prompts-desarrollo.md` - Registro de prompts utilizados en el desarrollo.
  - `prompts-documentacion.md` - Prompts para la documentación.
  - `prompts-testing.md` - Prompts para testing y pruebas.

### Mejorado
- Cobertura de tests ampliada en `core/game.py` para alcanzar >90% de coverage.
- Refinamiento de la lógica del juego con mejores validaciones.

---

## [Liberado] - 2025-09-15

### Agregado
- CLI mejorado (`core/main.py`):
  - Validación segura de conversión a entero en prompts de origen y destino.  
  - Manejo de `salir` en ambos inputs para abandonar la partida.  
  - Mensajes de error claros ante entradas inválidas.
- Tests adicionales para elevar coverage > 90%:
  - `test/test_board_extra.py`: cubre casos de `get_punto`, `get_cantidad_fichas`, `get_color_fichas`, `puede_mover_a`, `es_movimiento_valido`, `sacar_ficha`, `mover_ficha`, `get_fichas_en_casa` y bear-off.
  - `test/test_cli.py`: verifica impresión inicial del CLI, salida con `salir` y captura de movimientos inválidos.
  - Extensión de tests en `core/player.py` y `core/game.py` para cubrir ramas faltantes.

### Cambiado
- Refactor en `core/main.py` para un flujo de juego más robusto, aislando la lógica de validación de inputs.

### Fixed
- Corrección de errores de rango en `get_punto()` y validación de movimientos en `es_movimiento_valido()` e `intentar_mover()`.

---

## [Liberado] - 2025-09-10

### Agregado
- Implementación completa de la **Interfaz CLI** (`cli/CLI.py`):
  - Interfaz de línea de comandos totalmente funcional para jugar Backgammon.
  - Loop principal del juego con manejo de turnos.
  - Entrada de usuario para movimientos (origen y destino).
  - Opción para salir del juego en cualquier momento con comando 'salir'.
  - Visualización del estado del tablero y información de turnos.
  - Manejo de tiradas de dados y movimientos pendientes.

### Mejorado
- Refinamiento de todas las clases del core con correcciones de bugs.
- Mejora en la validación de movimientos y manejo de errores.
- Optimización de la lógica del tablero y posicionamiento de fichas.

---

## [Liberado] - 2025-09-05

### Agregado
- **Clase `Board` (Tablero)** (`core/board.py`):
  - Representación completa del tablero de Backgammon con 24 puntos.
  - Configuración inicial automática de fichas según reglas oficiales.
  - Métodos para obtener información de puntos: `get_punto()`, `get_cantidad_fichas()`, `get_color_fichas()`.
  - Validación de movimientos: `puede_mover_a()`, `es_movimiento_valido()`.
  - Operaciones de fichas: `sacar_ficha()`, `mover_ficha()`.
  - Soporte para bear-off y gestión de fichas en casa.
  - Representación visual del tablero con `mostrar_tablero()`.

- **Clase `Game` (Juego Principal)** (`core/game.py`):
  - Lógica principal del juego de Backgammon.
  - Gestión de turnos entre jugadores blanco y negro.
  - Integración de dados, tablero y jugadores.
  - Manejo de movimientos pendientes y validación.
  - Detección de condiciones de victoria.
  - Métodos para lanzar dados y realizar movimientos.

### Mejorado
- Completado el sistema de tests con mayor cobertura.
- Refinamiento de la clase `Jugador` con métodos adicionales.
- Mejoras en la clase `Ficha` para mejor integración con el tablero.

---

## [Liberado] - 2025-09-01

### Agregado
- Clase `Ficha` para representar fichas individuales  
  - Manejo de posición en tablero (puntos 1–24)  
  - Estados: en tablero, en barra, fuera del tablero  
  - Métodos para mover entre estados  
  - Comparación entre fichas y representación string

### Cambiado  
- Completada clase `Jugador` con funcionalidad completa  
  - Métodos para manejo de fichas en barra  
  - Métodos para bear-off (fichas fuera del tablero)  
  - Implementado método `ha_ganado()` para verificar victoria  
  - Documentación completa con docstrings en todos los métodos

---

## [Liberado] - 2025-08-30

### Agregado
- **Suite completa de Tests Unitarios**:
  - `test/test_dice.py` - Tests para la clase `Dado` con validación de tiradas y dobles.
  - `test/test_player.py` - Tests extensivos para la clase `Jugador` incluyendo manejo de fichas en barra y bear-off.
  - `test/test_checker.py` - Tests para la clase `Ficha` con todos los estados y transiciones.
  - `test/test_board.py` - Tests para la clase `Board` con validación de movimientos y configuración inicial.
  - `test/test_game.py` - Tests para la lógica principal del juego.
  - Configuración inicial de coverage testing con herramientas de análisis.

### Mejorado
- Completada funcionalidad de la clase `Jugador`:
  - Métodos para manejo de fichas: `agregar_ficha_barra()`, `quitar_ficha_barra()`.
  - Métodos para bear-off: `agregar_ficha_fuera()`, `get_fichas_fuera()`.
  - Lógica de victoria: `ha_ganado()` verifica si todas las fichas están fuera.
  - Contadores de fichas: `get_fichas_en_barra()`.

---

## [liberado] - 2025-08-29

### Agregado
- Estructura inicial del proyecto con carpetas `core/`, `cli/`, `pygame_ui/`, `assets/`, `tests/`
- Clase `Dado` para manejo de dados del juego  
  - Método `lanzar_dados()` para tirar dos dados  
  - Manejo de tiradas dobles (4 movimientos)  
  - Método `usar_lanzada()` para consumir movimientos  
  - Métodos auxiliares para obtener valores y verificar dobles  
- Clase `Jugador` básica para representar jugadores  
  - Constructor con nombre y color  
  - Métodos getter básicos  
  - Representación string del jugador  
- Archivo `.gitignore` para mantener repositorio limpio  
- Documentación inicial del proyecto

### Por hacer
- ~~Completar funcionalidad de la clase `Jugador`~~ ✅ Completado  
- ~~Implementar clase `Tablero`~~ ✅ Completado  
- ~~Crear clase `Juego` principal~~ ✅ Completado  
- ~~Desarrollar interfaz CLI~~ ✅ Completado  
- ~~Implementar tests unitarios~~ ✅ Completado
- Desarrollar interfaz gráfica con Pygame (futuro)
- Implementar funcionalidades avanzadas (doubling cube, match play)
- Agregar inteligencia artificial para jugador automatizado

---

## [Estructura del Proyecto]

```
computacion-2025-backgammon-JoacoVanrell/
├── core/                    # Lógica principal del juego
│   ├── __init__.py         # Módulo core
│   ├── board.py            # Clase Board (tablero)
│   ├── checker.py          # Clase Ficha 
│   ├── dice.py             # Clase Dado
│   ├── game.py             # Clase Game (lógica principal)
│   └── player.py           # Clase Jugador
├── cli/                    # Interfaz de línea de comandos
│   └── CLI.py              # Interfaz CLI funcional
├── test/                   # Tests unitarios
│   ├── test_board.py       # Tests del tablero
│   ├── test_checker.py     # Tests de fichas
│   ├── test_dice.py        # Tests de dados
│   ├── test_game.py        # Tests del juego
│   └── test_player.py      # Tests de jugadores
├── pygame_ui/              # Interfaz gráfica (futuro)
├── assets/                 # Recursos gráficos
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Documentación principal
├── CHANGELOG.md           # Este archivo
└── justificacion.md       # Justificación técnica
```

