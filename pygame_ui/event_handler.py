"""
Manejador de eventos para la interfaz pygame de Backgammon
Basado en la estructura del profesor - separación de responsabilidades
"""

import pygame
from constants import *


class EventHandler:
    """
    Clase responsable de manejar todos los eventos de pygame
    Sigue el patrón del profesor: cada clase tiene una responsabilidad específica
    """
    
    def __init__(self):
        self.running = True
        self.selected_point = None
        self.last_click_pos = None
    
    def is_running(self):
        """Retorna si la aplicación debe seguir ejecutándose"""
        return self.running
    
    def get_selected_point(self):
        """Retorna el punto actualmente seleccionado"""
        return self.selected_point
    
    def _hit_test(self, hitmap, pos):
        """
        Detecta si un clic intersecta con alguna ficha
        Retorna el número del punto o None
        """
        click_x, click_y = pos
        
        for point_number, checkers in hitmap.items():
            for checker_x, checker_y, radius in checkers:
                # Calcular distancia del clic al centro de la ficha
                distance_squared = (click_x - checker_x) ** 2 + (click_y - checker_y) ** 2
                if distance_squared <= radius ** 2:
                    return point_number
        
        return None
    
    def handle_mouse_click(self, pos, hitmap):
        """
        Maneja clics del mouse en el tablero
        pos: posición del clic (x, y)
        hitmap: mapa de posiciones de fichas para detección de colisiones
        """
        self.last_click_pos = pos
        clicked_point = self._hit_test(hitmap, pos)
        
        if clicked_point is not None:
            if self.selected_point == clicked_point:
                # Clic en el mismo punto: deseleccionar
                self.selected_point = None
                return {'action': 'deselect', 'point': clicked_point}
            else:
                # Clic en punto diferente: seleccionar nuevo
                old_selection = self.selected_point
                self.selected_point = clicked_point
                return {
                    'action': 'select', 
                    'point': clicked_point, 
                    'previous': old_selection
                }
        else:
            # Clic en área vacía: deseleccionar
            if self.selected_point is not None:
                old_selection = self.selected_point
                self.selected_point = None
                return {'action': 'deselect', 'point': old_selection}
        
        return {'action': 'none'}
    
    def handle_keyboard(self, key):
        """
        Maneja eventos de teclado
        key: tecla presionada
        """
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            self.running = False
            return {'action': 'quit'}
        
        elif key == pygame.K_SPACE:
            return {'action': 'roll_dice'}
        
        elif key == pygame.K_r:
            return {'action': 'reset_game'}
        
        elif key == pygame.K_h:
            return {'action': 'show_help'}
        
        return {'action': 'none'}
    
    def process_events(self, hitmap=None):
        """
        Procesa todos los eventos pendientes de pygame
        Retorna una lista de acciones a realizar
        """
        actions = []
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                actions.append({'action': 'quit'})
            
            elif event.type == pygame.KEYDOWN:
                action = self.handle_keyboard(event.key)
                if action['action'] != 'none':
                    actions.append(action)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and hitmap is not None:  # Clic izquierdo
                    action = self.handle_mouse_click(event.pos, hitmap)
                    if action['action'] != 'none':
                        actions.append(action)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # Clic derecho
                    actions.append({'action': 'right_click', 'pos': event.pos})
        
        return actions
    
    def reset_selection(self):
        """Limpia la selección actual"""
        self.selected_point = None