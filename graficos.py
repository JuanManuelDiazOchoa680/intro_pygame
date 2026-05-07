import math
import pygame
import sys

pygame.init()

ventana = pygame.display.set_mode((400, 400))

#colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

#variables
pi = math.pi


ventana.fill(BLACK)

pygame.draw.line(ventana, WHITE, (0, 0), (400, 400), 5)
pygame.draw.line(ventana, WHITE, (400, 0), (0, 400), 5)
pygame.draw.line(ventana, WHITE, (200, 0), (200, 400), 5)
pygame.draw.line(ventana, WHITE, (0, 200), (400, 200), 5)

pygame.draw.line(ventana, GREEN, (0, 200), (200, 0), 5)
pygame.draw.line(ventana, GREEN, (400, 200), (200, 400), 5)
pygame.draw.line(ventana, GREEN, (200, 0), (400, 200), 5)
pygame.draw.line(ventana, GREEN, (200, 400), (0, 200), 5)

pygame.draw.rect(ventana, ORANGE, (150, 150, 50, 50))
pygame.draw.rect(ventana, GREEN, ((200, 200), (50, 50)), 3)

p3 = [(100, 200), (200, 300), (100, 400), (0, 300)]
pygame.draw.polygon(ventana, BLUE, p3)
p1 = [(300, 0), (400, 100), (300, 200), (200, 100)]
pygame.draw.polygon(ventana, RED, p1)
p2 = [(200, 0), (230, 170), (400, 200), (230, 230), (200, 400), (170, 230), (0, 200), (170, 170)]
pygame.draw.polygon(ventana, YELLOW, p2)

pygame.draw.circle(ventana, WHITE, (300, 300), 100, 0)

pygame.draw.ellipse(ventana, ORANGE, (200, 250, 200, 100), 3)
pygame.draw.ellipse(ventana, ORANGE, (250, 200, 100, 200), 3)

pygame.draw.arc(ventana, GREEN, (200, 0, 200, 200), pi/4, 7*pi/4, 100)

fuente_arial = pygame.font.SysFont("Arial", 35, 1 , 1)
texto = fuente_arial.render("JUAN MANUEL", 1, WHITE)
ventana.blit(texto, (0, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()