#!/usr/bin/env python3
"""
Interfaz principal para el juego de Backgammon usando Pygame
Estructura profesional basada en el ejemplo del profesor
Arquitectura modular con separación clara de responsabilidades
"""

import pygame
import sys

# Importar nuestros módulos
from constants import *
from board_renderer import BoardRenderer
from event_handler import EventHandler
from game_state import GameState


class BackgammonGame:
    """
    Clase principal del juego de Backgammon
    Coordina todos los componentes siguiendo el patrón del profesor
    """
    
    def __init__(self):
        # Inicializar pygame
        pygame.init()
        
        # Configurar pantalla
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Backgammon - Estructura Profesional")
        
        # Configurar reloj para FPS
        self.clock = pygame.time.Clock()
        
        # Configurar fuentes
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.small_font = pygame.font.Font(None, SMALL_FONT_SIZE)
        
        # Inicializar componentes
        self.game_state = GameState()
        self.board_renderer = BoardRenderer()
        self.event_handler = EventHandler()
        
        # Variables de estado
        self.hitmap = {}
    
    def _render_ui_info(self):
        """Renderiza información del juego en la parte superior"""
        info = self.game_state.get_game_info()
        
        # Información del jugador actual
        player_text = f"Turno: Jugador {info['current_player'].capitalize()}"
        text_surface = self.font.render(player_text, True, TEXT_COLOR)
        self.screen.blit(text_surface, (20, 10))
        
        # Información de dados
        if info['dice_values']:
            dice_text = f"Dados: {info['dice_values'][0]}, {info['dice_values'][1]}"
            if info['moves_remaining'] > 0:
                dice_text += f" (Movimientos: {info['moves_remaining']})"
        else:
            dice_text = "Presiona ESPACIO para lanzar dados"
        
        text_surface = self.font.render(dice_text, True, TEXT_COLOR)
        self.screen.blit(text_surface, (300, 10))
        
        # Información de selección
        selected = self.event_handler.get_selected_point()
        if selected:
            checkers = self.game_state.get_checkers_at_point(selected)
            if checkers:
                color = checkers[0]
                count = len(checkers)
                selection_text = f"Punto {selected}: {count} ficha(s) {color}"
            else:
                selection_text = f"Punto {selected}: vacío"
        else:
            selection_text = "Haz clic en una ficha para seleccionar"
        
        text_surface = self.small_font.render(selection_text, True, TEXT_COLOR)
        self.screen.blit(text_surface, (20, SCREEN_HEIGHT - 30))
    
    def _render_help(self):
        """Renderiza ayuda en la parte inferior"""
        help_texts = [
            "ESPACIO: Lanzar dados",
            "ESC/Q: Salir",
            "R: Reiniciar",
            "H: Ayuda"
        ]
        
        x_offset = 20
        y_position = SCREEN_HEIGHT - 60
        
        for text in help_texts:
            text_surface = self.small_font.render(text, True, TEXT_COLOR)
            self.screen.blit(text_surface, (x_offset, y_position))
            x_offset += 150
    
    def _handle_game_actions(self, actions):
        """Procesa las acciones generadas por el event handler"""
        for action in actions:
            if action['action'] == 'quit':
                return False
            
            elif action['action'] == 'select':
                point = action['point']
                self.board_renderer.set_selected_point(point)
                print(f"Punto seleccionado: {point}")
                
                # Mostrar información de las fichas en el punto
                checkers = self.game_state.get_checkers_at_point(point)
                if checkers:
                    print(f"  - {len(checkers)} ficha(s) {checkers[0]}")
            
            elif action['action'] == 'deselect':
                self.board_renderer.set_selected_point(None)
                print("Punto deseleccionado")
            
            elif action['action'] == 'roll_dice':
                dice = self.game_state.roll_dice()
                print(f"Dados lanzados: {dice}")
            
            elif action['action'] == 'reset_game':
                self.game_state.reset_game()
                self.board_renderer.set_selected_point(None)
                self.event_handler.reset_selection()
                print("Juego reiniciado")
            
            elif action['action'] == 'show_help':
                print("=== AYUDA ===")
                print("ESPACIO: Lanzar dados")
                print("Clic: Seleccionar ficha")
                print("ESC/Q: Salir")
                print("R: Reiniciar juego")
        
        return True
    
    def run(self):
        """Bucle principal del juego"""
        print("=== Backgammon - Iniciando ===")
        print("Estructura profesional basada en el ejemplo del profesor")
        print("Presiona H para ver la ayuda completa")
        
        while self.event_handler.is_running():
            # Procesar eventos
            actions = self.event_handler.process_events(self.hitmap)
            if not self._handle_game_actions(actions):
                break
            
            # Renderizar tablero
            self.hitmap = self.board_renderer.render_board(
                self.screen, 
                self.game_state, 
                self.font
            )
            
            # Renderizar UI
            self._render_ui_info()
            self._render_help()
            
            # Actualizar pantalla
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        # Limpiar y salir
        pygame.quit()
        sys.exit()


def main():
    """Función principal - punto de entrada del programa"""
    try:
        game = BackgammonGame()
        game.run()
    except Exception as e:
        print(f"Error durante la ejecución: {e}")
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    main()