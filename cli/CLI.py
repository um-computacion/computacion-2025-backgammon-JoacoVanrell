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

        if not game.movimientos_disponibles():
            print("No tienes movimientos posibles, se cede el turno.")
            game.terminar_turno()
            continue
        
        print(f"Movimientos pendientes: {game.movimientos_disponibles()}")

        # Lógica de reingreso desde la barra
        if jugador.get_fichas_en_barra() > 0:
            print(f"Tenes {jugador.get_fichas_en_barra()} ficha(s) en la barra.")
            dado_input = input("Elige un dado para reingresar (o 'salir'): ").strip()
            if dado_input.lower() == "salir":
                break
            try:
                pasos = int(dado_input)
                game.reingresar_ficha(pasos)
            except ValueError as e:
                print(f"Error al reingresar: {e}")
            continue

        # Solicitar movimiento normal
        origen_input = input("Origen (1-24, o 'salir'): ").strip()
        if origen_input.lower() == "salir":
            break
        try:
            origen = int(origen_input)
        except ValueError:
            print("Origen inválido.")
            continue

        destino_input = input("Destino (1-24): ").strip()
        try:
            destino = int(destino_input)
        except ValueError:
            print("Destino inválido.")
            continue

        # Intentar movimiento
        try:
            turno_terminado = game.mover(origen, destino)
            if turno_terminado:
                print("Turno completado.")
        except ValueError as e:
            print(f"Movimiento inválido: {e}")


if __name__ == "__main__":
    main()