import pygame
pygame.init()

# player
surf = pygame.Surface((40,40))
surf.fill((0,150,255))
pygame.image.save(surf, "learning/python/assets/player.png")

# enemy
surf = pygame.Surface((40,40))
surf.fill((255,50,50))
pygame.image.save(surf, "learning/python/assets/enemy.png")

# boss
surf = pygame.Surface((120,80))
surf.fill((200,0,200))
pygame.image.save(surf, "learning/python/assets/boss.png")

# bullet
surf = pygame.Surface((6,15))
surf.fill((255,255,0))
pygame.image.save(surf, "learning/python/assets/bullet.png")

# background
surf = pygame.Surface((600,700))
surf.fill((5,5,20))
pygame.image.save(surf, "learning/python/assets/background.png")

print("Assets created!")

