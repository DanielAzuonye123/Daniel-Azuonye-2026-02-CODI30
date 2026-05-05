import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
PURPLE = (200,0,200)
YELLOW = (255,255,0)

clock = pygame.time.Clock()

# ================= LOADERS =================
def load_image(path, size=None):
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.scale(img, size)
        return img
    surf = pygame.Surface((40,40))
    surf.fill((255,0,0))
    return surf

def load_sound(path):
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    return None

# ================= IMAGES =================
player_img = load_image("learning/python/assets/player.png", (60,60))
enemy_img = load_image("learning/python/assets/enemy.png", (50,50))
bullet_img = load_image("learning/python/assets/bullet.png", (12,24))
background_img = load_image("learning/python/assets/background.png", (WIDTH,HEIGHT))

# ================= PLAYER =================
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 6
player_health = 5
player_upgrade = 1

# ================= OBJECTS =================
bullets = []
enemies = []
powerups = []
enemy_bullets = []

bullet_speed = 10
enemy_speed = 2

score = 0
level = 1
level_timer = 0

game_state = "menu"

# ================= SPAWN =================
def spawn_enemy():
    x = random.randint(0, WIDTH-50)
    enemies.append([x, -50, 2])  # x y hp

for _ in range(5):
    spawn_enemy()

# ================= SHOOT =================
def shoot():
    # bullet from player center
    bullets.append([player_x + 24, player_y])

# ================= LOOP =================
running = True
while running:

    screen.blit(background_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "game"

        elif game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot()

    keys = pygame.key.get_pressed()

    # ================= MENU =================
    if game_state == "menu":

        font = pygame.font.SysFont(None,60)
        text = font.render("SPACE SHOOTER",True,WHITE)
        screen.blit(text,(120,200))

        font2 = pygame.font.SysFont(None,30)
        screen.blit(font2.render("Press ENTER",True,WHITE),(220,300))

    # ================= GAME =================
    elif game_state == "game":

        # movement
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # bullets
        for b in bullets:
            b[1] -= bullet_speed

        # enemies
        for e in enemies:
            e[1] += enemy_speed

        # bullet hit enemy
        for b in bullets[:]:
            for e in enemies[:]:
                if pygame.Rect(b[0],b[1],12,24).colliderect(
                   pygame.Rect(e[0],e[1],50,50)):

                    bullets.remove(b)
                    e[2] -= 1

                    if e[2] <= 0:
                        enemies.remove(e)
                        spawn_enemy()
                        score += 10

        # enemy hit player
        for e in enemies:
            if pygame.Rect(player_x,player_y,60,60).colliderect(
               pygame.Rect(e[0],e[1],50,50)):

                player_health -= 1
                e[1] = -50

        # spawn powerups
        if random.randint(1,400) == 1:
            powerups.append([random.randint(0,WIDTH-20),-20])

        # move powerups
        for p in powerups:
            p[1] += 3

        # pickup
        for p in powerups[:]:
            if pygame.Rect(player_x,player_y,60,60).colliderect(
               pygame.Rect(p[0],p[1],20,20)):
                powerups.remove(p)
                player_upgrade += 1

        # level up
        if score >= level * 50:
            level += 1
            enemy_speed += 0.5
            level_timer = 120

        # draw player
        screen.blit(player_img,(player_x,player_y))

        # draw bullets
        for b in bullets:
            screen.blit(bullet_img,(b[0],b[1]))

        # draw enemies
        for e in enemies:
            screen.blit(enemy_img,(e[0],e[1]))

        # draw powerups
        for p in powerups:
            pygame.draw.rect(screen,GREEN,(p[0],p[1],20,20))

        # UI
        font = pygame.font.SysFont(None,30)

        screen.blit(font.render(f"Score: {score}",True,WHITE),(10,10))
        screen.blit(font.render(f"Level: {level}",True,WHITE),(10,40))
        screen.blit(font.render(f"HP: {player_health}",True,WHITE),(10,70))

        # LEVEL TEXT
        if level_timer > 0:
            level_timer -= 1
            big = pygame.font.SysFont(None,70)
            screen.blit(big.render(f"LEVEL {level}",True,YELLOW),(180,300))

        # game over
        if player_health <= 0:
            game_state = "gameover"

    # ================= GAME OVER =================
    elif game_state == "gameover":
        font = pygame.font.SysFont(None,80)
        screen.blit(font.render("GAME OVER",True,RED),(120,250))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
