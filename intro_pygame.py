import pygame
pygame.init()
ventana = pygame.display.set_mode((1360, 720))
pygame.display.set_caption("OMG")

negro = (0, 0, 0)
blanco = (255, 255, 255)

superficie_1_negro = pygame.Surface((100, 500))
superficie_1_negro.fill(negro)
superficie_2_negro = pygame.Surface((500, 100))
superficie_2_negro.fill(negro)

#patas
superficie_3_negro = pygame.Surface((100, 250))
superficie_3_negro.fill(negro)
superficie_4_negro = pygame.Surface((100, 250))
superficie_4_negro.fill(negro)
superficie_5_negro = pygame.Surface((250, 100))
superficie_5_negro.fill(negro)
superficie_6_negro = pygame.Surface((250, 100))
superficie_6_negro.fill(negro)

ventana.fill(blanco)
ventana.blit(superficie_1_negro, (630, 110))
ventana.blit(superficie_2_negro, (430, 310))
ventana.blit(superficie_3_negro, (430, 360))
ventana.blit(superficie_4_negro, (830, 110))
ventana.blit(superficie_5_negro, (680, 510))
ventana.blit(superficie_6_negro, (430, 110))
pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
pygame.quit()
