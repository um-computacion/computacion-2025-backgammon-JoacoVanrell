# Proyecto Backgammon

**Autor:** Joaquin Vanrell  
**Carrera:** Ingeniería en Informática  
**Materia:** Computación I  

---

## Descripción
Implementación del juego **Backgammon** en Python, desarrollada como parte de la materia Computación I.  
El proyecto está estructurado en módulos independientes (`core`, `cli`, `tests`) que permiten separar la lógica del juego de la interfaz de usuario.  

La lógica incluye:
- Representación del tablero con 24 puntos.
- Gestión de fichas (en tablero, barra y fuera).
- Turnos de jugadores (blancas y negras).
- Tiradas de dados (con soporte para dobles).
- Movimientos, capturas y validación de reglas básicas.
- Condición de victoria por bear-off.

---

## Estructura del Proyecto

/backgammon/
├── core/ # Lógica principal del juego (Board, Game, Jugador, Dado, Ficha)
├── cli/ # Interfaz de línea de comandos (CLI)
├── tests/ # Conjunto de pruebas unitarias
├── JUSTIFICACION.md # Documento con diseño y decisiones
├── README.md # Este archivo
└── CHANGELOG.md # Registro de cambios

## Requisitos
- **Python 3.10+**
- Uso de **entorno virtual** recomendado

Crear y activar el entorno virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate   
.venv\Scripts\activate     

