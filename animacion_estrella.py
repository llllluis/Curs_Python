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
x, y = 400, 0
width, height = 100, 100
frame_index = 0
frame_delay = 15
frame_counter = 0
moving = False
fall_speed = 0
is_falling = True
# Rectángulo del obstáculo
obstacle_rect = pygame.Rect(400, 200, 100, 100)
obstacle_color = BLACK
clock = pygame.time.Clock()
EmpujarCuadrado = ""
is_touching = False
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    moving = False
    
    # Movimiento en 4 direcciones
    if keys[pygame.K_LEFT]  and x>=0:
        x -= 5
        moving = True
        is_falling = False
        EmpujarCuadrado = "izquierda"
        if is_touching:
            obstacle_rect.x -= 5  # Mover obstáculo si hay colisión
    elif keys[pygame.K_RIGHT]  and x<=WIDTH-100:
        x += 5
        moving = True
        is_falling = False
        EmpujarCuadrado = "derecha"
        if is_touching:
            obstacle_rect.x += 5  # Mover obstáculo si hay colisión
    elif keys[pygame.K_UP]  and y>=0:
        y -= 5
        moving = True
        is_falling = False
        EmpujarCuadrado = "arriba"
        if is_touching:
            obstacle_rect.y -= 5  # Mover obstáculo si hay colisión
    elif keys[pygame.K_DOWN] and y<=HEIGHT-100:
        y += 5
        moving = True        
        is_falling = False
        EmpujarCuadrado = "abajo"
        if is_touching:
            obstacle_rect.y += 5  # Mover obstáculo si hay colisión
    
    # Si se pulsa la tecla espacio, reiniciar posición y estado
    if keys[pygame.K_SPACE] and is_touching:
       
        if EmpujarCuadrado == "izquierda":
                #obstacle_rect.x, obstacle_rect.y = obstacle_rect.x-10, obstacle_rect.y
                obstacle_rect.x, obstacle_rect.y = obstacle_rect.x-10, obstacle_rect.y
            #is_falling = True
                print("izquierda")
        elif EmpujarCuadrado == "derecha":
                obstacle_rect.x, obstacle_rect.y = obstacle_rect.x+20, obstacle_rect.y
                print("derecha")
        elif EmpujarCuadrado == "arriba":
                obstacle_rect.x, obstacle_rect.y = obstacle_rect.x, obstacle_rect.y-10
                print("arriba") 
        elif EmpujarCuadrado == "abajo":
                obstacle_rect.x, obstacle_rect.y = obstacle_rect.x, obstacle_rect.y+10
                print("abajo")  
        #obstacle_color = BLACK
    # Control de animación
    print(EmpujarCuadrado)
    if moving:
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0
            frame_index = (frame_index + 1) % len(run_frames)
   

    # Animación del objeto que cae
    if is_falling:        
        #y += fall_speed
        obstacle_rect.y += fall_speed
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_counter = 0 
            frame_index = (frame_index + 1)
            if frame_index >= len(run_frames):
                frame_index = 0

    current_img = run_frames[frame_index]
    # Rectángulo del jugador
    player_rect = pygame.Rect(x, y, width, height)

    # Comprobar colisión
    if player_rect.colliderect(obstacle_rect): # or y >= HEIGHT - 100:
        obstacle_color = current_img.get_at((50, 10))  # Color del obstáculo
        #obstacle_rect.y = y + 5
        #obstacle_rect.x = x + 5
        #obstacle_rect.y += 5
        #obstacle_rect.x += 5


        if EmpujarCuadrado == "izquierda":
                obstacle_rect.x, obstacle_rect.y = player_rect.x - player_rect.width, player_rect.y               
                print("izquierda")
        elif EmpujarCuadrado == "derecha":
                obstacle_rect.x, obstacle_rect.y = player_rect.x + player_rect.width, player_rect.y
                print("derecha")
        elif EmpujarCuadrado == "arriba":
                obstacle_rect.x, obstacle_rect.y = player_rect.x, player_rect.y-player_rect.height
                print("arriba") 
        elif EmpujarCuadrado == "abajo":
                obstacle_rect.x, obstacle_rect.y = player_rect.x, player_rect.y + player_rect.height
                print("abajo")  


        is_falling = False
        is_touching = True
    else:
        #obstacle_color = BLACK
        is_touching = False
        is_falling = True



    # Dibujar personaje y obstáculo
    
    pygame.draw.rect(screen, obstacle_color, obstacle_rect)
    screen.blit(current_img, (x, y))

    pygame.display.update()
    clock.tick(60)