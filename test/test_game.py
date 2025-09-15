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

if __name__ == "__main__":
    unittest.main()