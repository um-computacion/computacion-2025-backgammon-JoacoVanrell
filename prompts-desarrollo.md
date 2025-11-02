# Prompts de Desarrollo

Este archivo documenta los prompts utilizados durante el desarrollo del código del proyecto.

---

## Prompt 1: Estructura inicial del proyecto

**Usuario:**
> Necesito empezar un proyecto de Backgammon en Python. ¿Cómo organizo las carpetas y qué clases necesito?

**Asistente:**
Recomendé esta estructura modular:
```
proyecto/
├── core/          # Lógica del juego
├── cli/           # Interfaz terminal
├── pygame_ui/     # Interfaz gráfica (futuro)
├── test/          # Tests unitarios
├── assets/        # Recursos
└── requirements.txt
```

**Clases principales sugeridas:**
- `Ficha`: Representa fichas individuales
- `Jugador`: Información del jugador
- `Dado`: Manejo de tiradas
- `Board`: Tablero de 24 puntos
- `Game`: Orquestador principal

---

## Prompt 2: Implementar clase Dado

**Usuario:**
> ¿Cómo implemento los dados? Necesito que soporten dobles (cuando salen dos números iguales se juega 4 veces)

**Asistente:**
Implementé la clase Dado con:
- Método `lanzar()` que genera dos valores aleatorios
- Método `es_doble()` para detectar dobles
- Atributo `_proximas_tiradas` para testing determinístico
- Lógica en Game para convertir dobles en 4 movimientos

```python
def lanzar(self):
    self._dado1 = random.randint(1, 6)
    self._dado2 = random.randint(1, 6)
    return (self._dado1, self._dado2)
```

---

## Prompt 3: Direcciones de movimiento

**Usuario:**
> No entiendo las direcciones del Backgammon. ¿Cómo se mueven las fichas blancas y negras?

**Asistente:**
Expliqué:
- **Blancas**: Se mueven de punto 24 → 1 (dirección -1)
- **Negras**: Se mueven de punto 1 → 24 (dirección +1)

Implementamos método privado en Game:
```python
def _dir(self, color: str) -> int:
    return -1 if color == "blanco" else +1
```

Esto encapsula la lógica de dirección en un solo lugar.

---

## Prompt 4: Validación de movimientos

**Usuario:**
> Necesito validar que no se puede mover a un punto con 2 o más fichas enemigas

**Asistente:**
Implementé en Board el método `puede_mover_a()`:
```python
def puede_mover_a(self, punto_destino: int, color_jugador: str) -> bool:
    count = self.get_cantidad_fichas(punto_destino)
    color_dest = self.get_color_fichas(punto_destino)
    if count == 0 or color_dest == color_jugador:
        return True
    return count == 1 and color_dest != color_jugador
```

Esto valida:
- Punto vacío ✓
- Punto con fichas propias ✓
- Punto con 1 ficha enemiga ✓ (captura)
- Punto con 2+ fichas enemigas ✗ (bloqueado)

---

## Prompt 5: Sistema de turnos con movimientos pendientes

**Usuario:**
> ¿Cómo manejo que el usuario pueda usar ambos dados en el mismo turno sin que cambie automáticamente?

**Asistente:**
Implementé sistema de movimientos pendientes en Game:
- Atributo `_mov_pendientes: List[int]` que guarda dados disponibles
- Al iniciar turno se llenan: dobles → [3,3,3,3], normales → [2,5]
- Cada movimiento consume un valor con `_consumir(pasos)`
- El turno solo cambia cuando `_mov_pendientes` está vacío

Método clave:
```python
def intentar_mover(self, origen, destino, pasos):
    if self.tablero.mover_ficha(origen, destino, self.turno):
        self._consumir(pasos)
        if not self._mov_pendientes:  # Solo cambiar si ya no hay dados
            self.cambiar_turno()
```

---

## Prompt 6: Pygame no muestra movimientos válidos

**Usuario:**
> Tengo pygame funcionando pero el usuario no sabe dónde puede mover. ¿Cómo muestro los movimientos válidos?

**Asistente:**
Implementamos sistema de destacado visual:
1. Al seleccionar origen, calcular destinos válidos con `obtener_movimientos_validos()`
2. Dibujar círculos verdes en esos puntos con `_dibujar_movimiento_valido()`
3. Usar color semitransparente: `VALID_MOVE_COLOR = (0, 255, 0, 100)`

```python
def _dibujar_movimiento_valido(self, punto):
    x, y = self._calcular_posicion_punto(punto)
    pygame.draw.circle(self.pantalla, VALID_MOVE_COLOR, (x, y), 20)
```

---

## Prompt 7: Fichas en barra tienen prioridad

**Usuario:**
> Las reglas dicen que si tienes fichas en la barra, DEBES reingresarlas antes de hacer otros movimientos. ¿Cómo implemento esto?

**Asistente:**
Implementé validación en Game:
```python
def mover(self, origen, destino):
    if self.jugador_actual().get_fichas_en_barra() > 0:
        raise ValueError("Debes reingresar fichas de la barra primero")
    # ... resto del movimiento
```

Y en pygame_ui verificamos:
```python
if game.jugador_actual().get_fichas_en_barra() > 0:
    # Solo permitir reingresos
    if punto:
        pasos = calcular_pasos_reingreso(punto)
        game.reingresar_ficha(pasos)
```

---

## Prompt 8: Validar movimientos posibles antes de jugar

**Usuario:**
> A veces los dados no permiten ningún movimiento legal y el juego se queda trabado

**Asistente:**
Implementé `_validar_movimientos_posibles()` en Game:
```python
def _validar_movimientos_posibles(self) -> bool:
    # Si hay fichas en barra, solo validar reingresos
    if self.jugador_actual().get_fichas_en_barra() > 0:
        for pasos in set(self._mov_pendientes):
            if puede_reingresar(pasos):
                return True
        return False
    
    # Si no, buscar cualquier movimiento válido
    for origen in range(1, 25):
        for pasos in set(self._mov_pendientes):
            if es_movimiento_valido(origen, pasos):
                return True
    return False
```

Si no hay movimientos, se limpian los dados y se pasa el turno automáticamente.

---

## Prompt 9: Configuración de pylint

**Usuario:**
> ¿Cómo configuro pylint para que no sea tan estricto pero mantenga buena calidad?

**Asistente:**
Creamos `.pylintrc` con configuración balanceada:
```ini
[MESSAGES CONTROL]
disable=
    too-few-public-methods,      # Clases simples están bien
    consider-using-f-string,      # String format es aceptable
    missing-module-docstring      # No todos los módulos necesitan docstring

[DESIGN]
max-line-length=100              # 100 caracteres por línea
max-args=7                       # Hasta 7 argumentos
min-public-methods=1             # Al menos 1 método público

[MASTER]
fail-under=8.0                   # Score mínimo aceptable
```

Esto da flexibilidad sin sacrificar calidad.

---

## Prompt 10: Refactorizar Game con métodos privados

**Usuario:**
> Mi clase Game está muy grande y difícil de leer. ¿Cómo la simplifico?

**Asistente:**
Refactorizamos extrayendo métodos privados:
- `_dir(color)`: Calcula dirección de movimiento
- `_destino(origen, pasos)`: Calcula punto destino
- `_puede_bear_off_desde(origen, pasos)`: Valida bear-off
- `_validar_movimientos_posibles()`: Verifica si hay jugadas legales
- `_consumir(pasos)`: Consume un dado usado

Esto redujo la complejidad ciclomática y mejoró la legibilidad.

**Antes:** Métodos de 50+ líneas
**Después:** Métodos de 10-20 líneas, cada uno con una responsabilidad clara

---

## Resumen de patrones aplicados

### Patrones de diseño:
1. **Separation of Concerns**: core/ separado de UI
2. **Strategy**: Dado como estrategia de generación de números
3. **Facade**: Game como fachada para Board/Dice/Player
4. **Adapter**: pygame_ui/game_state adapta core para pygame

### Principios SOLID aplicados:
- **S**ingle Responsibility: Cada clase hace una cosa
- **O**pen/Closed: Puedes extender sin modificar
- **L**iskov Substitution: Subclases respetan contratos
- **I**nterface Segregation: Interfaces pequeñas y específicas
- **D**ependency Inversion: UI depende de abstracciones (Game), no de detalles

### Mejores prácticas:
- Type hints en todos los métodos
- Docstrings en métodos públicos
- Validación estricta de inputs
- Manejo de errores con excepciones descriptivas
- Encapsulación con atributos privados (_atributo)
- Métodos privados para lógica interna (_metodo)

### Herramientas de desarrollo:
- Git para control de versiones
- pylint para calidad de código
- coverage para medir tests
- unittest para testing
- Type hints para documentación
