from core.game import Game


def main() -> None:
    print("=== Backgammon CLI ===")
    game = Game("Jugador 1", "Jugador 2")

    while True:
        # Estado de la partida
        if game.ha_terminado():
            print(game.mostrar_tablero())
            print(f"Ganador: {game.get_ganador()}")
            break

        # Mostrar tablero y turno
        print(game.mostrar_tablero())
        jugador = game.jugador_actual()
        print(f"Turno de: {jugador.get_nombre()} ({jugador.get_color()})")

        # Tirada de dados o movimientos pendientes
        if not game.movimientos_disponibles():
            tirada = game.lanzar_dados()
            print(f"Tirada de dados: {tirada}")
        else:
            print(f"Movimientos pendientes: {game.movimientos_disponibles()}")

        # Solicitar punto de origen
        origen_input = input("Origen (1-24, o 'salir'): ").strip()
        if origen_input.lower() == "salir":
            print("Saliendo del juego...")
            break
        try:
            origen = int(origen_input)
        except ValueError:
            print("Origen inválido. Ingresá un número entre 1 y 24.")
            continue

        # Solicitar punto de destino
        destino_input = input("Destino (1-24, o 'salir'): ").strip()
        if destino_input.lower() == "salir":
            print("Saliendo del juego...")
            break
        try:
            destino = int(destino_input)
        except ValueError:
            print("Destino inválido. Ingresá un número entre 1 y 24.")
            continue

        # Intentar movimiento
        try:
            game.mover(origen, destino)
        except ValueError as e:
            print(f"Movimiento inválido: {e}")
            continue


if __name__ == "__main__":
    main()