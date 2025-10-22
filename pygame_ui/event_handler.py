"""
Manejador de eventos para la interfaz pygame de Backgammon
Basado en la estructura del profesor - separación de responsabilidades
"""

import pygame
from constants import *


class ManejadorEventos:
    """
    Clase responsable de manejar todos los eventos de pygame
    Sigue el patrón del profesor: cada clase tiene una responsabilidad específica
    """
    
    def __init__(self):
        self.ejecutandose = True
        self.punto_seleccionado = None
        self.ultima_posicion_clic = None
    
    def esta_ejecutandose(self):
        """Retorna si la aplicación debe seguir ejecutándose"""
        return self.ejecutandose
    
    def obtener_punto_seleccionado(self):
        """Retorna el punto actualmente seleccionado"""
        return self.punto_seleccionado
    
    def _detectar_clic_en_ficha(self, mapa_clics, posicion):
        """
        Detecta si un clic intersecta con alguna ficha
        Retorna el número del punto o None
        """
        clic_x, clic_y = posicion
        
        for numero_punto, fichas in mapa_clics.items():
            for ficha_x, ficha_y, radio in fichas:
                # Calcular distancia del clic al centro de la ficha
                distancia_cuadrada = (clic_x - ficha_x) ** 2 + (clic_y - ficha_y) ** 2
                if distancia_cuadrada <= radio ** 2:
                    return numero_punto
        
        return None
    
    def manejar_clic_mouse(self, posicion, mapa_clics):
        """
        Maneja clics del mouse en el tablero
        posicion: posición del clic (x, y)
        mapa_clics: mapa de posiciones de fichas para detección de colisiones
        """
        self.ultima_posicion_clic = posicion
        punto_clickeado = self._detectar_clic_en_ficha(mapa_clics, posicion)
        
        if punto_clickeado is not None:
            if self.punto_seleccionado == punto_clickeado:
                # Clic en el mismo punto: deseleccionar
                self.punto_seleccionado = None
                return {'accion': 'deseleccionar', 'punto': punto_clickeado}
            else:
                # Clic en punto diferente: seleccionar nuevo
                seleccion_anterior = self.punto_seleccionado
                self.punto_seleccionado = punto_clickeado
                return {
                    'accion': 'seleccionar', 
                    'punto': punto_clickeado, 
                    'anterior': seleccion_anterior
                }
        else:
            # Clic en área vacía: deseleccionar
            if self.punto_seleccionado is not None:
                seleccion_anterior = self.punto_seleccionado
                self.punto_seleccionado = None
                return {'accion': 'deseleccionar', 'punto': seleccion_anterior}
        
        return {'accion': 'ninguna'}
    
    def manejar_teclado(self, tecla):
        """
        Maneja eventos de teclado
        tecla: tecla presionada
        """
        if tecla == pygame.K_ESCAPE or tecla == pygame.K_q:
            self.ejecutandose = False
            return {'accion': 'salir'}
        
        elif tecla == pygame.K_SPACE:
            return {'accion': 'tirar_dados'}
        
        elif tecla == pygame.K_r:
            return {'accion': 'reiniciar_juego'}
        
        elif tecla == pygame.K_h:
            return {'accion': 'mostrar_ayuda'}
        
        return {'accion': 'ninguna'}
    
    def procesar_eventos(self, mapa_clics=None):
        """
        Procesa todos los eventos pendientes de pygame
        Retorna una lista de acciones a realizar
        """
        acciones = []
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutandose = False
                acciones.append({'accion': 'salir'})
            
            elif evento.type == pygame.KEYDOWN:
                accion = self.manejar_teclado(evento.key)
                if accion['accion'] != 'ninguna':
                    acciones.append(accion)
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1 and mapa_clics is not None:  # Clic izquierdo
                    accion = self.manejar_clic_mouse(evento.pos, mapa_clics)
                    if accion['accion'] != 'ninguna':
                        acciones.append(accion)
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 3:  # Clic derecho
                    acciones.append({'accion': 'clic_derecho', 'posicion': evento.pos})
        
        return acciones
    
    def limpiar_seleccion(self):
        """Limpia la selección actual"""
        self.punto_seleccionado = None