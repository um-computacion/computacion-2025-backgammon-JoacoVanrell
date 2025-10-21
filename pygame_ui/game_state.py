"""
Estado del juego para la interfaz pygame de Backgammon
Basado en la estructura del profesor - manejo de estado separado
"""

from constants import INITIAL_SETUP
import random


class GameState:
    """
    Clase que mantiene el estado actual del juego
    Actúa como intermediario entre la lógica del juego y la interfaz
    """
    
    def __init__(self):
        self.points = {i: [] for i in range(1, 25)}  # Puntos 1-24
        self.current_player = 'white'
        self.dice_values = []
        self.moves_remaining = []
        self.game_phase = 'initial'  # 'initial', 'playing', 'bearing_off', 'finished'
        
        # Configurar posición inicial
        self._setup_initial_position()
    
    def _setup_initial_position(self):
        """Configura la posición inicial del backgammon"""
        for point, (color, count) in INITIAL_SETUP.items():
            self.points[point] = [color] * count
    
    def get_checkers_at_point(self, point_number):
        """Retorna las fichas en un punto específico"""
        if 1 <= point_number <= 24:
            return self.points[point_number]
        return []
    
    def get_current_player(self):
        """Retorna el jugador actual"""
        return self.current_player
    
    def get_dice_values(self):
        """Retorna los valores actuales de los dados"""
        return self.dice_values.copy()
    
    def get_moves_remaining(self):
        """Retorna los movimientos pendientes"""
        return self.moves_remaining.copy()
    
    def roll_dice(self):
        """Simula lanzar los dados"""
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        self.dice_values = [die1, die2]
        
        if die1 == die2:
            # Dobles: cuatro movimientos
            self.moves_remaining = [die1, die1, die1, die1]
        else:
            # Movimientos normales
            self.moves_remaining = [die1, die2]
        
        return self.dice_values
    
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
    
    def move_checker(self, from_point, to_point):
        """
        Mueve una ficha de un punto a otro
        Retorna True si el movimiento fue exitoso
        """
        if not self.can_move_checker(from_point, to_point):
            return False
        
        # Realizar el movimiento
        checker = self.points[from_point].pop()
        
        # Si hay una ficha oponente solitaria en el destino, capturarla
        if (self.points[to_point] and 
            self.points[to_point][0] != self.current_player and 
            len(self.points[to_point]) == 1):
            # Capturar ficha (en backgammon real iría a la barra)
            captured = self.points[to_point].pop()
        
        # Colocar la ficha en el destino
        self.points[to_point].append(checker)
        
        # Usar el movimiento
        move_distance = abs(to_point - from_point)
        self.moves_remaining.remove(move_distance)
        
        # Si no quedan movimientos, cambiar turno
        if not self.moves_remaining:
            self.switch_player()
        
        return True
    
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