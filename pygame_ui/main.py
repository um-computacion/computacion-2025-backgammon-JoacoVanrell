import pygame

# Inicializar pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Backgammon")

# Colores básicos
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)           # Fondo del tablero
LIGHT_TRIANGLE = (245, 222, 179)  # Beige claro para triángulos
DARK_TRIANGLE = (101, 67, 33)     # Marrón más oscuro para contraste
FICHA_BLANCA = (245, 245, 245)    # Color de las fichas blancas
FICHA_NEGRA = (60, 60, 60)        # Color de las fichas negras

# Configurar fuente para texto
font = pygame.font.Font(None, 36)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Limpiar pantalla
    screen.fill(WHITE)
    
    # Dibujar tablero (rectángulo marrón)
    tablero_rect = pygame.Rect(50, 50, 700, 400)
    pygame.draw.rect(screen, BROWN, tablero_rect)
    pygame.draw.rect(screen, BLACK, tablero_rect, 3)
    
    # Configuración de triángulos
    triangle_width = 50
    triangle_height = 120
    start_x = 60
    barra_width = 40
    lado_izquierdo_x = start_x + (6 * triangle_width) + barra_width
    
    # Triángulos superiores - lado derecho (puntos 13-18)
    for i in range(6):
        x = start_x + i * triangle_width
        color = LIGHT_TRIANGLE if i % 2 == 0 else DARK_TRIANGLE
        triangle = [(x, 50), (x + triangle_width, 50), (x + triangle_width//2, 50 + triangle_height)]
        pygame.draw.polygon(screen, color, triangle)
        pygame.draw.polygon(screen, BLACK, triangle, 2)
    
    # Triángulos superiores - lado izquierdo (puntos 19-24)
    for i in range(6):
        x = lado_izquierdo_x + i * triangle_width
        color = DARK_TRIANGLE if i % 2 == 0 else LIGHT_TRIANGLE
        triangle = [(x, 50), (x + triangle_width, 50), (x + triangle_width//2, 50 + triangle_height)]
        pygame.draw.polygon(screen, color, triangle)
        pygame.draw.polygon(screen, BLACK, triangle, 2)
    
    # Triángulos inferiores - lado derecho (puntos 12-7)
    for i in range(6):
        x = start_x + i * triangle_width
        color = DARK_TRIANGLE if i % 2 == 0 else LIGHT_TRIANGLE
        triangle = [(x, 450), (x + triangle_width, 450), (x + triangle_width//2, 450 - triangle_height)]
        pygame.draw.polygon(screen, color, triangle)
        pygame.draw.polygon(screen, BLACK, triangle, 2)
    
    # Triángulos inferiores - lado izquierdo (puntos 6-1)
    for i in range(6):
        x = lado_izquierdo_x + i * triangle_width
        color = LIGHT_TRIANGLE if i % 2 == 0 else DARK_TRIANGLE
        triangle = [(x, 450), (x + triangle_width, 450), (x + triangle_width//2, 450 - triangle_height)]
        pygame.draw.polygon(screen, color, triangle)
        pygame.draw.polygon(screen, BLACK, triangle, 2)
    
    # Dibujar barra central
    barra_x = start_x + (6 * triangle_width)
    barra_rect = pygame.Rect(barra_x, 50, barra_width, 400)
    pygame.draw.rect(screen, DARK_TRIANGLE, barra_rect)
    pygame.draw.rect(screen, BLACK, barra_rect, 2)
    
    # Dibujar fichas básicas
    ficha_radio = 15
    
    # Fichas blancas en punto 1 (triángulo inferior derecho)
    punto1_x = lado_izquierdo_x + 5 * triangle_width + triangle_width//2
    punto1_y = 430
    pygame.draw.circle(screen, FICHA_BLANCA, (punto1_x, punto1_y), ficha_radio)
    pygame.draw.circle(screen, BLACK, (punto1_x, punto1_y), ficha_radio, 2)
    pygame.draw.circle(screen, FICHA_BLANCA, (punto1_x, punto1_y - 30), ficha_radio)
    pygame.draw.circle(screen, BLACK, (punto1_x, punto1_y - 30), ficha_radio, 2)
    
    # Fichas negras en punto 24 (triángulo superior izquierdo)
    punto24_x = lado_izquierdo_x + 5 * triangle_width + triangle_width//2
    punto24_y = 70
    pygame.draw.circle(screen, FICHA_NEGRA, (punto24_x, punto24_y), ficha_radio)
    pygame.draw.circle(screen, BLACK, (punto24_x, punto24_y), ficha_radio, 2)
    pygame.draw.circle(screen, FICHA_NEGRA, (punto24_x, punto24_y + 30), ficha_radio)
    pygame.draw.circle(screen, BLACK, (punto24_x, punto24_y + 30), ficha_radio, 2)
    
    # Información del juego
    info_x = 50
    info_y = 480
    
    # Mostrar turno actual
    turno_text = font.render("Turno: Jugador 1", True, BLACK)
    screen.blit(turno_text, (info_x, info_y))
    
    # Mostrar dados
    dados_text = font.render("Dados: 3, 5", True, BLACK)
    screen.blit(dados_text, (info_x + 200, info_y))
    
    # Instrucciones
    instrucciones_text = font.render("Haz clic para mover fichas", True, BLACK)
    screen.blit(instrucciones_text, (info_x + 400, info_y))
    
    # Actualizar pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()