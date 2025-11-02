# Prompts de Testing

Este archivo documenta los prompts utilizados durante el desarrollo de los tests del proyecto.

---

## Prompt 1: Tests básicos para la clase Game

**Usuario:**
> Necesito ayuda para hacer tests de la clase Game. Quiero testear el flujo básico de un turno: lanzar dados, hacer un movimiento válido, y cambiar de turno. ¿Me puedes ayudar a estructurar estos tests?

**Asistente:**
Creé tests en `test/test_game.py` que incluyen:
- `test_iniciar_turno_lanza_dados`: Verifica que al iniciar turno se lancen los dados correctamente
- `test_movimientos_disponibles_dobles`: Valida que los dobles generan 4 movimientos
- `test_mover_ficha_consume_dado`: Comprueba que al mover una ficha se consume el valor del dado usado
- `test_terminar_turno_cambia_jugador`: Verifica que terminar turno cambia al siguiente jugador

---

## Prompt 2: Tests de captura y barra

**Usuario:**
> Necesito tests más complejos para la clase Game que cubran captura de fichas y reingreso desde la barra. ¿Cómo puedo mockear el tablero para estos casos?

**Asistente:**
Implementé tests usando stubs del tablero:
- `test_captura_aumenta_barra_del_rival`: Verifica que capturar una ficha aumenta el contador de barra del rival
- `test_reingresar_ficha_reduce_barra`: Comprueba que reingresar desde barra reduce el contador
- `test_no_puede_mover_con_fichas_en_barra`: Valida que con fichas en barra solo se permiten reingresos

Usé la técnica de crear clases stub como `_BoardStubCaptura` para simular estados específicos del tablero sin depender de la implementación real de Board.

---

## Prompt 3: Tests de bear-off

**Usuario:**
> ¿Cómo testeo el bear-off? Es la parte más compleja porque hay que verificar que todas las fichas estén en casa antes de poder sacar

**Asistente:**
Creé tests específicos para bear-off:
- `test_bear_off_valido`: Verifica que se puede sacar una ficha cuando todas están en casa
- `test_bear_off_invalido_fichas_fuera_casa`: Comprueba que no se puede sacar si hay fichas fuera de casa
- `test_bear_off_aumenta_contador_fuera`: Valida que sacar una ficha incrementa el contador de fichas fuera

También implementé un stub `_BoardStubBearOff` que simula el estado donde todas las fichas están en casa.

---

## Prompt 4: Aumentar cobertura de tests

**Usuario:**
> Ejecuté coverage y me da 85%. ¿Qué me falta testear para llegar a >90%?

**Asistente:**
Analicé el reporte de coverage y agregué tests faltantes:
- Tests para el método `_validar_movimientos_posibles()`
- Tests para casos edge: turnos sin movimientos válidos
- Tests para validación de bear-off con diferentes configuraciones
- Tests para dobles cuando no hay movimientos disponibles

Con estos tests adicionales la cobertura subió a 94%.

---

## Prompt 5: Tests de integración con Pygame

**Usuario:**
> ¿Cómo testeo que pygame_ui se integra correctamente con el core sin tener que ejecutar la interfaz gráfica?

**Asistente:**
Expliqué que para pygame_ui es mejor hacer:
1. Tests unitarios del core (ya los tienes)
2. Tests de las funciones de drawing que no dependan de pygame.display
3. Tests manuales de la interfaz ejecutando el juego

Pygame es difícil de testear automáticamente porque requiere ventanas y eventos reales. Lo importante es que el core esté 100% testeado, que es donde está la lógica crítica.

---

## Prompt 6: Uso de mocks para dados aleatorios

**Usuario:**
> Mis tests de dados fallan aleatoriamente porque usan random. ¿Cómo hago tests determinísticos?

**Asistente:**
Implementé dos soluciones:
1. Usar `set_proximas_tiradas()` en la clase Dado para tests determinísticos
2. Usar `unittest.mock.patch` para mockear `random.randint`:

```python
@patch('random.randint', side_effect=[3, 5])
def test_lanzar_dados(self, mock_random):
    dados = self.game.dados.lanzar()
    self.assertEqual(dados, (3, 5))
```

Esto garantiza que los tests sean reproducibles.

---

## Prompt 7: Tests de validación de movimientos

**Usuario:**
> Necesito testear que Game valide correctamente que no se puede mover a un punto bloqueado por 2+ fichas enemigas

**Asistente:**
Creé tests específicos de validación:
- `test_no_puede_mover_punto_bloqueado`: Verifica rechazo de movimiento a punto bloqueado
- `test_puede_capturar_ficha_solitaria`: Valida que sí se puede mover a punto con 1 ficha enemiga
- `test_puede_mover_punto_propio`: Comprueba que siempre puedes mover a tus propios puntos

Estos tests usan stubs del tablero para simular diferentes configuraciones de fichas.

---

## Resumen de estrategia de testing

1. **Tests unitarios por clase**: Cada clase del core tiene su archivo de tests
2. **Uso de stubs**: Para aislar componentes y testear casos específicos
3. **Mocks para aleatoriedad**: Para hacer tests determinísticos
4. **Cobertura >90%**: Objetivo cumplido con 94% en módulo core
5. **46 tests en total**: Distribuidos en 5 archivos

**Herramientas utilizadas:**
- `unittest` (biblioteca estándar de Python)
- `unittest.mock` para mocking
- `coverage.py` para medir cobertura
- Stubs personalizados para Board

**Comandos útiles:**
```bash
# Ejecutar todos los tests
python3 -m unittest discover -s test -v

# Ejecutar tests con cobertura
python3 -m coverage run -m unittest discover -s test
python3 -m coverage report

# Ver cobertura detallada
python3 -m coverage html
```
