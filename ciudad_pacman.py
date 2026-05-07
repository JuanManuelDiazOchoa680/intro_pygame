# crear una ciudad de hierro con parque de atracciones usando los elementos graficos vistos con pygame
import math
import pygame
import sys
import random

pygame.init()
ventana = pygame.display.set_mode((1000, 600))

gris = (128, 128, 128)
gris_oscuro = (64, 64, 64)
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
naranja = (255, 165, 0)
naranja_oscuro = (255, 140, 0)
amarillo = (255, 255, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
morado = (128, 0, 128)
rosado = (255, 192, 203)

pi = math.pi

#edificios

pygame.draw.rect(ventana, gris, (20, 10, 80, 500))
pygame.draw.rect(ventana, gris, (120, 200, 100, 500))
pygame.draw.rect(ventana, gris, (240, 400, 200, 500))
pygame.draw.rect(ventana, gris, (460, 10, 40, 500))
pygame.draw.rect(ventana, gris, (520, 300, 80, 500))
pygame.draw.rect(ventana, gris, (620, 200, 200, 500))
pygame.draw.rect(ventana, gris, (840, 300, 150, 500))

#piso

pygame.draw.rect(ventana, gris_oscuro, (0, 500, 1000, 100))

# sillas de laa rueda de la fortuna

pygame.draw.rect(ventana, blanco, (690, 160, 20, 20))
pygame.draw.line(ventana, blanco, (690, 160), (700, 150), 3)
pygame.draw.line(ventana, blanco, (710, 160), (700, 150), 3)

pygame.draw.rect(ventana, blanco, (690, 460, 20, 20))
pygame.draw.line(ventana, blanco, (690, 460), (700, 450), 3)
pygame.draw.line(ventana, blanco, (710, 460), (700, 450), 3)

pygame.draw.rect(ventana, blanco, (540, 310, 20, 20))
pygame.draw.line(ventana, blanco, (540, 310), (550, 300), 3)
pygame.draw.line(ventana, blanco, (560, 310), (550, 300), 3)

pygame.draw.rect(ventana, blanco, (840, 310, 20, 20))  
pygame.draw.line(ventana, blanco, (840, 310), (850, 300), 3)
pygame.draw.line(ventana, blanco, (860, 310), (850, 300), 3) 

# rueda de la fortuna

pygame.draw.circle(ventana, rojo, (700, 300), 150, 3)
pygame.draw.line(ventana, rojo, (700, 150), (700, 450), 3)
pygame.draw.line(ventana, rojo, (550, 300), (850, 300), 3)
pygame.draw.line(ventana, rojo, (600, 190), (800, 410), 3)
pygame.draw.line(ventana, rojo, (600, 410), (800, 190), 3)

#base de la rueda de la fortuna
pygame.draw.line(ventana, naranja, (700, 300), (680, 490), 3)
pygame.draw.line(ventana, naranja, (700, 300), (720, 490), 3)
pygame.draw.rect(ventana, naranja_oscuro, (650, 490, 100, 10))

#pacmans (personas)
pygame.draw.arc(ventana, amarillo, (100, 450, 50, 50), pi/4, 7*pi/4, 100)

pygame.draw.arc(ventana, amarillo, (350, 450, 50, 50), 5*pi/4, 11*pi/4, 100)

pygame.draw.arc(ventana, amarillo, (600, 450, 50, 50), pi/4, 7*pi/4, 100)

pygame.draw.arc(ventana, amarillo, (850, 450, 50, 50), 5*pi/4, 11*pi/4, 100)


pygame.display.set_caption("Ciudad Pacman")

texto = pygame.font.SysFont("Arial", 35, 1 , 1)
texto_renderizado = texto.render("JUAN MANUEL", 1, blanco)
ventana.blit(texto_renderizado, (350, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
