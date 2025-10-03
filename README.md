# Proyecto Backgammon

**Autor:** Joaquín Vanrell  
**Carrera:** Ingeniería en Informática  
**Materia:** Computación I  
**Universidad:** Universidad de Mendoza  
**Año:** 2025  

---

## Descripción
Este es mi proyecto final de la materia Computación I. Implementé el juego **Backgammon** en Python usando programación orientada a objetos.

El objetivo era aprender a:
- Organizar el código en clases y módulos
- Separar la lógica del juego de la interfaz
- Escribir tests para verificar que todo funciona
- Documentar el código y el proyecto

### Lo que hace el juego:
- Tablero de Backgammon con 24 puntos
- Fichas que se pueden mover, capturar y sacar del tablero
- Dados que se lanzan para determinar los movimientos
- Turnos entre dos jugadores (blanco y negro)
- Reglas básicas del Backgammon (movimientos, capturas, bear-off)
- Interfaz simple en la terminal para jugar

---

## Cómo está organizado el proyecto

```
proyecto/
├── core/                    # Aquí está toda la lógica del juego
│   ├── board.py            # El tablero de 24 puntos
│   ├── checker.py          # Las fichas del juego
│   ├── dice.py             # Los dados
│   ├── game.py             # La lógica principal del juego
│   └── player.py           # Los jugadores
├── cli/                     # La interfaz para jugar en terminal
│   └── CLI.py              # El programa que ejecutas para jugar
├── test/                    # Tests para verificar que todo funciona
│   ├── test_board.py       # Tests del tablero
│   ├── test_checker.py     # Tests de las fichas
│   ├── test_dice.py        # Tests de los dados
│   ├── test_game.py        # Tests del juego
│   └── test_player.py      # Tests de los jugadores
├── requirements.txt         # Programas extra que necesitas instalar
├── README.md               # Este archivo
├── CHANGELOG.md            # Lista de cambios que fui haciendo
└── justificacion.md        # Explico por qué hice las cosas así
```

---

## Cómo usar el proyecto

### Lo que necesitas:
- Python 3.10 o más nuevo
- Una terminal o consola

### Instalar:
1. **Descargar el proyecto:**
   ```bash
   git clone [URL del repositorio]
   cd computacion-2025-backgammon-JoacoVanrell
   ```

2. **Crear un entorno virtual (recomendado):**
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

### Jugar:
```bash
python cli/CLI.py
```

### Ejecutar tests:
```bash
python -m unittest discover test/ -v
```

### Ver cobertura de tests:
```bash
coverage run -m unittest discover test/
coverage report
```

---

## Cómo se juega (básico)

1. **Objetivo:** Sacar todas tus fichas del tablero antes que tu oponente

2. **Tablero:** 
   - 24 puntos numerados del 1 al 24
   - Las fichas blancas van de 24 hacia 1
   - Las fichas negras van de 1 hacia 24

3. **Turnos:**
   - Tiras dos dados
   - Mueves tus fichas según los números que salieron
   - Si sale doble (ej: 3-3), tienes 4 movimientos

4. **Movimientos:**
   - Ingresas el punto de origen (donde está tu ficha)
   - Ingresas el punto de destino (donde la quieres mover)
   - El programa valida si el movimiento es válido

5. **Captura:**
   - Si hay una ficha enemiga sola, la puedes capturar
   - La ficha capturada va a la "barra" y debe reentrar

6. **Bear-off:**
   - Cuando todas tus fichas están en "casa" (puntos 1-6 o 19-24)
   - Puedes empezar a sacarlas del tablero
   - El primero en sacar todas gana

---

## Lo que aprendí haciendo este proyecto

### Conceptos de programación:
- **Clases y objetos:** Cada cosa del juego es una clase (Tablero, Ficha, Dado, etc.)
- **Encapsulación:** Cada clase maneja sus propios datos
- **Separación de responsabilidades:** Cada clase hace una cosa específica
- **Módulos:** Organizar el código en archivos separados

### Herramientas:
- **Git:** Para llevar control de cambios
- **unittest:** Para hacer tests automáticos
- **coverage:** Para ver qué partes del código están probadas
- **Documentación:** README, CHANGELOG, comentarios en el código

### Dificultades que tuve:
- Entender todas las reglas del Backgammon
- Organizar bien las clases y sus responsabilidades
- Hacer que los tests cubran todos los casos
- Manejar los errores y validaciones

---

## Ejemplo de partida

```
=== Backgammon CLI ===

Tablero de Backgammon:
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

Turno de: Jugador 1 (blanco)
Tirada de dados: (4, 2)
Origen (1-24, o 'salir'): 24
Destino (1-24, o 'salir'): 20
```

---

## Estadísticas del proyecto

- **Líneas de código:** ~1,500
- **Clases principales:** 5 (Board, Game, Player, Dice, Checker)  
- **Tests:** 46 pruebas unitarias
- **Cobertura:** >90% del código está probado
- **Tiempo de desarrollo:** 3 meses (parte del cuatrimestre)

---

## Archivos importantes

- **`core/game.py`:** La lógica principal del juego
- **`cli/CLI.py`:** El programa que ejecutas para jugar
- **`test/`:** Todos los tests para verificar que funciona
- **`justificacion.md`:** Explico las decisiones técnicas que tomé
- **`CHANGELOG.md`:** Lista cronológica de todos los cambios

---

