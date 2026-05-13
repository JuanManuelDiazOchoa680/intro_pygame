import math
import pygame
import sys

pygame.init()
ventana = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Ciudad Pacman")

gris = (128, 128, 128)
gris_oscuro = (64, 64, 64)
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
naranja = (255, 165, 0)
naranja_oscuro = (255, 140, 0)
amarillo = (255, 255, 0)

pi = math.pi

texto = pygame.font.SysFont("Arial", 35, True, True)
texto_renderizado = texto.render("JUAN MANUEL", True, blanco)

pacmans = [
    {"x": 100, "y": 450, "vx": 4},
    {"x": 350, "y": 450, "vx": -3},
    {"x": 600, "y": 450, "vx": 5},
    {"x": 850, "y": 450, "vx": -4},
]

clock = pygame.time.Clock()


def dibujar_escena(surface):
    surface.fill(negro)

    pygame.draw.rect(surface, gris, (20, 10, 80, 500))
    pygame.draw.rect(surface, gris, (120, 200, 100, 500))
    pygame.draw.rect(surface, gris, (240, 400, 200, 500))
    pygame.draw.rect(surface, gris, (460, 10, 40, 500))
    pygame.draw.rect(surface, gris, (520, 300, 80, 500))
    pygame.draw.rect(surface, gris, (620, 200, 200, 500))
    pygame.draw.rect(surface, gris, (840, 300, 150, 500))

    pygame.draw.rect(surface, gris_oscuro, (0, 500, 1000, 100))

    pygame.draw.rect(surface, blanco, (690, 160, 20, 20))
    pygame.draw.line(surface, blanco, (690, 160), (700, 150), 3)
    pygame.draw.line(surface, blanco, (710, 160), (700, 150), 3)

    pygame.draw.rect(surface, blanco, (690, 460, 20, 20))
    pygame.draw.line(surface, blanco, (690, 460), (700, 450), 3)
    pygame.draw.line(surface, blanco, (710, 460), (700, 450), 3)

    pygame.draw.rect(surface, blanco, (540, 310, 20, 20))
    pygame.draw.line(surface, blanco, (540, 310), (550, 300), 3)
    pygame.draw.line(surface, blanco, (560, 310), (550, 300), 3)

    pygame.draw.rect(surface, blanco, (840, 310, 20, 20))
    pygame.draw.line(surface, blanco, (840, 310), (850, 300), 3)
    pygame.draw.line(surface, blanco, (860, 310), (850, 300), 3)

    pygame.draw.circle(surface, rojo, (700, 300), 150, 3)
    pygame.draw.line(surface, rojo, (700, 150), (700, 450), 3)
    pygame.draw.line(surface, rojo, (550, 300), (850, 300), 3)
    pygame.draw.line(surface, rojo, (600, 190), (800, 410), 3)
    pygame.draw.line(surface, rojo, (600, 410), (800, 190), 3)

    pygame.draw.line(surface, naranja, (700, 300), (680, 490), 3)
    pygame.draw.line(surface, naranja, (700, 300), (720, 490), 3)
    pygame.draw.rect(surface, naranja_oscuro, (650, 490, 100, 10))

    surface.blit(texto_renderizado, (350, 20))


def dibujar_pacman(surface, x, y, direccion_derecha):
    rect = pygame.Rect(x, y, 50, 50)
    if direccion_derecha:
        inicio = pi / 4
        fin = 7 * pi / 4
    else:
        inicio = 5 * pi / 4
        fin = 11 * pi / 4
    pygame.draw.arc(surface, amarillo, rect, inicio, fin, 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for pacman in pacmans:
        pacman["x"] += pacman["vx"]
        if pacman["x"] <= 0:
            pacman["x"] = 0
            pacman["vx"] *= -1
        elif pacman["x"] >= 950:
            pacman["x"] = 950
            pacman["vx"] *= -1

    dibujar_escena(ventana)
    for pacman in pacmans:
        direccion_derecha = pacman["vx"] > 0
        dibujar_pacman(ventana, pacman["x"], pacman["y"], direccion_derecha)

    pygame.display.update()
    clock.tick(50)
