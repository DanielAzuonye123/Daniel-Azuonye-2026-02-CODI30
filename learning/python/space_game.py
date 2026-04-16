import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player_x = 250
player_y = 500
player_speed = 7

# Enemy
enemy_x = random.randint(0, WIDTH)
enemy_y = -50
enemy_speed = 5

score = 0
font = pygame.font.SysFont(None, 35)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -50
        enemy_x = random.randint(0, WIDTH)
        score += 1
        enemy_speed += 0.2

    # Collision
    if abs(player_x - enemy_x) < 40 and abs(player_y - enemy_y) < 40:
        running = False

    # Draw player + enemy
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 40, 40))
    pygame.draw.circle(screen, RED, (enemy_x, enemy_y), 20)

    # Score
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
