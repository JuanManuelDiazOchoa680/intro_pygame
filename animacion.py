# importamos la libreria pygame
import pygame
import sys

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((1000, 700))

# establecer titulo de la ventana
pygame.display.set_caption("Rebotes rectángulo")

# definición colores
rojo = (255,0,0)
azul = (0,0,255)

# variable de movimiento
XX = 50
MOVIMIENTO_XX = 5
MOVIMIENTO_XY = 5
YX = 60
MOVIMIENTO_YX = 5
MOVIMIENTO_YY = 5
ZX = 70
MOVIMIENTO_ZX = 5
MOVIMIENTO_ZY = 5
AX = 80
MOVIMIENTO_AX = 5
MOVIMIENTO_AY = 5
BX = 90
MOVIMIENTO_BX = 5
MOVIMIENTO_BY = 5


XY = 150
YY = 160
ZY = 170
AY = 180
BY = 190




# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)



    # movimiento del rectángulo
    XX = XX + MOVIMIENTO_XX
    XY = XY + MOVIMIENTO_XY
    YX = YX + MOVIMIENTO_YX
    YY = YY + MOVIMIENTO_YY
    ZX = ZX + MOVIMIENTO_ZX
    ZY = ZY + MOVIMIENTO_ZY
    AX = AX + MOVIMIENTO_AX
    AY = AY + MOVIMIENTO_AY
    BX = BX + MOVIMIENTO_BX
    BY = BY + MOVIMIENTO_BY

# eje x

    if XX >= 960:
        XX = 960
        MOVIMIENTO_XX = -5

    elif XX <= 0:
        XX = 0
        MOVIMIENTO_XX = 5

    if YX >= 960:
        YX = 960
        MOVIMIENTO_YX = -5

    elif YX <= 0:
        YX = 0
        MOVIMIENTO_YX = 5

    if ZX >= 960:
        ZX = 960
        MOVIMIENTO_ZX = -5

    elif ZX <= 0:
        ZX = 0
        MOVIMIENTO_ZX = 5

    if AX >= 960:
        AX = 960
        MOVIMIENTO_AX = -5

    elif AX <= 0:
        AX = 0
        MOVIMIENTO_AX = 5

    if BX >= 960:
        BX = 960
        MOVIMIENTO_BX = -5

    elif BX <= 0:
        BX = 0
        MOVIMIENTO_BX = 5


# eje y
    if XY >= 660:
        XY = 660
        MOVIMIENTO_XY = -5

    elif XY <= 0:
        XY = 0
        MOVIMIENTO_XY = 5

    if YY >= 660:
        YY = 660
        MOVIMIENTO_YY = -5

    elif YY <= 0:
        YY = 0
        MOVIMIENTO_YY = 5

    if ZY >= 660:
        ZY = 660
        MOVIMIENTO_ZY = -5

    elif ZY <= 0:
        ZY = 0
        MOVIMIENTO_ZY = 5

    if AY >= 660:
        AY = 660
        MOVIMIENTO_AY = -5

    elif AY <= 0:
        AY = 0
        MOVIMIENTO_AY = 5

    if BY >= 660:
        BY = 660
        MOVIMIENTO_BY = -5

    elif BY <= 0:
        BY = 0
        MOVIMIENTO_BY = 5


    # dibujar rectangulo en ventana
    pygame.draw.rect(ventana, rojo, (XX,XY,40,40))
    pygame.draw.rect(ventana, rojo, (YX,YY,40,40))
    pygame.draw.rect(ventana, rojo, (ZX,ZY,40,40))
    pygame.draw.rect(ventana, rojo, (AX,AY,40,40))
    pygame.draw.rect(ventana, rojo, (BX,BY,40,40))
    # actualizar visualización de la ventana
    pygame.display.flip()