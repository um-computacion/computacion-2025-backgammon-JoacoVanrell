import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Backgammon")

# Colores básicos
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (160, 82, 45)

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
    
    # Dibujar algunos triángulos básicos (puntos del tablero)
    # Triángulos superiores
    triangle1 = [(100, 50), (150, 50), (125, 150)]
    triangle2 = [(150, 50), (200, 50), (175, 150)]
    pygame.draw.polygon(screen, LIGHT_BROWN, triangle1)
    pygame.draw.polygon(screen, DARK_BROWN, triangle2)
    pygame.draw.polygon(screen, BLACK, triangle1, 2)
    pygame.draw.polygon(screen, BLACK, triangle2, 2)
    
    # Actualizar pantalla
    pygame.display.flip()


pygame.quit()
sys.exit()