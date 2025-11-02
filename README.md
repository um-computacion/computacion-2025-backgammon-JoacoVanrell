# Proyecto Backgammon

**Autor:** Joaquín Vanrell  
**Carrera:** Ingeniería en Informática  
**Materia:** Computación I  
**Universidad:** Universidad de Mendoza  
**Año:** 2025  

---

## Descripción

Este es mi proyecto final de la materia Computación I. Implementé el juego **Backgammon** en Python utilizando programación orientada a objetos, siguiendo las mejores prácticas de desarrollo de software.

### Objetivos del proyecto:
- Implementar las reglas completas del Backgammon
- Aplicar conceptos de POO (clases, herencia, encapsulación)
- Separar la lógica del juego de las interfaces
- Escribir tests unitarios completos
- Mantener código limpio y documentado
- Usar herramientas de calidad de código (pylint, coverage)

### Características implementadas:
- ✅ Tablero de Backgammon con 24 puntos
- ✅ Movimiento de fichas con validación de reglas
- ✅ Sistema de captura y barra
- ✅ Bear-off (sacar fichas del tablero)
- ✅ Dados con soporte para dobles
- ✅ Detección de victoria
- ✅ Interfaz CLI funcional
- ✅ Interfaz gráfica con Pygame
- ✅ 54 tests unitarios (100% aprobados)
- ✅ Cobertura de código >90%
- ✅ Código validado con pylint (score ≥8.0)

---

## Estructura del proyecto

```
computacion-2025-backgammon-JoacoVanrell/
├── core/                    # Lógica del juego (independiente de UI)
│   ├── __init__.py
│   ├── board.py            # Tablero (24 puntos, validaciones)
│   ├── checker.py          # Fichas (estado, posición)
│   ├── dice.py             # Dados (tiradas, dobles)
│   ├── game.py             # Juego (turnos, reglas, victoria)
│   └── player.py           # Jugadores (color, nombre, contadores)
│
├── cli/                     # Interfaz de línea de comandos
│   └── CLI.py              # Programa principal CLI
│
├── pygame_ui/               # Interfaz gráfica con Pygame
│   ├── __init__.py
│   ├── main.py             # Programa principal Pygame
│   ├── constants.py        # Constantes visuales
│   ├── drawing.py          # Renderizado del tablero
│
├── test/                    # Tests unitarios
│   ├── __init__.py
│   ├── test_board.py       # Tests del tablero
│   ├── test_checker.py     # Tests de las fichas
│   ├── test_dice.py        # Tests de los dados
│   ├── test_game.py        # Tests del juego
│   └── test_player.py      # Tests de los jugadores
│
├── .pylintrc               # Configuración de pylint
├── .coveragerc             # Configuración de coverage
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
├── CHANGELOG.md           # Historial de cambios
└── justificacion.md       # Decisiones de diseño
```

---

## Instalación y configuración

### Requisitos previos:
- **Python 3.10 o superior**
- **pip** (gestor de paquetes de Python)
- **git** (para clonar el repositorio)

### Pasos de instalación:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/um-computacion/computacion-2025-backgammon-JoacoVanrell.git
   cd computacion-2025-backgammon-JoacoVanrell
   ```

2. **Crear entorno virtual (recomendado):**
   ```bash
   python3 -m venv venv
   
   # En Linux/Mac:
   source venv/bin/activate
   
   # En Windows:
   venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Cómo usar el proyecto

### Opción 1: Jugar en la terminal (CLI)

```bash
python3 cli/CLI.py
```

**Comandos durante el juego:**
- Ingresa el número del punto de origen (1-24)
- Ingresa el número del punto de destino (1-24)
- Escribe `salir` para terminar la partida

### Opción 2: Jugar con interfaz gráfica (Pygame)

```bash
python3 pygame_ui/main.py
```

### Ejecutar todos los tests:

```bash
python3 -m unittest discover -s test -v
```

**Resultado esperado:** 46 tests aprobados

### Ver cobertura de código:

```bash
# Ejecutar tests con coverage
python3 -m coverage run -m unittest discover -s test

# Ver reporte en terminal
python3 -m coverage report

# Generar reporte HTML
python3 -m coverage html
# Abrir htmlcov/index.html en un navegador
```

**Cobertura esperada:** >90% en el módulo `core/`

### Verificar calidad con pylint:

```bash
# Verificar el core
pylint core/

# Verificar el CLI
pylint cli/

# Verificar todo
pylint core/ cli/
```

**Score esperado:** ≥8.0/10.0

---

## Reglas del Backgammon (resumen)

### Objetivo:
Ser el primero en sacar todas tus 15 fichas del tablero.

### Tablero:
- 24 puntos numerados
- Jugador blanco mueve de 24→1
- Jugador negro mueve de 1→24

### Mecánica del juego:

1. **Lanzar dados**: Cada turno tiras dos dados
2. **Mover fichas**: Usa los valores de los dados para mover
3. **Dobles**: Si sacas doble (ej: 3-3), tienes 4 movimientos
4. **Captura**: Si una ficha enemiga está sola, puedes capturarla (va a la barra)
5. **Reingreso**: Las fichas capturadas deben reingresar antes de hacer otros movimientos
6. **Bear-off**: Cuando todas tus fichas están en casa (últimos 6 puntos), puedes sacarlas
7. **Victoria**: El primero en sacar todas sus fichas gana

### Restricciones:
- No puedes mover a un punto con 2+ fichas enemigas
- Debes usar todos los dados si es posible
- Si solo puedes usar un dado, debes usar el mayor

---

## Ejemplo de partida

```
=== Backgammon CLI ===

Tablero actual:
==================================================
13 14 15 16 17 18   19 20 21 22 23 24
 N  N  N  N  N  N  |  B  B
 N  N  N  N  N     |  B
 N  N  N           |
 N  N              |
 N                 |
--------------------------------------------------
 B  B              |  N
 B  B              |  N
 B  B              |  N  N  N
 B  B              |  N  N  N
 B                 |  N  N  N
12 11 10  9  8  7    6  5  4  3  2  1
==================================================

Turno de: Jugador Blanco
Dados lanzados: (5, 3)
Movimientos disponibles: [5, 3]

Ingresa punto de origen (1-24 o 'salir'): 24
Ingresa punto de destino (1-24 o 'salir'): 19

✓ Movimiento realizado: 24 → 19
Movimientos restantes: [3]

Ingresa punto de origen (1-24 o 'salir'): 13
Ingresa punto de destino (1-24 o 'salir'): 10

✓ Movimiento realizado: 13 → 10
Turno terminado.
```

---

## Arquitectura y diseño

### Principios aplicados:

1. **Separación de responsabilidades**: 
   - `core/`: Lógica pura del juego
   - `cli/` y `pygame_ui/`: Interfaces de usuario
   - `test/`: Pruebas unitarias

2. **Encapsulación**: 
   - Cada clase maneja su propio estado
   - Atributos privados con getters/setters

3. **Abstracción**: 
   - Interfaces claras entre componentes
   - El UI no conoce detalles internos del core

4. **Testing**: 
   - Tests unitarios para cada clase
   - Tests de integración para flujos completos

### Clases principales:

- **`Game`**: Orquesta el juego completo (turnos, dados, victoria)
- **`Board`**: Maneja el tablero y validaciones de movimientos
- **`Player`**: Representa un jugador (color, nombre, contadores)
- **`Dice`**: Maneja los dados y las tiradas
- **`Checker`**: Representa una ficha individual

---

## Tecnologías y herramientas

- **Lenguaje**: Python 3.10+
- **Testing**: unittest (biblioteca estándar)
- **Cobertura**: coverage.py
- **Calidad de código**: pylint
- **UI Gráfica**: pygame 2.6+
- **Control de versiones**: Git/GitHub
- **CI/CD**: GitHub Actions

---


## Problemas conocidos y limitaciones

- La IA de los jugadores no está implementada (solo juego humano vs humano)
- El CLI es básico (sin colores ni formato avanzado)
- No hay persistencia de partidas (guardar/cargar)
- No hay red/multijugador online

---






