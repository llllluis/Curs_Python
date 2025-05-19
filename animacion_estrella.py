import pygame
import sys

pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimiento 4 direcciones + Colisión")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Cargar animaciones
run_frames = []
for i in range(1, 6):
    #image = pygame.image.load(f"D:\projectes_programacio\Curs_Python\Catch_fruits\IMG\StarHeart0{i}_play.png").convert_alpha()
    image = pygame.image.load(f"C:\LLUIS\Dropbox\CODE\Python\Catch_fruits\IMG\StarHeart0{i}_play.png").convert_alpha()
    run_frames.append(pygame.transform.scale(image, (100, 100)))

# Variables del personaje
x, y = 400, 300
width, height = 100, 100
frame_index = 0
frame_delay = 5
frame_counter = 0
moving = False

# Rectángulo del obstáculo
obstacle_rect = pygame.Rect(200, 300, 100, 100)

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    moving = False

    # Movimiento en 4 direcciones
    if keys[pygame.K_LEFT]:
        x -= 5
        moving = True
    if keys[pygame.K_RIGHT]:
        x += 5
        moving = True
    if keys[pygame.K_UP]:
        y -= 5
        moving = True
    if keys[pygame.K_DOWN]:
        y += 5
        moving = True

    # Control de animación
    if moving:
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0
            frame_index = (frame_index + 1) % len(run_frames)
    else:
        frame_index = 0

    # Rectángulo del jugador
    player_rect = pygame.Rect(x, y, width, height)

    # Comprobar colisión
    if player_rect.colliderect(obstacle_rect):
        obstacle_color = RED
    else:
        obstacle_color = BLACK

    # Dibujar personaje y obstáculo
    screen.blit(run_frames[frame_index], (x, y))
    pygame.draw.rect(screen, obstacle_color, obstacle_rect)

    pygame.display.update()
    clock.tick(60)