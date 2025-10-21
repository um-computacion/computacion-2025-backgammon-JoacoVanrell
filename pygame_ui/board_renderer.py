"""
Renderizador del tablero de Backgammon
Basado en la estructura del profesor - separación clara de responsabilidades
"""

import pygame
from constants import *


class BoardRenderer:
    """
    Clase responsable de renderizar el tablero de Backgammon
    Sigue el patrón del profesor: una clase específica para cada responsabilidad
    """
    
    def __init__(self):
        self.selected_point = None
        self.board_rect = None
        self.hitmap = {}  # Para detección de clics
    
    def set_selected_point(self, point_number):
        """Establece el punto seleccionado para highlighting"""
        self.selected_point = point_number
    
    def get_board_rect(self):
        """Retorna el rectángulo del tablero para otros componentes"""
        return self.board_rect
    
    def get_hitmap(self):
        """Retorna el hitmap para detección de clics"""
        return self.hitmap
    
    def _point_to_visual_position(self, point_number):
        """
        Convierte número de punto (1-24) a posición visual
        Retorna: (row, column) donde row es 'top'|'bottom' y column es 0-11
        """
        if 1 <= point_number <= 12:
            # Puntos 1-12: fila inferior, de derecha a izquierda
            return 'bottom', 12 - point_number
        elif 13 <= point_number <= 24:
            # Puntos 13-24: fila superior, de izquierda a derecha
            return 'top', point_number - 13
        else:
            return None, None
    
    def _draw_triangle(self, surface, column, row, color):
        """Dibuja un triángulo en la posición especificada"""
        if not self.board_rect:
            return
            
        x_start = self.board_rect.left + column * TRIANGLE_WIDTH
        x_end = x_start + TRIANGLE_WIDTH
        x_center = x_start + TRIANGLE_WIDTH / 2
        
        if row == 'top':
            # Triángulo apuntando hacia abajo
            tip_y = self.board_rect.top + self.board_rect.height * 0.4
            points = [
                (x_start, self.board_rect.top),
                (x_end, self.board_rect.top),
                (x_center, tip_y)
            ]
        else:
            # Triángulo apuntando hacia arriba
            tip_y = self.board_rect.bottom - self.board_rect.height * 0.4
            points = [
                (x_start, self.board_rect.bottom),
                (x_end, self.board_rect.bottom),
                (x_center, tip_y)
            ]
        
        pygame.draw.polygon(surface, color, points)
        pygame.draw.polygon(surface, LINE_COLOR, points, 2)
    
    def _draw_checker(self, surface, center_x, center_y, color, is_selected=False, stack_count=None):
        """Dibuja una ficha individual"""
        # Color de la ficha
        checker_color = WHITE_CHECKER if color == 'white' else BLACK_CHECKER
        
        # Dibujar círculo principal
        pygame.draw.circle(surface, checker_color, (int(center_x), int(center_y)), CHECKER_RADIUS)
        
        # Borde (rojo si está seleccionada)
        border_color = SELECTED_COLOR if is_selected else LINE_COLOR
        border_width = 3 if is_selected else 1
        pygame.draw.circle(surface, border_color, (int(center_x), int(center_y)), CHECKER_RADIUS, border_width)
        
        # Mostrar número si hay muchas fichas apiladas
        if stack_count and stack_count > MAX_VISIBLE_CHECKERS:
            font = pygame.font.Font(None, 16)
            text_color = LINE_COLOR if color == 'white' else WHITE_CHECKER
            text = font.render(str(stack_count), True, text_color)
            text_rect = text.get_rect(center=(int(center_x), int(center_y)))
            surface.blit(text, text_rect)
    
    def _calculate_checker_positions(self, point_number, checker_count):
        """Calcula las posiciones de las fichas en un punto"""
        if not self.board_rect:
            return []
        
        row, column = self._point_to_visual_position(point_number)
        if row is None:
            return []
        
        # Centro horizontal del triángulo
        center_x = self.board_rect.left + column * TRIANGLE_WIDTH + TRIANGLE_WIDTH / 2
        
        # Posiciones verticales
        positions = []
        visible_count = min(checker_count, MAX_VISIBLE_CHECKERS)
        
        if row == 'top':
            # Fichas van hacia abajo desde la parte superior
            start_y = self.board_rect.top + CHECKER_RADIUS + 10
            for i in range(visible_count):
                y = start_y + i * (CHECKER_RADIUS * 2 + CHECKER_STACK_GAP)
                positions.append((center_x, y))
        else:
            # Fichas van hacia arriba desde la parte inferior
            start_y = self.board_rect.bottom - CHECKER_RADIUS - 10
            for i in range(visible_count):
                y = start_y - i * (CHECKER_RADIUS * 2 + CHECKER_STACK_GAP)
                positions.append((center_x, y))
        
        return positions
    
    def _draw_point_labels(self, surface, font):
        """Dibuja las etiquetas de los puntos (números 1-24)"""
        if not self.board_rect:
            return
        
        # Etiquetas superiores (puntos 13-24)
        for column in range(12):
            point_number = column + 13
            x = self.board_rect.left + column * TRIANGLE_WIDTH + TRIANGLE_WIDTH / 2
            y = self.board_rect.top - 20
            
            text = font.render(str(point_number), True, TEXT_COLOR)
            text_rect = text.get_rect(center=(int(x), int(y)))
            surface.blit(text, text_rect)
        
        # Etiquetas inferiores (puntos 12-1)
        for column in range(12):
            point_number = 12 - column
            x = self.board_rect.left + column * TRIANGLE_WIDTH + TRIANGLE_WIDTH / 2
            y = self.board_rect.bottom + 20
            
            text = font.render(str(point_number), True, TEXT_COLOR)
            text_rect = text.get_rect(center=(int(x), int(y)))
            surface.blit(text, text_rect)
    
    def render_board(self, surface, game_state, font):
        """
        Método principal para renderizar el tablero completo
        game_state: objeto que contiene el estado actual del juego
        """
        # Limpiar pantalla
        surface.fill(BACKGROUND_COLOR)
        
        # Establecer rectángulo del tablero
        self.board_rect = pygame.Rect(
            MARGIN, 
            MARGIN + 30, 
            BOARD_WIDTH, 
            BOARD_HEIGHT
        )
        
        # Dibujar marco del tablero
        pygame.draw.rect(surface, BOARD_COLOR, self.board_rect, border_radius=10)
        pygame.draw.rect(surface, LINE_COLOR, self.board_rect, 3, border_radius=10)
        
        # Dibujar triángulos alternados
        for column in range(12):
            # Triángulos superiores
            color_top = TRIANGLE_COLOR_A if column % 2 == 0 else TRIANGLE_COLOR_B
            self._draw_triangle(surface, column, 'top', color_top)
            
            # Triángulos inferiores (colores invertidos)
            color_bottom = TRIANGLE_COLOR_B if column % 2 == 0 else TRIANGLE_COLOR_A
            self._draw_triangle(surface, column, 'bottom', color_bottom)
        
        # Línea central del tablero
        center_y = self.board_rect.centery
        pygame.draw.line(surface, LINE_COLOR, 
                        (self.board_rect.left, center_y), 
                        (self.board_rect.right, center_y), 2)
        
        # Dibujar etiquetas de puntos
        self._draw_point_labels(surface, font)
        
        # Limpiar hitmap
        self.hitmap = {i: [] for i in range(1, 25)}
        
        # Dibujar fichas usando el estado del juego
        for point_number in range(1, 25):
            checkers = game_state.get_checkers_at_point(point_number)
            if not checkers:
                continue
            
            checker_count = len(checkers)
            checker_color = checkers[0]  # Asumimos que todas las fichas en un punto son del mismo color
            
            positions = self._calculate_checker_positions(point_number, checker_count)
            is_selected = (self.selected_point == point_number)
            
            for i, (x, y) in enumerate(positions):
                # Mostrar número total en la última ficha visible si hay más fichas
                stack_display = checker_count if (i == len(positions) - 1 and checker_count > MAX_VISIBLE_CHECKERS) else None
                
                self._draw_checker(surface, x, y, checker_color, is_selected, stack_display)
                
                # Agregar al hitmap para detección de clics
                self.hitmap[point_number].append((int(x), int(y), CHECKER_RADIUS))
        
        return self.hitmap