import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Onda expansiva")

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Suelo
ground_rect = pygame.Rect(0, 550, WIDTH, 50)

# Cargar animación de objeto que cae
fall_frames = []
for i in range(1, 5):
    img = pygame.image.load(f"C:\LLUIS\Dropbox\CODE\Python\Catch_fruits\IMG\StarHeart0{i}_play.png").convert_alpha()
    img = pygame.transform.scale(img, (50, 50))
    fall_frames.append(img)

# Objeto que cae
fall_x, fall_y = 400, 0
fall_speed = 4
fall_frame_index, fall_frame_delay, fall_frame_counter = 0, 5, 0
is_falling = True
exploded = False
explosion_radius = 150

# Jugador (no afectado por explosión)
player_rect = pygame.Rect(400, 450, 50, 100)

# Objetivos a derribar
targets = [
    {"rect": pygame.Rect(200, 450, 50, 100), "alive": True},
    {"rect": pygame.Rect(500, 450, 50, 100), "alive": True},
    {"rect": pygame.Rect(650, 450, 50, 100), "alive": True}
]

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del objeto que cae
    if is_falling:
        fall_y += fall_speed
        fall_frame_counter += 1
        if fall_frame_counter >= fall_frame_delay:
            fall_frame_counter = 0
            fall_frame_index = (fall_frame_index + 1) % len(fall_frames)

    current_fall_img = fall_frames[fall_frame_index]
    fall_rect = current_fall_img.get_rect(topleft=(fall_x, fall_y))

    # Detección de colisión con el suelo
    if fall_rect.colliderect(ground_rect) and not exploded:
        is_falling = False
        fall_y = ground_rect.top - fall_rect.height
        exploded = True

        # Onda expansiva
        explosion_center = fall_rect.center
        for target in targets:
            if not target["alive"]:
                continue
            target_center = target["rect"].center

            distance = math.dist(explosion_center, target_center)
            if distance <= explosion_radius:
                if not player_rect.colliderect(target["rect"]):  # Ignorar jugador
                    target["alive"] = False  # Derribar

    # Dibujar suelo
    pygame.draw.rect(screen, GRAY, ground_rect)

    # Dibujar jugador (no afectado)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Dibujar targets
    for target in targets:
        if target["alive"]:
            pygame.draw.rect(screen, RED, target["rect"])
        else:
            pygame.draw.line(screen, RED, target["rect"].topleft, target["rect"].bottomright, 2)
            pygame.draw.line(screen, RED, target["rect"].topright, target["rect"].bottomleft, 2)

    # Dibujar objeto que cae
    if not exploded:
        screen.blit(current_fall_img, (fall_x, fall_y))
    else:
        # Onda expansiva visual
        pygame.draw.circle(screen, GREEN, explosion_center, explosion_radius, 2)

    pygame.display.update()
    clock.tick(60)
