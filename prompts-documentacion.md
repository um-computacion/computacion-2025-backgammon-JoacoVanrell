# Prompts de Documentación

Este archivo documenta los prompts utilizados para crear y mantener la documentación del proyecto.

---

## Prompt 1: Estructura del README

**Usuario:**
> Necesito crear un README profesional para mi proyecto de Backgammon. ¿Qué secciones debería incluir?

**Asistente:**
Recomendé incluir estas secciones:
1. **Título y descripción**: Qué es el proyecto
2. **Instalación**: Cómo instalar dependencias
3. **Uso**: Cómo ejecutar CLI y Pygame
4. **Testing**: Cómo correr tests y coverage
5. **Estructura del proyecto**: Organización de carpetas
6. **Reglas del juego**: Resumen de cómo se juega Backgammon
7. **Tecnologías**: Python, pygame, unittest, etc.
8. **Autor y licencia**: Información del proyecto

Creamos un README de ~267 líneas con toda esta información.

---

## Prompt 2: ¿Qué es un CHANGELOG?

**Usuario:**
> Me pidieron hacer un CHANGELOG.md pero no sé bien qué es ni cómo se estructura. ¿Me explicas?

**Asistente:**
Un CHANGELOG es un archivo que documenta todos los cambios importantes del proyecto en orden cronológico. Expliqué el formato basado en [Keep a Changelog](https://keepachangelog.com/):

**Estructura:**
- **[Liberado] - Fecha**: Versión publicada
- **Agregado**: Nuevas funcionalidades
- **Cambiado**: Cambios en funcionalidad existente
- **Corregido**: Bugs arreglados
- **Eliminado**: Funcionalidades removidas

**Ejemplo:**
```markdown
## [Liberado] - 2025-11-01

### Agregado
- Interfaz Pygame completamente funcional
- Sistema de validación de movimientos

### Mejorado
- Game.py refactorizado con mejores validaciones
```

Creamos el CHANGELOG con todas las fases del desarrollo del proyecto.

---

## Prompt 3: Documentación de justificacion.md

**Usuario:**
> Tengo que hacer un archivo justificacion.md que explique mis decisiones de diseño. ¿Qué debería incluir?

**Asistente:**
Recomendé estructurarlo así:
1. **Resumen del diseño general**: Arquitectura en capas
2. **Clases y responsabilidades**: Qué hace cada clase
3. **Justificación de atributos**: Por qué elegiste ciertos atributos
4. **Decisiones de diseño relevantes**: Por qué separaste core/UI, etc.
5. **Excepciones y manejo de errores**: Cómo validas
6. **Estrategia de testing**: Por qué 46 tests, qué cubren
7. **Integración entre capas**: Cómo se comunican core/CLI/pygame

Creamos un documento que explica el "por qué" detrás de cada decisión técnica.

---

## Prompt 4: Agregar diagrama UML

**Usuario:**
> El diagrama UML va dentro del archivo de justificacion.md, crealo sin imagen, con puro texto

**Asistente:**
Creé un diagrama UML completo en formato ASCII que incluye:
- Todas las clases del core (Ficha, Jugador, Dado, Board, Game)
- Clases de UI (CLI, Constants, Drawing, Main)
- Relaciones: composición (◆), agregación (◇), dependencia (---)
- Atributos y métodos de cada clase
- Notación UML estándar (+público, -privado)

El diagrama se visualiza perfectamente en cualquier editor de texto.

---

## Prompt 5: Actualizar README con Pygame

**Usuario:**
> Ya tengo pygame funcionando, necesito actualizar el README para explicar cómo usarlo

**Asistente:**
Agregamos sección completa de Pygame:
- Cómo ejecutar: `python3 pygame_ui/main.py`
- **Controles**:
  - ESPACIO: Lanzar dados
  - Clic izquierdo: Seleccionar ficha y destino
  - R: Reiniciar
  - ESC/Q: Salir
  - H: Ayuda
- Explicación de círculos verdes (movimientos válidos)
- Pantalla de victoria y reinicio

---

## Prompt 6: Documentar uso de pylint

**Usuario:**
> Ya implementé pylint, ¿cómo lo documento en el README?

**Asistente:**
Agregamos sección de calidad de código:
```bash
# Verificar el core
pylint core/

# Verificar el CLI
pylint cli/

# Verificar todo
pylint core/ cli/
```

Explicamos que el score esperado es ≥8.0/10 y que está configurado en `.pylintrc`.

---

## Prompt 7: Completar documentación final

**Usuario:**
> Podrias hacerme la version final del readme. No inclui lo del docker porque no era obligatoria, y si implemente ya lo del pylint. Tambien actualizame el de justificacion.md

**Asistente:**
Actualicé ambos archivos:

**README.md:**
- Eliminé referencias a Docker (no obligatorio)
- Agregué instrucciones completas de pylint
- Documenté controles de Pygame
- Agregué estadísticas del proyecto (46 tests, >90% coverage)
- Incluí tabla de métricas

**justificacion.md:**
- Amplié sección de pygame_ui con separación modular
- Agregué detalles de interactividad completa
- Documenté manejo de casos especiales
- Incluí flujo de integración entre capas
- Agregué diagrama UML en ASCII

---

## Prompt 8: Actualizar CHANGELOG con última versión

**Usuario:**
> Ahora actualizame el changelog

**Asistente:**
Agregué entrada del 1 de noviembre 2025 con:
- **Agregado**: Pygame funcional, validación de movimientos, pylint, Dockerfile
- **Mejorado**: Game.py refactorizado, CLI mejorado, Pygame optimizado
- **Documentación**: README y justificacion.md actualizados
- **Técnico**: 46 tests, >90% coverage, pylint ≥8.0

---

## Resumen de documentación creada

### Archivos principales:
1. **README.md** (~400 líneas): Documentación completa del proyecto
2. **CHANGELOG.md** (~350 líneas): Historial de cambios detallado
3. **justificacion.md** (~200 líneas): Decisiones técnicas y diagrama UML

### Buenas prácticas aplicadas:
- Formato Markdown consistente
- Ejemplos de código cuando es relevante
- Comandos copy-paste listos para usar
- Secciones claramente organizadas
- Lenguaje claro y directo
- Sin jerga innecesaria

### Herramientas mencionadas:
- Python 3.10+
- pygame 2.6+
- unittest
- coverage.py
- pylint

### Audiencia objetivo:
- Profesor de la materia (evaluación)
- Compañeros estudiantes (referencia)
- Yo mismo en el futuro (mantenimiento)
