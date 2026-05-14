import pygame, sys

pygame.init()

pantalla = pygame.display.set_mode((370, 442))
pygame.display.set_caption("Mario Bros")
NEGRO = (0, 0, 0)
pantalla.fill(NEGRO)

mario = pygame.image.load("assets/images/mario03.png").convert()

pantalla.blit(mario, (5,5))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
