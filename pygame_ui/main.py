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
from board_renderer import RenderizadorTablero
from event_handler import ManejadorEventos
from game_state import EstadoJuego


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
        self.estado_juego = EstadoJuego()
        self.renderizador_tablero = RenderizadorTablero()
        self.manejador_eventos = ManejadorEventos()
        
        # Variables de estado
        self.hitmap = {}
    
    def _render_ui_info(self):
        """Renderiza información del juego en la parte superior"""
        info = self.estado_juego.obtener_info_juego()
        
        # Información del jugador actual
        player_text = f"Turno: Jugador {info['jugador_actual'].capitalize()}"
        text_surface = self.font.render(player_text, True, TEXT_COLOR)
        self.screen.blit(text_surface, (20, 10))
        
        # Información de dados
        if info['valores_dados']:
            dice_text = f"Dados: {info['valores_dados'][0]}, {info['valores_dados'][1]}"
            if info['movimientos_restantes'] > 0:
                dice_text += f" (Movimientos: {info['movimientos_restantes']})"
        else:
            dice_text = "Presiona ESPACIO para lanzar dados"
        
        text_surface = self.font.render(dice_text, True, TEXT_COLOR)
        self.screen.blit(text_surface, (300, 10))
        
        # Información de selección
        seleccionado = self.manejador_eventos.obtener_punto_seleccionado()
        if seleccionado:
            fichas = self.estado_juego.get_checkers_at_point(seleccionado)
            if fichas:
                color = fichas[0]
                count = len(fichas)
                selection_text = f"Punto {seleccionado}: {count} ficha(s) {color}"
            else:
                selection_text = f"Punto {seleccionado}: vacío"
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
            if action['accion'] == 'salir':
                return False
            
            elif action['accion'] == 'seleccionar':
                point = action['punto']
                self.renderizador_tablero.establecer_punto_seleccionado(point)
                print(f"Punto seleccionado: {point}")
                
                # Mostrar información de las fichas en el punto
                fichas = self.estado_juego.get_checkers_at_point(point)
                if fichas:
                    print(f"  - {len(fichas)} ficha(s) {fichas[0]}")
            
            elif action['accion'] == 'deseleccionar':
                self.renderizador_tablero.establecer_punto_seleccionado(None)
                print("Punto deseleccionado")
            
            elif action['accion'] == 'tirar_dados':
                dados = self.estado_juego.tirar_dados()
                print(f"Dados lanzados: {dados}")
            
            elif action['accion'] == 'reiniciar_juego':
                self.estado_juego.reiniciar_juego()
                self.renderizador_tablero.establecer_punto_seleccionado(None)
                self.manejador_eventos.limpiar_seleccion()
                print("Juego reiniciado")
            
            elif action['accion'] == 'mostrar_ayuda':
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
        
        while self.manejador_eventos.esta_ejecutandose():
            # Procesar eventos
            acciones = self.manejador_eventos.procesar_eventos(self.hitmap)
            if not self._handle_game_actions(acciones):
                break
            
            # Renderizar tablero
            self.hitmap = self.renderizador_tablero.renderizar_tablero(
                self.screen, 
                self.estado_juego, 
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