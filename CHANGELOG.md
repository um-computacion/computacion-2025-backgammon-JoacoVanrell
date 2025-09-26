# Changelog

Todos los cambios importantes de este proyecto serán documentados en este archivo.  
El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
- Completar funcionalidad de la clase `Jugador`  
- Implementar clase `Tablero`  
- Crear clase `Juego` principal  
- Desarrollar interfaz CLI  
- Implementar tests unitarios

