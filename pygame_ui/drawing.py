import pygame
from core.game import Game
from .constants import *

pygame.font.init()
FONT = pygame.font.SysFont("sans-serif", FUENTE_MEDIANA)
FONT_NUMEROS = pygame.font.SysFont("sans-serif", FUENTE_PEQUENA)

def _get_coords_punto(punto):
    """Calcula las coordenadas (x, y) de la base de un punto del tablero, siguiendo el estándar."""
    x, y = 0, 0
    # Puntos en la parte inferior (1-12), de derecha a izquierda
    if 1 <= punto <= 12:
        y = HEIGHT - 50 - MARGEN_TABLERO
        if 1 <= punto <= 6:
            x = WIDTH - MARGEN_TABLERO - ((punto - 1) * ANCHO_TRIANGULO) - ANCHO_TRIANGULO // 2
        else: # 7 a 12
            x = WIDTH - MARGEN_TABLERO - ((punto - 1) * ANCHO_TRIANGULO) - ANCHO_BARRA - ANCHO_TRIANGULO // 2
    # Puntos en la parte superior (13-24), de izquierda a derecha
    elif 13 <= punto <= 24:
        y = MARGEN_TABLERO
        if 13 <= punto <= 18:
            x = MARGEN_TABLERO + ((punto - 13) * ANCHO_TRIANGULO) + ANCHO_TRIANGULO // 2
        else: # 19 a 24
            x = MARGEN_TABLERO + ((punto - 13) * ANCHO_TRIANGULO) + ANCHO_BARRA + ANCHO_TRIANGULO // 2
    return x, y

def dibujar_tablero(screen):
    """Dibuja el tablero con la orientación estándar."""
    screen.fill(COLOR_FONDO)
    
    for i in range(12):
        color = COLOR_TRIANGULO_1 if i % 2 == 0 else COLOR_TRIANGULO_2
        x_base = MARGEN_TABLERO + i * ANCHO_TRIANGULO
        if i >= 6: x_base += ANCHO_BARRA
        
        pygame.draw.polygon(screen, color, [
            (x_base, MARGEN_TABLERO), (x_base + ANCHO_TRIANGULO, MARGEN_TABLERO),
            (x_base + ANCHO_TRIANGULO // 2, MARGEN_TABLERO + ALTO_TRIANGULO)
        ])
        pygame.draw.polygon(screen, color, [
            (x_base, HEIGHT - 50 - MARGEN_TABLERO), (x_base + ANCHO_TRIANGULO, HEIGHT - 50 - MARGEN_TABLERO),
            (x_base + ANCHO_TRIANGULO // 2, HEIGHT - 50 - MARGEN_TABLERO - ALTO_TRIANGULO)
        ])
    
    pygame.draw.rect(screen, COLOR_TRIANGULO_1, (MARGEN_TABLERO + 6 * ANCHO_TRIANGULO, MARGEN_TABLERO, ANCHO_BARRA, HEIGHT - 100))

    for i in range(1, 25):
        x, y = _get_coords_punto(i)
        pos_y = MARGEN_TABLERO - 15 if 13 <= i <= 24 else HEIGHT - 50 - MARGEN_TABLERO + 15
        texto_num = FONT_NUMEROS.render(str(i), True, COLOR_TEXTO)
        rect_num = texto_num.get_rect(center=(x, pos_y))
        screen.blit(texto_num, rect_num)

def get_punto_from_coords(pos):
    """Convierte coordenadas de ratón a un punto del tablero con la lógica corregida."""
    x, y = pos
    
    if not (MARGEN_TABLERO <= x < WIDTH - MARGEN_TABLERO and MARGEN_TABLERO <= y < HEIGHT - 50 - MARGEN_TABLERO):
        return None
    
    # Determinar en qué columna visual (0-11) se hizo clic
    col_visual = (x - MARGEN_TABLERO)
    if col_visual > MARGEN_TABLERO + 6 * ANCHO_TRIANGULO: # Ajustar por la barra
        col_visual -= ANCHO_BARRA
    col_visual //= ANCHO_TRIANGULO

    # Mapear columna visual a punto del tablero
    if y > HEIGHT / 2:  # Parte inferior (1-12, de derecha a izquierda)
        # La columna visual 0 es el punto 12, la 11 es el 1
        return 12 - col_visual
    else:  # Parte superior (13-24, de izquierda a derecha)
        # La columna visual 0 es el punto 13, la 11 es el 24
        return 13 + col_visual

def dibujar_fichas(screen, game: Game, punto_seleccionado=None):
    """Dibuja las fichas del tablero y de la barra."""
    # Dibujar fichas en los puntos
    tablero_logico = game.tablero
    for i in range(1, 25):
        cantidad = tablero_logico.get_cantidad_fichas(i)
        if cantidad > 0:
            color_ficha = COLOR_FICHA_BLANCA if tablero_logico.get_color_fichas(i) == 'blanco' else COLOR_FICHA_NEGRA
            x, y_base = _get_coords_punto(i)
            for j in range(cantidad):
                y = y_base - RADIO_FICHA - j * (2 * RADIO_FICHA) if 1 <= i <= 12 else y_base + RADIO_FICHA + j * (2 * RADIO_FICHA)
                pygame.draw.circle(screen, color_ficha, (x, y), RADIO_FICHA)
                if i == punto_seleccionado and j == cantidad - 1:
                    pygame.draw.circle(screen, (255, 0, 0), (x, y), RADIO_FICHA, 3)
                else:
                    pygame.draw.circle(screen, COLOR_TEXTO, (x, y), RADIO_FICHA, 1)

    # Dibujar fichas en la barra
    x_barra = MARGEN_TABLERO + 6 * ANCHO_TRIANGULO + ANCHO_BARRA // 2
    # Fichas blancas comidas (abajo)
    for i in range(game.blanco.get_fichas_en_barra()):
        y = HEIGHT - 50 - MARGEN_TABLERO - RADIO_FICHA - i * (2 * RADIO_FICHA)
        pygame.draw.circle(screen, COLOR_FICHA_BLANCA, (x_barra, y), RADIO_FICHA)
        pygame.draw.circle(screen, COLOR_TEXTO, (x_barra, y), RADIO_FICHA, 1)
    # Fichas negras comidas (arriba)
    for i in range(game.negro.get_fichas_en_barra()):
        y = MARGEN_TABLERO + RADIO_FICHA + i * (2 * RADIO_FICHA)
        pygame.draw.circle(screen, COLOR_FICHA_NEGRA, (x_barra, y), RADIO_FICHA)
        pygame.draw.circle(screen, COLOR_TEXTO, (x_barra, y), RADIO_FICHA, 1)

def dibujar_footer(screen, game: Game, mensaje=""):
    """Dibuja el área de información debajo del tablero."""
    footer_y = HEIGHT - 50
    pygame.draw.rect(screen, COLOR_TRIANGULO_1, (0, footer_y, WIDTH, 50))
    texto_turno = FONT.render(f"Turno: {game.turno.capitalize()}", True, COLOR_TEXTO)
    screen.blit(texto_turno, (MARGEN_TABLERO, footer_y + 15))
    dados = game.movimientos_disponibles()
    if dados:
        texto_dados = FONT.render(f"Dados: {dados}", True, COLOR_TEXTO)
        screen.blit(texto_dados, (WIDTH // 2 - 50, footer_y + 15))
    texto_mensaje = FONT.render(mensaje, True, COLOR_TEXTO)
    rect_mensaje = texto_mensaje.get_rect(right=WIDTH - MARGEN_TABLERO, centery=footer_y + 25)
    screen.blit(texto_mensaje, rect_mensaje)

def dibujar_todo(screen, game: Game, mensaje="", punto_seleccionado=None):
    """Función principal que llama a todas las demás funciones de dibujo."""
    dibujar_tablero(screen)
    dibujar_fichas(screen, game, punto_seleccionado)
    dibujar_footer(screen, game, mensaje)
