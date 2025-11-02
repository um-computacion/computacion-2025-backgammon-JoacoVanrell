import pygame
from core.game import Game
from .constants import WIDTH, HEIGHT, COLOR_FONDO
from .drawing import dibujar_todo, get_punto_from_coords

def mostrar_pantalla_final(screen, ganador):
    """Muestra el mensaje del ganador y espera un clic para reiniciar."""
    FONT_GRANDE = pygame.font.SysFont("sans-serif", 48)
    mensaje = f"¡Ha ganado {ganador}!"
    texto = FONT_GRANDE.render(mensaje, True, (0,100,0))
    rect = texto.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
    
    mensaje_reinicio = pygame.font.SysFont("sans-serif", 32).render(
        "Haz clic para jugar de nuevo", True, (0,0,0)
    )
    rect_reinicio = mensaje_reinicio.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20))

    screen.fill(COLOR_FONDO)
    screen.blit(texto, rect)
    screen.blit(mensaje_reinicio, rect_reinicio)
    pygame.display.flip()

    esperando_reinicio = True
    while esperando_reinicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False # Salir del juego
            if event.type == pygame.MOUSEBUTTONDOWN:
                esperando_reinicio = False
    return True # Reiniciar

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Backgammon (Pygame)")
    clock = pygame.time.Clock()
    
    juego_activo = True
    while juego_activo:
        game = Game()
        partida_en_curso = True
        mensaje = "¡Bienvenido! Haz clic para lanzar los dados."
        origen_seleccionado = None

        while partida_en_curso:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    partida_en_curso = False
                    juego_activo = False

                if event.type == pygame.MOUSEBUTTONDOWN and not game.ha_terminado():
                    pos = pygame.mouse.get_pos()
                    if game.sin_movimientos():
                        game.lanzar_dados()
                        dados = game.movimientos_disponibles()
                        mensaje = f"Dados: {dados}"
                        if not dados:
                            mensaje = "No hay movimientos. Turno perdido."
                            game.terminar_turno()
                    else:
                        punto = get_punto_from_coords(pos)
                        if game.jugador_actual().get_fichas_en_barra() > 0:
                            if punto:
                                pasos = punto if game.turno == 'blanco' else 25 - punto
                                try:
                                    game.reingresar_ficha(pasos)
                                    mensaje = f"Ficha reingresada en {punto}."
                                    if game.sin_movimientos():
                                        mensaje = "Turno completado."
                                except ValueError as e:
                                    mensaje = f"Error: {e}"
                        elif punto:
                            if origen_seleccionado is None:
                                if game.tablero.get_color_fichas(punto) == game.turno:
                                    origen_seleccionado = punto
                                    mensaje = f"Ficha en {punto} seleccionada."
                                else:
                                    mensaje = "Selecciona una de tus fichas."
                            else:
                                try:
                                    game.mover(origen_seleccionado, punto)
                                    mensaje = f"Movido de {origen_seleccionado} a {punto}."
                                    if game.sin_movimientos():
                                        mensaje = "Turno completado."
                                except ValueError as e:
                                    mensaje = f"Error: {e}"
                                finally:
                                    origen_seleccionado = None

            screen.fill(COLOR_FONDO)
            dibujar_todo(screen, game, mensaje, origen_seleccionado)
            pygame.display.flip()

            if game.ha_terminado():
                ganador = game.get_ganador()
                if not mostrar_pantalla_final(screen, ganador):
                    juego_activo = False
                partida_en_curso = False
            
            clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
