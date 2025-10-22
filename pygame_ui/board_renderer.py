"""
Renderizador del tablero de Backgammon
Basado en la estructura del profesor - separación clara de responsabilidades
"""

import pygame
from constants import *


class RenderizadorTablero:
    """
    Clase responsable de renderizar el tablero de Backgammon
    Sigue el patrón del profesor: una clase específica para cada responsabilidad
    """
    
    def __init__(self):
        self.punto_seleccionado = None
        self.rectangulo_tablero = None
        self.mapa_clics = {}  # Para detección de clics
    
    def establecer_punto_seleccionado(self, numero_punto):
        """Establece el punto seleccionado para highlighting"""
        self.punto_seleccionado = numero_punto
    
    def obtener_rectangulo_tablero(self):
        """Retorna el rectángulo del tablero para otros componentes"""
        return self.rectangulo_tablero
    
    def obtener_mapa_clics(self):
        """Retorna el mapa de clics para detección de clics"""
        return self.mapa_clics
    
    def _punto_a_posicion_visual(self, numero_punto):
        """
        Convierte número de punto (1-24) a posición visual
        Retorna: (fila, columna) donde fila es 'superior'|'inferior' y columna es 0-11
        """
        if 1 <= numero_punto <= 12:
            # Puntos 1-12: fila inferior, de derecha a izquierda
            return 'inferior', 12 - numero_punto
        elif 13 <= numero_punto <= 24:
            # Puntos 13-24: fila superior, de izquierda a derecha
            return 'superior', numero_punto - 13
        else:
            return None, None
    
    def _dibujar_triangulo(self, superficie, columna, fila, color):
        """Dibuja un triángulo en la posición especificada"""
        if not self.rectangulo_tablero:
            return
            
        x_inicio = self.rectangulo_tablero.left + columna * TRIANGLE_WIDTH
        x_fin = x_inicio + TRIANGLE_WIDTH
        x_centro = x_inicio + TRIANGLE_WIDTH / 2
        
        if fila == 'superior':
            # Triángulo apuntando hacia abajo
            punta_y = self.rectangulo_tablero.top + self.rectangulo_tablero.height * 0.4
            puntos = [
                (x_inicio, self.rectangulo_tablero.top),
                (x_fin, self.rectangulo_tablero.top),
                (x_centro, punta_y)
            ]
        else:
            # Triángulo apuntando hacia arriba
            punta_y = self.rectangulo_tablero.bottom - self.rectangulo_tablero.height * 0.4
            puntos = [
                (x_inicio, self.rectangulo_tablero.bottom),
                (x_fin, self.rectangulo_tablero.bottom),
                (x_centro, punta_y)
            ]
        
        pygame.draw.polygon(superficie, color, puntos)
        pygame.draw.polygon(superficie, LINE_COLOR, puntos, 2)
    
    def _dibujar_ficha(self, superficie, centro_x, centro_y, color, esta_seleccionada=False, cantidad_pila=None):
        """Dibuja una ficha individual"""
        # Color de la ficha
        color_ficha = WHITE_CHECKER if color == 'white' else BLACK_CHECKER
        
        # Dibujar círculo principal
        pygame.draw.circle(superficie, color_ficha, (int(centro_x), int(centro_y)), CHECKER_RADIUS)
        
        # Borde (rojo si está seleccionada)
        color_borde = SELECTED_COLOR if esta_seleccionada else LINE_COLOR
        grosor_borde = 3 if esta_seleccionada else 1
        pygame.draw.circle(superficie, color_borde, (int(centro_x), int(centro_y)), CHECKER_RADIUS, grosor_borde)
        
        # Mostrar número si hay muchas fichas apiladas
        if cantidad_pila and cantidad_pila > MAX_VISIBLE_CHECKERS:
            fuente = pygame.font.Font(None, 16)
            color_texto = LINE_COLOR if color == 'white' else WHITE_CHECKER
            texto = fuente.render(str(cantidad_pila), True, color_texto)
            rectangulo_texto = texto.get_rect(center=(int(centro_x), int(centro_y)))
            superficie.blit(texto, rectangulo_texto)
    
    def _calcular_posiciones_fichas(self, numero_punto, cantidad_fichas):
        """Calcula las posiciones de las fichas en un punto"""
        if not self.rectangulo_tablero:
            return []
        
        fila, columna = self._punto_a_posicion_visual(numero_punto)
        if fila is None:
            return []
        
        # Centro horizontal del triángulo
        centro_x = self.rectangulo_tablero.left + columna * TRIANGLE_WIDTH + TRIANGLE_WIDTH / 2
        
        # Posiciones verticales
        posiciones = []
        fichas_visibles = min(cantidad_fichas, MAX_VISIBLE_CHECKERS)
        
        if fila == 'superior':
            # Fichas van hacia abajo desde la parte superior
            inicio_y = self.rectangulo_tablero.top + CHECKER_RADIUS + 10
            for i in range(fichas_visibles):
                y = inicio_y + i * (CHECKER_RADIUS * 2 + CHECKER_STACK_GAP)
                posiciones.append((centro_x, y))
        else:
            # Fichas van hacia arriba desde la parte inferior
            inicio_y = self.rectangulo_tablero.bottom - CHECKER_RADIUS - 10
            for i in range(fichas_visibles):
                y = inicio_y - i * (CHECKER_RADIUS * 2 + CHECKER_STACK_GAP)
                posiciones.append((centro_x, y))
        
        return posiciones
    
    def _dibujar_etiquetas_puntos(self, superficie, fuente):
        """Dibuja las etiquetas de los puntos (números 1-24)"""
        if not self.rectangulo_tablero:
            return
        
        # Etiquetas superiores (puntos 13-24)
        for columna in range(12):
            numero_punto = columna + 13
            x = self.rectangulo_tablero.left + columna * TRIANGLE_WIDTH + TRIANGLE_WIDTH / 2
            y = self.rectangulo_tablero.top - 20
            
            texto = fuente.render(str(numero_punto), True, TEXT_COLOR)
            rectangulo_texto = texto.get_rect(center=(int(x), int(y)))
            superficie.blit(texto, rectangulo_texto)
        
        # Etiquetas inferiores (puntos 12-1)
        for columna in range(12):
            numero_punto = 12 - columna
            x = self.rectangulo_tablero.left + columna * TRIANGLE_WIDTH + TRIANGLE_WIDTH / 2
            y = self.rectangulo_tablero.bottom + 20
            
            texto = fuente.render(str(numero_punto), True, TEXT_COLOR)
            rectangulo_texto = texto.get_rect(center=(int(x), int(y)))
            superficie.blit(texto, rectangulo_texto)
    
    def renderizar_tablero(self, superficie, estado_juego, fuente):
        """
        Método principal para renderizar el tablero completo
        estado_juego: objeto que contiene el estado actual del juego
        """
        # Limpiar pantalla
        superficie.fill(BACKGROUND_COLOR)
        
        # Establecer rectángulo del tablero
        self.rectangulo_tablero = pygame.Rect(
            MARGIN, 
            MARGIN + 30, 
            BOARD_WIDTH, 
            BOARD_HEIGHT
        )
        
        # Dibujar marco del tablero
        pygame.draw.rect(superficie, BOARD_COLOR, self.rectangulo_tablero, border_radius=10)
        pygame.draw.rect(superficie, LINE_COLOR, self.rectangulo_tablero, 3, border_radius=10)
        
        # Dibujar triángulos alternados
        for columna in range(12):
            # Triángulos superiores
            color_superior = TRIANGLE_COLOR_A if columna % 2 == 0 else TRIANGLE_COLOR_B
            self._dibujar_triangulo(superficie, columna, 'superior', color_superior)
            
            # Triángulos inferiores (colores invertidos)
            color_inferior = TRIANGLE_COLOR_B if columna % 2 == 0 else TRIANGLE_COLOR_A
            self._dibujar_triangulo(superficie, columna, 'inferior', color_inferior)
        
        # Línea central del tablero
        centro_y = self.rectangulo_tablero.centery
        pygame.draw.line(superficie, LINE_COLOR, 
                        (self.rectangulo_tablero.left, centro_y), 
                        (self.rectangulo_tablero.right, centro_y), 2)
        
        # Dibujar etiquetas de puntos
        self._dibujar_etiquetas_puntos(superficie, fuente)
        
        # Limpiar mapa de clics
        self.mapa_clics = {i: [] for i in range(1, 25)}
        
        # Dibujar fichas usando el estado del juego
        for numero_punto in range(1, 25):
            fichas = estado_juego.get_checkers_at_point(numero_punto)
            if not fichas:
                continue
            
            cantidad_fichas = len(fichas)
            color_ficha = fichas[0]  # Asumimos que todas las fichas en un punto son del mismo color
            
            posiciones = self._calcular_posiciones_fichas(numero_punto, cantidad_fichas)
            esta_seleccionada = (self.punto_seleccionado == numero_punto)
            
            for i, (x, y) in enumerate(posiciones):
                # Mostrar número total en la última ficha visible si hay más fichas
                mostrar_pila = cantidad_fichas if (i == len(posiciones) - 1 and cantidad_fichas > MAX_VISIBLE_CHECKERS) else None
                
                self._dibujar_ficha(superficie, x, y, color_ficha, esta_seleccionada, mostrar_pila)
                
                # Agregar al mapa de clics para detección de clics
                self.mapa_clics[numero_punto].append((int(x), int(y), CHECKER_RADIUS))
        
        return self.mapa_clics