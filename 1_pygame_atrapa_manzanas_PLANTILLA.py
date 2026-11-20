"""
EJERCICIO 1 - PYGAME: "Atrapa las manzanas"  (~30 min)
Mueve la canasta con las flechas IZQUIERDA/DERECHA y atrapa las manzanas.
Cada manzana atrapada suma 1 punto; cada una que se cae resta 1 vida.

INSTRUCCIONES: reemplaza cada ____ por el código correcto (hay 13 espacios).
"""
import pygame
import random

# --- Inicialización ---------------------------------------------------------
pygame.init()
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa las manzanas")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36)

# --- Variables del juego ----------------------------------------------------
jugador = pygame.Rect(250, 360, 100, 20)
velocidad_jugador = 7
manzana = pygame.Rect(random.randint(0, ANCHO - 20), 0, 20, 20)
velocidad_manzana = 4
puntos = 0
vidas = 3
nivel = 1


def reiniciar_manzana():
    """Coloca la manzana arriba, en una posición X aleatoria."""
    manzana.x = random.randint(0, ANCHO - manzana.width)
    manzana.y = 0


# --- Bucle principal --------------------------------------------------------
corriendo = True
while corriendo:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Teclado (movimiento continuo)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad_jugador
    jugador.clamp_ip(pantalla.get_rect())                  # Mantiene la canasta dentro de la ventana

    # Lógica
    manzana.y += velocidad_manzana
    if jugador.colliderect(manzana):
        puntos += 1
        if puntos>0 and puntos%5 == 0:
            velocidad_manzana +=1
            nivel += 1
        reiniciar_manzana()
        print("Llevas", puntos, "puntos. Velocidad: ", velocidad_manzana, "Nivel:", nivel)
    elif manzana.top > ALTO:
        vidas -= 1
        reiniciar_manzana()

    # Dibujo
    pantalla.fill((20, 20, 40))
    pygame.draw.rect(pantalla, (80, 160, 255), jugador)
    pygame.draw.circle(pantalla, (220, 30, 30), manzana.center, 10)
    texto = fuente.render(f"Puntos: {puntos}   Vidas: {vidas}", True, (255, 255, 255))

    pantalla.blit(texto, (10, 10))

    if puntos>0:
        txt_nivel = " "
        if puntos%5==0:
            txt_nivel = f"NIVEL {nivel}"

        texto_nivel = fuente.render(txt_nivel, True, (0, 0, 255))

        w = texto_nivel.get_width()
        h = texto_nivel.get_height()
    
        pantalla.blit(texto_nivel, (ANCHO/2 - w/2, ALTO/2 - h/2))

    if vidas <= 0:

        texto_game_over = fuente.render("GAME OVER", True, (255, 0, 0))
        w = texto_game_over.get_width()
        h = texto_game_over.get_height()
    
        pantalla.blit(texto_game_over, (ANCHO/2 - w/2, ALTO/2 - h/2))

        corriendo = False

    pygame.display.flip()
    reloj.tick(60)


print(f"Fin del juego. Puntaje final: {puntos}")
pygame.quit()

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Haz que la velocidad de la manzana aumente cada 5 puntos.
# b) Muestra "GAME OVER" en pantalla antes de salir.
