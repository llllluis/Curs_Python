import pygame
import sys
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite-based Collision Demo")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Load animation frames
def load_animation():
    frames = []
    for i in range(1, 6):
        path = f"C:/LLUIS/Dropbox/CODE/Python/Catch_fruits/IMG/StarHeart0{i}_play.png"
        image = pygame.image.load(path).convert_alpha()
        frames.append(pygame.transform.scale(image, (100, 100)))
    return frames

# 🧍‍♂️ Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, frames):
        super().__init__()
        self.frames = frames
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.frame_index = 0
        self.frame_delay = 15
        self.frame_counter = 0
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)

    def update(self, obstacles):
        keys = pygame.key.get_pressed()
        self.direction.x = self.direction.y = 0

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.direction.x = 1
        elif keys[pygame.K_UP] and self.rect.top > 0:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.direction.y = 1

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Animate only if moving
        if self.direction.length_squared() > 0:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame_counter = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]

        # Handle pushing and stopping fall on collision
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                obstacle.is_falling = False  # 🚨 Stop falling!
                if keys[pygame.K_SPACE]:
                    obstacle.push(self.direction)
        
        # Handle pushing and stopping fall on collision
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                obstacle.stop_falling_with_effects()  # 💥 visual + logic
                if keys[pygame.K_SPACE]:
                    obstacle.push(self.direction)



    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

# 🧱 Obstacle Class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w=100, h=100, fall_speed=1):
        super().__init__()
        self.width = w
        self.height = h
        self.color_state = (0, 0, 0)  # Default color black
        self.rect = pygame.Rect(x, y, w, h)

        self.fall_speed = fall_speed
        self.is_falling = True
        self.touched_time = None
        self.shake_timer = 0
        self.glow_border = False

    def update(self):
        # Resume falling after 3 seconds
        if not self.is_falling and self.touched_time:
            if pygame.time.get_ticks() - self.touched_time > 3000:
                self.is_falling = True
                self.touched_time = None
                self.color_state = (0, 0, 0)
                self.glow_border = False

        if self.is_falling:
            self.rect.y += self.fall_speed
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT
                self.is_falling = False

        # Shake effect
        if self.shake_timer > 0:
            self.shake_timer -= 1

    def push(self, direction):
        self.rect.x += direction.x * 10
        self.rect.y += direction.y * 10

    def stop_falling_with_effects(self):
    
        self.is_falling = False
        self.touched_time = pygame.time.get_ticks()
        self.color_state = (255, 0, 0)  # Red
        self.shake_timer = 10
        self.glow_border = True

    def draw(self, surface):
        # Shake offset
        offset_x = offset_y = 0
        if self.shake_timer > 0:
            offset_x = random.randint(-2, 2)
            offset_y = random.randint(-2, 2)

        draw_rect = self.rect.move(offset_x, offset_y)
        pygame.draw.rect(surface, self.color_state, draw_rect)
        
        # Glow border
        if self.glow_border:
            pygame.draw.rect(surface, (255, 0, 0), draw_rect, 4)

# === INIT ===
run_frames = load_animation()
player = Player(400, 0, run_frames)
obstacles = pygame.sprite.Group()

# Spawn some obstacles
for _ in range(5):
    ox = random.randint(100, 700)
    oy = random.randint(100, 400)
    obstacles.add(Obstacle(ox, oy))

# === GAME LOOP ===
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update logic
    screen.fill(WHITE)
    player.update(obstacles)
   

    # Draw everything
    for obstacle in obstacles:
        obstacle.update()
        obstacle.draw(screen)
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)
