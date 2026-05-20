import pygame
import sys

pygame.init()
pygame.mixer.init()

BLANCO = pygame.Color(255, 255, 255)

pantalla = pygame.display.set_mode((400, 400))
pantalla.fill(BLANCO)
pygame.display.set_caption("sonidos en pygame")

continuar = True

SILBATO = pygame.mixer.music.load("assets/sounds/silbato.ogg")

pygame.mixer.music.play(1,0.0)

GALLO = pygame.mixer.Sound("assets/sounds/gallo.ogg")
CUERVO = pygame.mixer.Sound("assets/sounds/cuervo.ogg")
BICI = pygame.mixer.Sound("assets/sounds/timbre.ogg")

while continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                GALLO.play()
            elif event.key == pygame.K_c:
                CUERVO.play()
            elif event.key == pygame.K_b:
                BICI.play()
    pygame.display.flip()
