import pygame
pygame.init()
ventana = pygame.display.set_mode((1080, 690))
pygame.display.set_caption("OMG")

azul = (13, 94, 175)
blanco = (255, 255, 255)

#piezas

superficie_1 = pygame.Surface((1080, 76.6666))
superficie_1.fill(blanco)
superficie_2 = pygame.Surface((1080, 76.6666))
superficie_2.fill(blanco)
superficie_3 = pygame.Surface((76.6666, 383.3333))
superficie_3.fill(blanco)
superficie_4 = pygame.Surface((383.3333, 76.6666))
superficie_4.fill(blanco)
superficie_5 = pygame.Surface((696.6664, 76.6666))
superficie_5.fill(blanco)
superficie_6 = pygame.Surface((696.6664, 76.6666))
superficie_6.fill(blanco)

ventana.fill(azul)
ventana.blit(superficie_1, (0, 536.6662))
ventana.blit(superficie_2, (0, 383.3333))
ventana.blit(superficie_3, (150, 0))
ventana.blit(superficie_4, (0, 153.3332))
ventana.blit(superficie_5, (383.3333, 76.6666))
ventana.blit(superficie_6, (383.3333, 229.9998))
pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
pygame.quit()