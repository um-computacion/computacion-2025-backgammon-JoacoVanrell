# Changelog

Todos los cambios importantes de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [liberado] - 2025-08-29

### Agregado
- Estructura inicial del proyecto con carpetas core/, cli/, pygame_ui/, assets/, tests/
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

## Plantilla para futuras entradas

### [Liberado] - 2025-09-01

#### Agregado
- Clase Ficha para representar fichas individuales
  - Manejo de posición en tablero (puntos 1-24)
  - Estados: en tablero, en barra, fuera del tablero
  - Métodos para mover entre estados
  - Comparación entre fichas y representación string

#### Cambiado  
- Completada clase Jugador con funcionalidad completa
  - Agregados métodos para manejo de fichas en barra
  - Agregados métodos para bear-off (fichas fuera del tablero)
  - Implementado método ha_ganado() para verificar victoria
  - Documentación completa con docstrings en todos los métodos

#### Deprecated
- Características que serán removidas

#### Removido
- Características removidas

#### Arreglado
- Bugs corregidos

#### Seguridad
- Vulnerabilidades corregidas