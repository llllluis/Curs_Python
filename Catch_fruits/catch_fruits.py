import pygame
import random
import re # Importar la librería re para expresiones regulares
import os
# Inicializar Pygame
pygame.init()
# inicializar el mixer de pygame para reproducir sonidos
pygame.mixer.init()
# carregar variables internes
# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0,0,255)
NARANJA = (255, 165, 0)
AMARILLO = (255, 255, 0)
# defenir velocitat de caiguda de los objetos
vel_x, vel_y = 4, 4  # Velocidades en X y Y
player_speed = 10 # Velocidad del jugador
score = 0 # Puntaje inicial 
OldScore=0 # Puntaje temporal
#################################################
#################################################
ConfigOption=2 # selecionar pantalla 1 o 2
#################################################
#################################################
PuntuacionMaxima=5
ActivePowerUp=False # Variable para activar el interrogante
# definir variables de configuracion externes
global screen_width
screen_width =0
global screen_height
screen_height=0
global Titulo
Titulo=""
global SoundFonfo
SoundFonfo=""
global SoundPowerUP
SoundPowerUP=""
global ImgPlayer
ImgPlayer=""
global ImgTarget1
ImgTarget1=""
global ImgTarget2
ImgTarget2=""
global ImgQuestion
ImgQuestion=""
global lives
lives = 0
global ConfigFile
ConfigFile=""
global directorio_actual
directorio_actual = ""
global ImgFonfo
ImgFonfo=""
global SounbColision
SounbColision=""
##############################
ruta_ejecutable = os.path.abspath(__file__)
directorio_actual = os.path.dirname(ruta_ejecutable)   
#ConfigFile="\AM1_setup.txt" 
##############################

# Leer el archivo .txt
def buscar_etiqueta(nombre_archivo, etiqueta):
    print(nombre_archivo)
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            coincidencia = re.match(f"\\[{etiqueta}\\] (.*)", linea)
            if coincidencia:
                return coincidencia.group(1)
    return None

# Función para animar la explosión
def animar_explosion(x, y):
    for i in range(5):  # Ciclo para generar la animación
        
        # Dibujar círculos de explosión de diferentes tamaños y colores
        pygame.draw.circle(screen, NARANJA, (x, y), 20 + i * 10)
        pygame.draw.circle(screen, AMARILLO, (x, y), 10 + i * 5)
        pygame.draw.circle(screen, ROJO, (x, y), 5 + i * 2)        
        pygame.display.flip()  # Actualizar pantalla
        pygame.time.delay(100)  # Pausa entre frames

def AnimarPowerUp(x,y):
    for i in range(5):

        # Dibujar círculos de explosión de diferentes tamaños y colores
        pygame.draw.circle(screen, AZUL, (x, y), 20 + i * 10)
        pygame.draw.circle(screen, ROJO, (x, y), 10 + i * 5)

        pygame.display.flip()  # Actualizar pantalla
        pygame.time.delay(100)  # Pausa entre frames

def EfectoTransicionPantalla():
    for i in range(100):  # Ciclo para generar la animación
        screen.fill(BLANCO)  # Limpiar la pantalla

        # Dibujar círculos de explosión de diferentes tamaños y colores
        pygame.draw.circle(screen, NARANJA, (0, 0), 20 + i * 10)
        pygame.draw.circle(screen, AMARILLO, (0, 0), 10 + i * 5)

        pygame.display.flip()  # Actualizar pantalla
        pygame.time.delay(30)  # Pausa entre frames
    pygame.time.delay(500)
    
def CargarVariablesdExternas():
    
    # carrgar variables de configuracion externes
    global screen_width
    screen_width=int(buscar_etiqueta(directorio_actual + ConfigFile,"ancho"))
    global screen_height
    screen_height=int(buscar_etiqueta(directorio_actual + ConfigFile,"alto"))
    global Titulo
    Titulo=buscar_etiqueta(directorio_actual + ConfigFile,"TITULO")
    global SoundFonfo
    SoundFonfo=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"SND_FONDO"))
    global SoundPowerUP
    SoundPowerUP=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"SND_POWER"))
    global ImgPlayer
    ImgPlayer=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"IMG_PLAYER"))
    global ImgTarget1
    ImgTarget1=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"IMG_TARGET1"))
    global ImgTarget2
    ImgTarget2=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"IMG_TARGET2"))
    global ImgQuestion
    ImgQuestion=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"IMG_QUESTION"))
    global lives
    lives = lives + int(buscar_etiqueta(directorio_actual + ConfigFile,"VIDAS"))
    global ImgFonfo    
    ImgFonfo=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"IMG_FONDO"))
    global SounbColision
    SounbColision=directorio_actual + str(buscar_etiqueta(directorio_actual + ConfigFile,"SND_COLISION"))

#CargarVariablesdExternas()
MainLoop=True
while MainLoop:
    PuntuacionMaxima=score+5
    #cargar fichero de configuracion
    if ConfigOption==1:        
        ConfigFile="\AM1_setup.txt" 
        CargarVariablesdExternas()
    elif ConfigOption==2:
        ConfigFile="\AM2_setup.txt"
        CargarVariablesdExternas()

    # Inicializar Pygame screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(Titulo)
  
    ############################## variables para animacion estrella
    fall_frames = []
    for i in range(1, 6):  # Asegúrate de tener fall1.png a fall4.png
        img = pygame.image.load(f"{directorio_actual}\IMG\StarHeart0{i}_play.png").convert_alpha()
        img = pygame.transform.scale(img, (60, 60))
        fall_frames.append(img)

    # Variables para la animación
    #clock = pygame.time.Clock()
    fall_size=fall_frames[1].get_size()
    fall_x = random.randint(0, screen_width - fall_size[0])
    fall_y = 0
    fall_speed = 3
    fall_frame_index = 0
    fall_frame_delay = 5
    fall_frame_counter = 0
    is_falling = True
    ############################## fin  variables para animacion estrella
    
    # Cargar imágenes
    player_image = pygame.image.load(ImgPlayer)
    player_image = pygame.transform.scale(player_image, (50, 50))  # Cambia el tamaño si es necesario

    target_image = pygame.image.load(ImgTarget1)
    target_image = pygame.transform.scale(target_image, (50, 50))  # Cambia el tamaño si es necesario

    target_image2 = pygame.image.load(ImgTarget2)
    target_image2 = pygame.transform.scale(target_image2, (50, 50))  # Cambia el tamaño si es necesario

    question_img = pygame.image.load(ImgQuestion)    
    question_img = pygame.transform.scale(question_img, (50, 50))  # Cambia el tamaño si es necesario

    # Cargar sonido de colision(debes tener un archivo "rebote.mp3" en la misma carpeta)
    sonido_rebote = pygame.mixer.Sound(SounbColision)
    sonido_PowerUp = pygame.mixer.Sound(SoundPowerUP)

    # Variables del juego
    player_size = player_image.get_size()
    target_size = target_image.get_size()
    target_size2=target_image2.get_size()
    question_img_size= question_img.get_size()

    player_pos = [screen_width // 2, screen_height // 2]
    target_pos = [random.randint(0, screen_width - target_size[0]), 0] 
    target_pos2 = [random.randint(0, screen_width - target_size2[0]), -100]
    question_img_pos = [screen_width , screen_height]
    

    # Cargar imagen de fondo (debe estar en la misma carpeta)
    fondo = pygame.image.load(ImgFonfo)
    fondo = pygame.transform.scale(fondo, (screen_width, screen_height))  # Escalar al tamaño de la ventana


    # Fuente para mostrar el puntaje
    font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 72)
    
    # Carga la canción de fondo (formato recomendado: .mp3 o .ogg)
    pygame.mixer.music.load(SoundFonfo)  # Asegúrate de que esté en la misma carpeta o pon la ruta completa
    pygame.mixer.music.set_volume(0.4)  # Volumen entre 0.0 y 1.0
    pygame.mixer.music.play(-1)  # -1 para que se repita en bucle

  
    # Bucle accion del juego
    running = True
    while running:        
        print("Is_FALLING" + str(is_falling))
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                MainLoop=False

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size[0]:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < screen_height - player_size[1]:
            player_pos[1] += player_speed

        # Animación del objeto que cae
        if is_falling:
            fall_y += fall_speed
            fall_frame_counter += 1
            if fall_frame_counter >= fall_frame_delay:
                fall_frame_counter = 0
                fall_frame_index = (fall_frame_index + 1) % len(fall_frames)

        # Crear rectángulos basados en imágenes para colisión
        player_rect = player_image.get_rect(topleft=(player_pos[0], player_pos[1]))
        target_rect = target_image.get_rect(topleft=(target_pos[0], target_pos[1]))
        target_rect2 = target_image2.get_rect(topleft=(target_pos2[0], target_pos2[1]))
        ImgQuestion_rect= question_img.get_rect(topleft=(question_img_pos[0], question_img_pos[1]))
        # Obtener imagen actual y su rectángulo
        current_fall_img = fall_frames[fall_frame_index]
        fall_rect = current_fall_img.get_rect(topleft=(fall_x, fall_y))

        # Comprobar colisión
        if player_rect.colliderect(target_rect):
            score += 1
            target_pos = [random.randint(0, screen_width - target_size[0]), 0]
            sonido_rebote.play(maxtime=500)  # Reproducir sonido

        if player_rect.colliderect(target_rect2):   
            score += 1
            target_pos2 = [random.randint(0, screen_width - target_size2[0]), 0]
            sonido_rebote.play(maxtime=500)  # Reproducir sonido
        
        if player_rect.colliderect(ImgQuestion_rect):             
           AnimarPowerUp(question_img_pos[0]+25,question_img_pos[1]+25)
           player_speed +=2
           question_img_pos = [screen_width, screen_height]
           sonido_PowerUp.play()

        # Detección de colisión con el player
        if fall_rect.colliderect(player_rect):
            is_falling = False
            fall_y = -100 #player_rect.top - fall_rect.height  # Ajuste para "tocar" el suelo            
            fall_x = random.randint(0, screen_width - fall_size[0])
            fall_frame_index = 0  # O dejar en el último frame
            EfectoTransicionPantalla()
                   
        if (score % 5)==0 and ActivePowerUp==False:         
            ActivePowerUp=True
            is_falling = True
            OldScore=score   
            question_img_pos = [random.randint(0, screen_width - target_size2[0]), 0]            
            vel_y +=1
            lives +=1            
            sonido_PowerUp.play()  # Reproducir sonido
        else:            
            if score != OldScore and ActivePowerUp==True:
                ActivePowerUp=False
                frame_index = 0
                
        

        # mover hacia abajo     
        target_pos = [target_pos[0], target_pos[1]+vel_y]
        target_pos2 = [target_pos2[0], target_pos2[1]+vel_y]
        question_img_pos = [question_img_pos[0], question_img_pos[1]+vel_y]
        fall_pos=[fall_x,fall_y]

        #colisión con el suelo
        if target_pos[1] >= screen_height-50:
            sonido_rebote.play(maxtime=500)  # Reproducir sonido
            animar_explosion(target_pos[0]+25,target_pos[1]+25)
            target_pos = [random.randint(0, screen_width - target_size[0]), 0]
            lives -= 1
            
        #colisión con el suelo
        if target_pos2[1] >= screen_height-50:
            sonido_rebote.play(maxtime=500)  # Reproducir sonido
            animar_explosion(target_pos2[0]+25,target_pos2[1]+25)
            target_pos2 = [random.randint(0, screen_width - target_size2[0]), 0]
            lives -= 1

        #colision animacion con el suelo
        if fall_pos[1]>=screen_height + 100:
            is_falling=False
            fall_y =  - 100
            fall_x = random.randint(0, screen_width - fall_size[0])
            fall_frame_index = 0  # O dejar en el último frame

        

        # Dibujar en pantalla        
        screen.blit(fondo, (0, 0))
        screen.blit(player_image, player_pos)
        screen.blit(target_image, target_pos)
        screen.blit(target_image2, target_pos2)
        screen.blit(question_img, question_img_pos)
        screen.blit(current_fall_img, (fall_x, fall_y))

        # Mostrar el puntaje
        score_text = font.render("Score: " + str(score), True, (0, 0, 0),(255,0,255))
        screen.blit(score_text, (10, 10))

        # Mostrar vides
        lives_text = font.render("Lives: " + str(lives), True, (0, 0, 0),(255,255,0))
        screen.blit(lives_text, (screen_width - 100, 10))

        
        #if score >= PuntuacionMaxima:
        #    if ConfigOption==1:
        #        ConfigOption=2
        #    elif ConfigOption==2:
        #        ConfigOption=1
        #    EfectoTransicionPantalla()
            #salir del bucle secundario
        #    running=False

        if lives <=0:
            running=False
            MainLoop=False
       

        # Actualizar la pantalla
        pygame.display.flip()

        # Control de FPS
        pygame.time.Clock().tick(30)

# animacion final game over
alpha = 1000
game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
game_over_surface = pygame.Surface(game_over_text.get_size(), pygame.SRCALPHA)

for i in range(255):
    game_over_surface.fill((0, 0, 0, 0))
    game_over_surface.blit(game_over_text, (0, 0))
    game_over_surface.set_alpha(alpha)
    screen.blit(fondo, (0, 0))
    screen.blit(game_over_surface, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (screen_width - 100, 10))
    pygame.display.flip()
    alpha += 1
    pygame.time.delay(10)
# Salir de Pygame
pygame.time.delay(2000)
pygame.quit()
