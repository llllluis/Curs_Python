import pygame
import sys

pygame.init()

# Pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TAC ABDOMINAL - 16 maig 2025")

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
 # Fuente para mostrar los frames
font = pygame.font.Font(None, 24)
#var.rango fotos
INICIAL = 268
FINAL = 446 # tac2=390 | tac1=535
# Cargar animación del objeto que cae
fall_frames = []
for i in range(INICIAL, FINAL):  # Asegúrate de tener fall1.png a fall4.png
    #img = pygame.image.load(f"D:\projectes_programacio\Curs_Python\Catch_fruits\IMG\StarHeart0{i}_play.png").convert_alpha()
    # tac1  --> img = pygame.image.load(f"C:\LLUIS\Dropbox\lluis\ADESLAS\TAC abdominal\RESULTAT_TAC\IMAGES\TACS\TAC1\TAC1_ABDOMINAL ({i}).jpg").convert_alpha()
    # tac2 --> img = pygame.image.load(f"C:\LLUIS\Dropbox\lluis\ADESLAS\TAC abdominal\RESULTAT_TAC\IMAGES\TACS\TAC2\TAC2_ABDOMINAL ({i}).jpg").convert_alpha()
    img = pygame.image.load(f"C:\LLUIS\Dropbox\lluis\ADESLAS\TAC abdominal\RESULTAT_TAC\IMAGES\TACS\TAC3\TAC3_ABDOMINAL ({i}).jpg").convert_alpha()
    img = pygame.transform.scale(img, (512, 512))
    fall_frames.append(img)

# Variables del objeto que cae
fall_x = (WIDTH/2)-(512/2)
fall_y = (HEIGHT/2)-(512/2)
fall_speed = 0
fall_frame_index = 0
fall_frame_delay = 10
fall_frame_counter = 0
is_playing = True

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
        fall_frame_index -= 1
        if fall_frame_index < 0:
            fall_frame_index = len(fall_frames) - 1
        pygame.time.delay(75)  # Pausa entre frames
    if keys[pygame.K_RIGHT]:
        fall_frame_index += 1
        if fall_frame_index >= len(fall_frames):
            fall_frame_index = 0
        pygame.time.delay(75)  # Pausa entre frames

        
    if keys[pygame.K_UP]:        
        is_playing = True
    if keys[pygame.K_DOWN]:        
        is_playing =False

    # Animación del objeto que cae
    if is_playing:
        fall_y += fall_speed
        fall_frame_counter += 1
        if fall_frame_counter >= fall_frame_delay:
            fall_frame_counter = 0 
            fall_frame_index = (fall_frame_index + 1)
            if fall_frame_index >= len(fall_frames):
                fall_frame_index = 0
    else:
        if fall_frame_index >= len(fall_frames) or fall_frame_index < 0:
            fall_frame_index = 0

    current_fall_img = fall_frames[fall_frame_index]
    fall_rect = current_fall_img.get_rect(topleft=(fall_x, fall_y))

    # Mostrar frames
    frames_text = font.render("Frames: " + str(fall_frame_index), True, (0, 0, 0),(255,255,155))
    screen.blit(frames_text, (WIDTH - 120, 10))
    # Dibujar objeto que cae
    screen.blit(current_fall_img, (fall_x, fall_y))

    pygame.display.update()
    clock.tick(60)