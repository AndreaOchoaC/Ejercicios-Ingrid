"""
EJERCICIO 1 - PYGAME: "Atrapa las manzanas"
Mueve la canasta con las flechas IZQUIERDA/DERECHA y atrapa las manzanas.
Cada manzana atrapada suma 1 punto; cada una que se cae resta 1 vida.

INSTRUCCIONES: reemplaza cada ____ por el código correcto (hay 13 espacios).
"""
import pygame
import random

# --- Inicialización ---------------------------------------------------------
pygame.____()                                          # 1. Inicia PyGame
ANCHO, ALTO = 600, 400
pantalla = pygame.display.____((ANCHO, ALTO))      # 2. Crea la ventana
pygame.display.set_caption("Atrapa las manzanas")
reloj = pygame.time.____()                            # 3. Reloj para controlar los FPS
fuente = pygame.font.SysFont(None, 36)

# --- Variables del juego ----------------------------------------------------
jugador = pygame.Rect(250, 360, 100, 20)
velocidad_jugador = 7
manzana = pygame.Rect(random.randint(0, ANCHO - 20), 0, 20, 20)
velocidad_manzana = ____                                  # 4. Elige una velocidad de caída (número)
puntos = ____                                             # 5. Puntaje inicial
vidas = 3


def reiniciar_manzana():
    """Coloca la manzana arriba, en una posición X aleatoria."""
    manzana.x = random.randint(0, ANCHO - manzana.width)
    manzana.y = ____                                      # 6. Arriba de la pantalla


# --- Bucle principal --------------------------------------------------------
corriendo = True
while corriendo:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.____:                 # 7. Evento de cerrar ventana
            corriendo = False

    # Teclado (movimiento continuo)
    teclas = pygame.key.____()                  # 8. Estado de todas las teclas
    if teclas[pygame.____]:                          # 9. Flecha izquierda
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad_jugador
    jugador.clamp_ip(pantalla.get_rect())                  # Mantiene la canasta dentro de la ventana

    # Lógica
    manzana.y += velocidad_manzana
    if jugador.____(manzana):                   # 10. ¿Hay colisión entre dos Rect?
        puntos += 1
        reiniciar_manzana()
    elif manzana.top > ALTO:
        vidas ____ 1                                     # 11. Resta una vida
        reiniciar_manzana()

    if vidas <= 0:
        corriendo = False

    # Dibujo
    pantalla.fill((20, 20, 40))
    pygame.draw.rect(pantalla, (80, 160, 255), jugador)
    pygame.draw.____(pantalla, (220, 30, 30), manzana.center, 10)   # 12. Dibuja la manzana
    texto = fuente.render(f"Puntos: {puntos}   Vidas: {vidas}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.____()                              # 13. Actualiza la pantalla
    reloj.tick(60)

print(f"Fin del juego. Puntaje final: {puntos}")
pygame.quit()

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Haz que la velocidad de la manzana aumente cada 5 puntos.
# b) Muestra "GAME OVER" en pantalla antes de salir.
