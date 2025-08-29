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

### [Versión] - Fecha

#### Agregado
- Nuevas características

#### Cambiado  
- Cambios en funcionalidad existente

#### Deprecated
- Características que serán removidas

#### Removido
- Características removidas

#### Arreglado
- Bugs corregidos

#### Seguridad
- Vulnerabilidades corregidas