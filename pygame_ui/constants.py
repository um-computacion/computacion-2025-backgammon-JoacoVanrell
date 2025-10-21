"""
Constantes para la interfaz pygame de Backgammon
Basado en la estructura del profesor
"""

# === DIMENSIONES DE PANTALLA ===
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
MARGIN = 50

# === COLORES PROFESIONALES ===
# Colores de fondo
BACKGROUND_COLOR = (240, 228, 188)      # Beige claro profesional
BOARD_COLOR = (139, 121, 94)            # Marrón para el tablero

# Colores de triángulos (alternados)
TRIANGLE_COLOR_A = (218, 165, 32)       # Dorado
TRIANGLE_COLOR_B = (160, 82, 45)        # Marrón rojizo

# Colores de líneas y texto
LINE_COLOR = (101, 67, 33)              # Marrón oscuro para líneas
TEXT_COLOR = (101, 67, 33)              # Marrón oscuro para texto

# Colores de fichas
WHITE_CHECKER = (255, 255, 255)         # Fichas blancas
BLACK_CHECKER = (50, 50, 50)            # Fichas negras

# Colores de selección y destacado
SELECTED_COLOR = (255, 0, 0)            # Rojo para selección
HIGHLIGHT_COLOR = (255, 255, 0)         # Amarillo para destacar

# === CONFIGURACIÓN DEL TABLERO ===
BOARD_WIDTH = SCREEN_WIDTH - 2 * MARGIN
BOARD_HEIGHT = SCREEN_HEIGHT - 2 * MARGIN - 60  # Espacio para UI
TRIANGLE_COUNT = 12                      # 12 triángulos por lado
TRIANGLE_WIDTH = BOARD_WIDTH / TRIANGLE_COUNT

# === CONFIGURACIÓN DE FICHAS ===
CHECKER_RADIUS = 18                      # Radio de las fichas
MAX_VISIBLE_CHECKERS = 5                 # Máximo de fichas visibles en una pila
CHECKER_STACK_GAP = 4                    # Separación entre fichas apiladas

# === FUENTES ===
FONT_SIZE = 20
SMALL_FONT_SIZE = 16

# === POSICIONES INICIALES DEL BACKGAMMON ===
INITIAL_SETUP = {
    # Fichas blancas
    24: ('white', 2),
    13: ('white', 5), 
    8: ('white', 3),
    6: ('white', 5),
    # Fichas negras
    1: ('black', 2),
    12: ('black', 5),
    17: ('black', 3),
    19: ('black', 5)
}