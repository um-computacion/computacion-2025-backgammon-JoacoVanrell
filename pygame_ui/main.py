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
    
    # Actualizar pantalla
    pygame.display.flip()


pygame.quit()
sys.exit()