import pygame
import sys

pygame.init()

# Pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Objeto animado que cae")

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Suelo
ground_rect = pygame.Rect(0, 550, WIDTH, 50)

# Cargar animación del objeto que cae
fall_frames = []
for i in range(1, 6):  # Asegúrate de tener fall1.png a fall4.png
    #img = pygame.image.load(f"D:\projectes_programacio\Curs_Python\Catch_fruits\IMG\StarHeart0{i}_play.png").convert_alpha()
    img = pygame.image.load(f"C:\LLUIS\Dropbox\CODE\Python\Catch_fruits\IMG\StarHeart0{i}_play.png").convert_alpha()
    img = pygame.transform.scale(img, (100, 100))
    fall_frames.append(img)

# Variables del objeto que cae
fall_x = 300
fall_y = 0
fall_speed = 3
fall_frame_index = 0
fall_frame_delay = 8
fall_frame_counter = 0
is_falling = True

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    # Movimiento en 4 direcciones
    if keys[pygame.K_LEFT]:
        fall_x -= fall_speed
        print("izquierda")

    if keys[pygame.K_RIGHT]:
        fall_x += fall_speed
        print
    if keys[pygame.K_UP]:
        fall_y -= fall_speed
        print
    if keys[pygame.K_DOWN]:
        fall_y += fall_speed
        print("abajo")

    # Animación del objeto que cae
    if is_falling:
        fall_y += fall_speed
        fall_frame_counter += 1
        if fall_frame_counter >= fall_frame_delay:
            fall_frame_counter = 0
 #          fall_frame_index = (fall_frame_index + 1) % len(fall_frames)
            fall_frame_index = (fall_frame_index + 1)
            if fall_frame_index >= len(fall_frames):
                fall_frame_index = 0

    current_fall_img = fall_frames[fall_frame_index]
    fall_rect = current_fall_img.get_rect(topleft=(fall_x, fall_y))

   
    # Detección de colisión con el suelo
    if fall_rect.colliderect(ground_rect):
        is_falling = False
        fall_y = ground_rect.top - fall_rect.height  # Ajuste para "tocar" el suelo
        fall_frame_index = 0  # O dejar en el último frame
        ground_color = WHITE
    else:
        ground_color = GRAY

    # Dibujar suelo
    pygame.draw.rect(screen, ground_color, ground_rect)

    # Dibujar objeto que cae
    screen.blit(current_fall_img, (fall_x, fall_y))

    pygame.display.update()
    clock.tick(60)
