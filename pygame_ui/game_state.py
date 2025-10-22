"""
Estado del juego para la interfaz pygame de Backgammon
Basado en la estructura del profesor - manejo de estado separado
"""

from constants import INITIAL_SETUP
import random


class EstadoJuego:
    """
    Clase que mantiene el estado actual del juego
    Actúa como intermediario entre la lógica del juego y la interfaz
    """
    
    def __init__(self):
        self.puntos = {i: [] for i in range(1, 25)}  # Puntos 1-24
        self.jugador_actual = 'white'
        self.valores_dados = []
        self.movimientos_restantes = []
        self.fase_juego = 'inicial'  # 'inicial', 'jugando', 'sacando_fichas', 'terminado'
        
        # Configurar posición inicial
        self._configurar_posicion_inicial()
    
    def _configurar_posicion_inicial(self):
        """Configura la posición inicial del backgammon"""
        for punto, (color, cantidad) in INITIAL_SETUP.items():
            self.puntos[punto] = [color] * cantidad
    
    def get_checkers_at_point(self, numero_punto):
        """Retorna las fichas en un punto específico"""
        if 1 <= numero_punto <= 24:
            return self.puntos[numero_punto]
        return []
    
    def obtener_jugador_actual(self):
        """Retorna el jugador actual"""
        return self.jugador_actual
    
    def obtener_valores_dados(self):
        """Retorna los valores actuales de los dados"""
        return self.valores_dados.copy()
    
    def obtener_movimientos_restantes(self):
        """Retorna los movimientos pendientes"""
        return self.movimientos_restantes.copy()
    
    def tirar_dados(self):
        """Simula lanzar los dados"""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        self.valores_dados = [dado1, dado2]
        
        if dado1 == dado2:
            # Dobles: cuatro movimientos
            self.movimientos_restantes = [dado1, dado1, dado1, dado1]
        else:
            # Movimientos normales
            self.movimientos_restantes = [dado1, dado2]
        
        return self.valores_dados
    
    def can_move_checker(self, from_point, to_point):
        """
        Verifica si se puede mover una ficha de un punto a otro
        Esta es una versión simplificada - en el juego real habría más validaciones
        """
        # Verificar que hay fichas en el punto origen
        if not self.points[from_point]:
            return False
        
        # Verificar que la ficha pertenece al jugador actual
        if self.points[from_point][0] != self.current_player:
            return False
        
        # Verificar que el punto destino es válido
        if not (1 <= to_point <= 24):
            return False
        
        # Verificar que hay movimientos disponibles
        move_distance = abs(to_point - from_point)
        if move_distance not in self.moves_remaining:
            return False
        
        # Verificar que el punto destino no está bloqueado por el oponente
        target_checkers = self.points[to_point]
        if target_checkers and target_checkers[0] != self.current_player and len(target_checkers) > 1:
            return False
        
        return True
    
    def intentar_movimiento(self, desde_punto, hasta_punto):
        """Intenta realizar un movimiento en el tablero"""
        if not self.movimientos_restantes:
            return False, "No hay movimientos restantes"
        
        # Verificar que el movimiento sea válido
        distancia = abs(hasta_punto - desde_punto)
        if distancia not in self.movimientos_restantes:
            return False, "Movimiento no válido con los dados actuales"
        
        # Verificar que haya fichas en el punto de origen
        fichas_origen = self.puntos[desde_punto]
        if not fichas_origen or fichas_origen[0] != self.jugador_actual:
            return False, "No hay fichas tuyas en ese punto"
        
        # Verificar que el punto destino sea válido
        fichas_destino = self.puntos[hasta_punto]
        if fichas_destino and fichas_destino[0] != self.jugador_actual and len(fichas_destino) > 1:
            return False, "El punto destino está bloqueado"
        
        # Realizar el movimiento
        self._realizar_movimiento(desde_punto, hasta_punto, distancia)
        return True, "Movimiento exitoso"
    
    def _realizar_movimiento(self, desde_punto, hasta_punto, distancia):
        """Ejecuta un movimiento válido"""
        # Remover ficha del punto origen
        self.puntos[desde_punto].pop()
        
        # Agregar ficha al punto destino
        if hasta_punto not in self.puntos:
            self.puntos[hasta_punto] = []
        
        fichas_destino = self.puntos[hasta_punto]
        
        # Si hay una ficha del oponente, la capturamos
        if fichas_destino and fichas_destino[0] != self.jugador_actual:
            ficha_capturada = fichas_destino.pop()
            # Aquí se podría manejar la captura (enviar a la barra)
        
        self.puntos[hasta_punto].append(self.jugador_actual)
        
        # Remover el movimiento usado
        self.movimientos_restantes.remove(distancia)
        
        # Si no quedan movimientos, cambiar de jugador
        if not self.movimientos_restantes:
            self.cambiar_jugador()
    
    def cambiar_jugador(self):
        """Cambia al siguiente jugador"""
        self.jugador_actual = 2 if self.jugador_actual == 1 else 1
        self.valores_dados = []
        self.movimientos_restantes = []
    
    def obtener_info_juego(self):
        """Retorna información completa del estado del juego"""
        return {
            'jugador_actual': self.jugador_actual,
            'valores_dados': self.valores_dados,
            'movimientos_restantes': len(self.movimientos_restantes),
            'puntos': self.puntos.copy()
        }
    
    def reiniciar_juego(self):
        """Reinicia el juego a su estado inicial"""
        self.__init__()
    
    def switch_player(self):
        """Cambia al siguiente jugador"""
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        self.dice_values = []
        self.moves_remaining = []
    
    def reset_game(self):
        """Reinicia el juego a la posición inicial"""
        self.points = {i: [] for i in range(1, 25)}
        self.current_player = 'white'
        self.dice_values = []
        self.moves_remaining = []
        self.game_phase = 'initial'
        self._setup_initial_position()
    
    def get_game_info(self):
        """Retorna información resumida del estado del juego"""
        return {
            'current_player': self.current_player,
            'dice_values': self.dice_values,
            'moves_remaining': len(self.moves_remaining),
            'game_phase': self.game_phase
        }