# importamos la libreria pygame
import pygame
import sys
import random
from PIL import Image

# Inicializamos la librería
pygame.init()

# Ventana
ventana = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Rebotes Imagen Random")

# --- Configuración ---
IMAGE_PATH = "image/image.png" 

# Definimos el tamaño aquí
ANCHO_IMG = 250
ALTO_IMG = 200

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_pygame_image(color):
    img = Image.open(IMAGE_PATH).convert("RGBA")
    color_layer = Image.new("RGBA", img.size, color)
    # Mantiene la transparencia original usando el canal alfa como máscara
    colored_img = Image.composite(color_layer, img, img) 
    
    # Conversión técnica de Pillow a Pygame
    surface = pygame.image.fromstring(colored_img.tobytes(), colored_img.size, colored_img.mode)
    
    # --- AGREGADO: CAMBIO DE TAMAÑO ---
    surface = pygame.transform.scale(surface, (ANCHO_IMG, ALTO_IMG))
    
    return surface

# --- Variables iniciales ---
negro = (0,0,0)
XX = 50
XY = 150
MOVIMIENTO_XX = 5
MOVIMIENTO_XY = 5

# Cargamos la primera imagen y configuramos el tiempo
current_image = get_pygame_image(get_random_color())
ultimo_cambio = pygame.time.get_ticks()

clock = pygame.time.Clock()

# Bucle principal
while True:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento
    XX = XX + MOVIMIENTO_XX
    XY = XY + MOVIMIENTO_XY

    # Rebotes Eje X 
    # (Ajustado para que rebote según el ancho de la ventana y el tamaño de la imagen)
    if XX >= (800):
        XX = (800)
        MOVIMIENTO_XX = -5
        current_image = get_pygame_image(get_random_color())
    elif XX <= -50:
        XX = -50
        MOVIMIENTO_XX = 5
        current_image = get_pygame_image(get_random_color())

    # Rebotes Eje Y
    # (Ajustado para que rebote según el alto de la ventana y el tamaño de la imagen)
    if XY >= (550):
        XY = (550)
        MOVIMIENTO_XY = -5
        current_image = get_pygame_image(get_random_color())
    elif XY <= -60:
        XY = -60
        MOVIMIENTO_XY = 5
        current_image = get_pygame_image(get_random_color())

    ventana.fill(negro)

    # --- LO QUE PONES EN EL BLIT ---
    ventana.blit(current_image, (XX, XY))
    
    pygame.display.flip()