import unittest
from core.game import Game

class TestGame(unittest.TestCase):

    def test_iniciar_turno_y_movimientos(self):
        g = Game()
        d1, d2 = g.iniciar_turno()
        movs = g.movimientos_disponibles()
        if d1 == d2:
            self.assertEqual(len(movs), 4)
        else:
            self.assertIn(len(movs), (1, 2))
        self.assertFalse(g.sin_movimientos())

    def test_mover_basico_y_cambio_turno(self):
        g = Game()
        # Forzamos un solo paso con dado
        g.dados.set_proximas_tiradas([(3,0)])
        g.iniciar_turno()  # now [3]
        origen = 6
        destino = 3
        g.mover(origen, destino)
        self.assertTrue(g.sin_movimientos())
        self.assertEqual(g.turno, "negro")

    def test_ha_terminado_get_ganador(self):
        g = Game()
        # Forzamos victoria de blanco
        for _ in range(g.blanco.TOTAL_FICHAS):
            g.blanco.agregar_fuera()
        self.assertTrue(g.ha_terminado())
        self.assertEqual(g.get_ganador(), g.blanco.get_nombre())

    def test_lanzar_dados_alias_sin_pendientes(self):
        g = Game()
        # Al no tener movimientos pendientes, lanzar_dados inicia turno
        d1, d2 = g.lanzar_dados()
        self.assertFalse(g.sin_movimientos())
        movs = g.movimientos_disponibles()
        # Puede ser 1, 2 ó 4 movimientos según doble o no
        self.assertIn(len(movs), (1, 2, 4))

    def test_lanzar_dados_alias_con_pendientes(self):
        g = Game()
        g.dados.set_proximas_tiradas([(2, 5)])
        g.iniciar_turno()            # mov_pendientes == [2, 5]
        vals = g.lanzar_dados()       # no reinicia; branch alternativo
        self.assertEqual(vals, (2, 5))
        self.assertEqual(g.movimientos_disponibles(), [2, 5])

    def test_mover_alias_direccion_invalida(self):
        g = Game()
        # Para blanco, origen < destino da pasos negativos
        with self.assertRaises(ValueError) as cm:
            g.mover(3, 4)
        self.assertIn("Dirección inválida", str(cm.exception))

    def test_intentar_mover_origen_fuera_rango(self):
        g = Game()
        # Forzamos un valor de dado válido para pasar ese if
        g._mov_pendientes = [1]
        with self.assertRaises(ValueError) as cm:
            g.intentar_mover(0, 1)
        self.assertIn("punto de origen", str(cm.exception))

    def test_intentar_mover_valor_no_disponible(self):
        g = Game()
        # Sin iniciar turno, lista de movimientos vacía
        with self.assertRaises(ValueError) as cm:
            g.intentar_mover(6, 2)
        self.assertEqual(str(cm.exception), "Ese valor de dado no está disponible")

    def test_intentar_mover_origen_vacio(self):
        g = Game()
        # habilitamos un dado para pasar la validación de "no disponible"
        g._mov_pendientes = [2]
        # en la apertura, el punto 7 está vacío para blancas
        with self.assertRaises(ValueError) as cm:
            g.intentar_mover(7, 2)
        self.assertIn("No hay fichas en el punto 7", str(cm.exception))

    def test_intentar_mover_color_equivocado(self):
        g = Game()
        # habilitamos un dado cualquiera
        g._mov_pendientes = [1]
        # en la apertura, el punto 12 es de negras; turno = blanco
        with self.assertRaises(ValueError) as cm:
            g.intentar_mover(12, 1)
        self.assertIn("No hay fichas blanco en el punto 12", str(cm.exception))

    def test_destino_fuera_sin_bearoff(self):
        g = Game()
        # forzamos tirada 6 para intentar 6->0 (fuera) sin estar en fase de bear-off
        g.dados.set_proximas_tiradas([(6, 0)])
        g.iniciar_turno()  # pendientes [6]
        # desde 6 con paso 6, destino = 0 -> debe ser inválido
        with self.assertRaises(ValueError) as cm:
            g.intentar_mover(6, 6)
        self.assertIn("Destino fuera del tablero y no es bear-off válido", str(cm.exception))

    def test_punto_bloqueado_para_negras(self):
        g = Game()
        # Simulamos turno de negras y dado 1 para intentar 12->13 (13 tiene 5 blancas)
        g.turno = "negro"
        g._mov_pendientes = [1]
        with self.assertRaises(ValueError) as cm:
            g.intentar_mover(12, 1)
        self.assertIn("El punto 13 está bloqueado", str(cm.exception))

    def test_consumo_parcial_de_dados(self):
        g = Game()
        # dos valores: 1 y 2
        g.dados.set_proximas_tiradas([(1, 2)])
        g.iniciar_turno()
        # mover 6->5 consume el "1"
        g.mover(6, 5)
        movs_restantes = g.movimientos_disponibles()
        self.assertEqual(len(movs_restantes), 1)
        self.assertIn(movs_restantes[0], (1, 2))

    def test_cambio_de_turno_y_jugador_rival(self):
        g = Game()
        self.assertEqual(g.jugador_actual().get_color(), "blanco")
        self.assertEqual(g.jugador_rival().get_color(), "negro")
        g.terminar_turno()
        self.assertEqual(g.jugador_actual().get_color(), "negro")
        self.assertEqual(g.jugador_rival().get_color(), "blanco")

    def test_mostrar_tablero_y_ganador_none(self):
        g = Game()
        tablero = g.mostrar_tablero()
        self.assertIsInstance(tablero, str)
        # al inicio no hay ganador
        self.assertIsNone(g.get_ganador())

    def test_pasos_no_positivos(self):
        g = Game()
        g._mov_pendientes = [1]  # para no chocar con "no disponible"
        with self.assertRaises(ValueError) as cm:
            g.intentar_mover(6, 0)
        self.assertIn("Los pasos deben ser positivos", str(cm.exception))

    def test_mover_sin_pendientes_dispara_no_disponible(self):
        g = Game()
        # sin tirar; _mov_pendientes = []
        with self.assertRaises(ValueError) as cm:
            g.mover(6, 5)  # calculará pasos=1 y fallará por "no disponible"
        self.assertIn("Ese valor de dado no está disponible", str(cm.exception))

    def test_lanzar_dados_con_un_solo_pendiente_devuelve_cero(self):
        g = Game()
        g.dados.set_proximas_tiradas([(4, 0)])  # así queda un solo valor
        g.iniciar_turno()
        vals = g.lanzar_dados()
        # cuando hay uno solo pendiente, el alias devuelve (v, 0)
        self.assertIn(vals[0], (4,))
        self.assertIn(vals[1], (0,))

    def test_consumir_devuelve_false_si_no_existe(self):
        g = Game()
        g._mov_pendientes = [2, 5]
        # método "privado" pero simple: ya venimos usando _mov_pendientes en tests
        self.assertFalse(g._consumir(3))
        self.assertEqual(g._mov_pendientes, [2, 5])

    def test_cambio_turno_y_rival(self):
        g = Game()
        self.assertEqual(g.jugador_actual().get_color(), "blanco")
        self.assertEqual(g.jugador_rival().get_color(), "negro")
        g.terminar_turno()
        self.assertEqual(g.jugador_actual().get_color(), "negro")
        self.assertEqual(g.jugador_rival().get_color(), "blanco")


    class _BoardStubCaptura:
        def get_cantidad_fichas(self, p): return 1
        def get_color_fichas(self, p): return "blanco"
        def puede_mover_a(self, p, c): return True
        def mover_ficha(self, o, d, c):
            from core.checker import Ficha
            return Ficha("negro")  # simula captura
        def mostrar_tablero(self): return "<stub>"

    def test_captura_aumenta_barra_del_rival(self):
        g = Game()
        g.tablero = self._BoardStubCaptura()
        g._mov_pendientes = [1]
        barra_antes = g.jugador_rival().en_barra()
        g.intentar_mover(6, 1)  # da igual el origen con el stub
        self.assertEqual(g.jugador_rival().en_barra(), barra_antes + 1)
        self.assertTrue(g.sin_movimientos())


    class _BoardStubBearOff:
        # el Game usa estas “constantes” del board:
        CASA_BLANCA = set(range(1, 7))
        CASA_NEGRA = set(range(19, 25))
        def __init__(self): self.saco = False
        def puede_bear_off(self, color): return color == "blanco"
        def sacar_ficha(self, origen):
            from core.checker import Ficha
            self.saco = True
            return Ficha("blanco")
        # métodos que Game podría consultar en otras ramas (no usados acá):
        def mostrar_tablero(self): return "<stub>"
        def get_cantidad_fichas(self, p): return 1
        def get_color_fichas(self, p): return "blanco"
        def puede_mover_a(self, p, c): return True
        def mover_ficha(self, o, d, c): return None

    def test_bearoff_consumo_y_fuera(self):
        g = Game()
        g.tablero = self._BoardStubBearOff()
        g._mov_pendientes = [6]
        fuera_antes = g.jugador_actual().fuera()
        # origen 1 para blancas con paso 6 → destino < 1 ⇒ bear-off
        g.intentar_mover(1, 6)
        self.assertEqual(g.jugador_actual().fuera(), fuera_antes + 1)
        self.assertTrue(g.sin_movimientos())


    def test_destino_fuera_sin_bearoff_con_mover(self):
        g = Game()
        g.dados.set_proximas_tiradas([(6, 0)])
        g.iniciar_turno()
        # mover() calcula pasos y luego cae en el mismo mensaje
        with self.assertRaises(ValueError) as cm:
            g.mover(6, 0)  # destino 0 inválido para CLI
        self.assertIn("Destino fuera del tablero y no es bear-off válido", str(cm.exception))



if __name__ == "__main__":
    unittest.main()
