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

# Variables para interactividad
ficha_seleccionada = None  # Para saber qué ficha está seleccionada
mouse_x, mouse_y = 0, 0    # Posición del mouse

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Detectar clics del mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Función para verificar si se hizo clic en una ficha
            def clic_en_ficha(ficha_x, ficha_y, nombre_ficha):
                global ficha_seleccionada
                if ((mouse_x - ficha_x)**2 + (mouse_y - ficha_y)**2) <= 15**2:
                    ficha_seleccionada = nombre_ficha
                    return True
                return False
            
            # Verificar todas las fichas
            ficha_encontrada = False
            
            # Fichas blancas punto 24
            punto24_x = 410 + 5 * 50 + 25
            punto24_y = 70
            if clic_en_ficha(punto24_x, punto24_y, "blanca_24_1"): ficha_encontrada = True
            if clic_en_ficha(punto24_x, punto24_y + 30, "blanca_24_2"): ficha_encontrada = True
            
            # Fichas blancas punto 13
            punto13_x = 60 + 0 * 50 + 25
            punto13_y = 70
            for i in range(5):
                if clic_en_ficha(punto13_x, punto13_y + i * 25, f"blanca_13_{i+1}"): 
                    ficha_encontrada = True
            
            # Fichas blancas punto 8 (corregido)
            punto8_x = 60 + 4 * 50 + 25
            punto8_y = 430
            for i in range(3):
                if clic_en_ficha(punto8_x, punto8_y - i * 25, f"blanca_8_{i+1}"): 
                    ficha_encontrada = True
            
            # Fichas blancas punto 6 (corregido)
            punto6_x = 410 + 0 * 50 + 25
            punto6_y = 430
            for i in range(5):
                if clic_en_ficha(punto6_x, punto6_y - i * 25, f"blanca_6_{i+1}"): 
                    ficha_encontrada = True
            
            # Fichas negras punto 1
            punto1_x = punto24_x
            punto1_y = 430
            if clic_en_ficha(punto1_x, punto1_y, "negra_1_1"): ficha_encontrada = True
            if clic_en_ficha(punto1_x, punto1_y - 30, "negra_1_2"): ficha_encontrada = True
            
            # Fichas negras punto 12
            punto12_x = punto13_x
            punto12_y = 430
            for i in range(5):
                if clic_en_ficha(punto12_x, punto12_y - i * 25, f"negra_12_{i+1}"): 
                    ficha_encontrada = True
            
            # Fichas negras punto 17 (corregido)
            punto17_x = 410 + 2 * 50 + 25
            punto17_y = 70
            for i in range(3):
                if clic_en_ficha(punto17_x, punto17_y + i * 25, f"negra_17_{i+1}"): 
                    ficha_encontrada = True
            
            # Fichas negras punto 19 (corregido)
            punto19_x = 410 + 0 * 50 + 25
            punto19_y = 70
            for i in range(5):
                if clic_en_ficha(punto19_x, punto19_y + i * 25, f"negra_19_{i+1}"): 
                    ficha_encontrada = True
            
            # Si no se encontró ninguna ficha, deseleccionar
            if not ficha_encontrada:
                ficha_seleccionada = None
    
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
    
    # Función para dibujar una ficha
    def dibujar_ficha(x, y, color_ficha, nombre_ficha):
        color_borde = (255, 0, 0) if ficha_seleccionada == nombre_ficha else BLACK
        borde_grosor = 4 if ficha_seleccionada == nombre_ficha else 2
        pygame.draw.circle(screen, color_ficha, (x, y), ficha_radio)
        pygame.draw.circle(screen, color_borde, (x, y), ficha_radio, borde_grosor)
    
    # Configuración inicial de backgammon según las reglas
    # Fichas blancas: punto 24 (2), punto 13 (5), punto 8 (3), punto 6 (5)
    # Fichas negras: punto 1 (2), punto 12 (5), punto 17 (3), punto 19 (5)
    
    # FICHAS BLANCAS
    # Punto 24 (2 fichas blancas) - triángulo superior izquierdo último
    punto24_x = lado_izquierdo_x + 5 * triangle_width + triangle_width//2
    punto24_y = 70
    dibujar_ficha(punto24_x, punto24_y, FICHA_BLANCA, "blanca_24_1")
    dibujar_ficha(punto24_x, punto24_y + 30, FICHA_BLANCA, "blanca_24_2")
    
    # Punto 13 (5 fichas blancas) - triángulo superior derecho primero
    punto13_x = start_x + 0 * triangle_width + triangle_width//2
    punto13_y = 70
    for i in range(5):
        dibujar_ficha(punto13_x, punto13_y + i * 25, FICHA_BLANCA, f"blanca_13_{i+1}")
    
    # Punto 8 (3 fichas blancas) - triángulo inferior derecho (8=12-4, índice 4)
    punto8_x = start_x + 4 * triangle_width + triangle_width//2
    punto8_y = 430
    for i in range(3):
        dibujar_ficha(punto8_x, punto8_y - i * 25, FICHA_BLANCA, f"blanca_8_{i+1}")
    
    # Punto 6 (5 fichas blancas) - triángulo inferior izquierdo (6=6-0, índice 0) 
    punto6_x = lado_izquierdo_x + 0 * triangle_width + triangle_width//2
    punto6_y = 430
    for i in range(5):
        dibujar_ficha(punto6_x, punto6_y - i * 25, FICHA_BLANCA, f"blanca_6_{i+1}")
    
    # FICHAS NEGRAS
    # Punto 1 (2 fichas negras) - triángulo inferior izquierdo último
    punto1_x = lado_izquierdo_x + 5 * triangle_width + triangle_width//2
    punto1_y = 430
    dibujar_ficha(punto1_x, punto1_y, FICHA_NEGRA, "negra_1_1")
    dibujar_ficha(punto1_x, punto1_y - 30, FICHA_NEGRA, "negra_1_2")
    
    # Punto 12 (5 fichas negras) - triángulo inferior derecho primero
    punto12_x = start_x + 0 * triangle_width + triangle_width//2
    punto12_y = 430
    for i in range(5):
        dibujar_ficha(punto12_x, punto12_y - i * 25, FICHA_NEGRA, f"negra_12_{i+1}")
    
    # Punto 17 (3 fichas negras) - triángulo superior izquierdo (17=19-2, índice 2)
    punto17_x = lado_izquierdo_x + 2 * triangle_width + triangle_width//2
    punto17_y = 70
    for i in range(3):
        dibujar_ficha(punto17_x, punto17_y + i * 25, FICHA_NEGRA, f"negra_17_{i+1}")
    
    # Punto 19 (5 fichas negras) - triángulo superior izquierdo (19=19-0, índice 0)
    punto19_x = lado_izquierdo_x + 0 * triangle_width + triangle_width//2
    punto19_y = 70
    for i in range(5):
        dibujar_ficha(punto19_x, punto19_y + i * 25, FICHA_NEGRA, f"negra_19_{i+1}")
    
    # Información del juego
    info_x = 50
    info_y = 480
    
    # Mostrar turno actual
    turno_text = font.render("Turno: Jugador 1", True, BLACK)
    screen.blit(turno_text, (info_x, info_y))
    
    # Mostrar dados
    dados_text = font.render("Dados: 3, 5", True, BLACK)
    screen.blit(dados_text, (info_x + 220, info_y))
    
    # Instrucciones - texto más corto y mejor posicionado
    if ficha_seleccionada:
        # Extraer info básica de la ficha (ej: "blanca_13_2" -> "Blanca P13")
        partes = ficha_seleccionada.split("_")
        color = partes[0].capitalize()
        punto = partes[1]
        instrucciones_text = font.render(f"Seleccionada: {color} P{punto}", True, BLACK)
    else:
        instrucciones_text = font.render("Clic para seleccionar ficha", True, BLACK)
    screen.blit(instrucciones_text, (info_x + 380, info_y))
    
    # Actualizar pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()