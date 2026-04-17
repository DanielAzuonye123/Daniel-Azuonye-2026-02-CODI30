import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Upgrade Game")

WHITE = (255,255,255)
RED = (255,0,0)

clock = pygame.time.Clock()

# ================= IMAGES =================
player_img = pygame.image.load("learning/python/assets/player.png")
enemy_img = pygame.image.load("learning/python/assets/enemy.png")
bullet_img = pygame.image.load("learning/python/assets/bullet.png")
background_img = pygame.image.load("learning/python/assets/background.png")

# ================= PLAYER =================
player_x = WIDTH // 2
player_y = HEIGHT - 80
player_speed = 6
player_health = 3

# ================= GAME OBJECTS =================
bullets = []
enemy_bullets = []
enemies = []

bullet_speed = 10
enemy_speed = 3
enemy_bullet_speed = 5

score = 0
level = 1
game_state = "menu"

# ================= FUNCTIONS =================
def spawn_enemy():
    x = random.randint(0, WIDTH-40)
    enemies.append([x, -50])

for _ in range(5):
    spawn_enemy()

def shoot():
    bullets.append([player_x+20, player_y])

# ================= GAME LOOP =================
running = True
while running:

    screen.blit(background_img, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = "game"

        if game_state == "game":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                shoot()

    keys = pygame.key.get_pressed()

    # ================= MENU =================
    if game_state == "menu":
        font = pygame.font.SysFont(None, 60)
        screen.blit(font.render("SPACE SHOOTER", True, WHITE), (120, 200))
        screen.blit(pygame.font.SysFont(None, 40).render("Press ENTER", True, WHITE), (220, 300))

    # ================= GAME =================
    elif game_state == "game":

        # movement
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # bullets move
        for b in bullets:
            b[1] -= bullet_speed

        # enemy movement
        for e in enemies:
            e[1] += enemy_speed

        # enemy shooting
        if random.randint(1, 60) < 2:
            if enemies:
                e = random.choice(enemies)
                enemy_bullets.append([e[0]+20, e[1]+40])

        # enemy bullets move
        for b in enemy_bullets:
            b[1] += enemy_bullet_speed

        # COLLISION PLAYER BULLETS
        for b in bullets[:]:
            for e in enemies[:]:
                if abs(b[0]-e[0]) < 30 and abs(b[1]-e[1]) < 30:
                    bullets.remove(b)
                    enemies.remove(e)
                    spawn_enemy()
                    score += 10

        # COLLISION PLAYER HIT
        for b in enemy_bullets[:]:
            if abs(b[0]-player_x) < 30 and abs(b[1]-player_y) < 30:
                enemy_bullets.remove(b)
                player_health -= 1
                if player_health <= 0:
                    game_state = "gameover"

        # level system
        if score >= level * 100:
            level += 1
            enemy_speed += 1

        # DRAW PLAYER
        screen.blit(player_img, (player_x, player_y))

        # DRAW BULLETS
        for b in bullets:
            screen.blit(bullet_img, (b[0], b[1]))

        # DRAW ENEMIES
        for e in enemies:
            screen.blit(enemy_img, (e[0], e[1]))

        # DRAW ENEMY BULLETS
        for b in enemy_bullets:
            screen.blit(bullet_img, (b[0], b[1]))

        # UI
        font = pygame.font.SysFont(None, 35)
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10,10))
        screen.blit(font.render(f"Level: {level}", True, WHITE), (10,40))
        screen.blit(font.render(f"HP: {player_health}", True, WHITE), (10,70))

    # ================= GAME OVER =================
    elif game_state == "gameover":
        font = pygame.font.SysFont(None, 80)
        screen.blit(font.render("GAME OVER", True, RED), (120, 250))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
