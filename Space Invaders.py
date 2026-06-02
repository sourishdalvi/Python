import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Space Invaders")
bg = pygame.image.load("Death Star Interior.jpg")
bg = pygame.transform.scale(bg, (800, 500))
playerimg = pygame.image.load("download (3).jpg")
playerimg = pygame.transform.scale(playerimg, (64, 64))
playerX = 370
playerY = 420
player_change = 0
enemyimg = pygame.image.load("download (4).jpg")
enemyimg = pygame.transform.scale(enemyimg, (64, 64))
enemyX = random.randint(0, 736)
enemyY = 50
enemy_change = 4
bulletimg = pygame.image.load("download (5).jpg")
bulletimg = pygame.transform.scale(bulletimg, (16, 32))
bulletX = 0
bulletY = playerY
bullet_change = 10
bullet_state = "ready"
def player(x, y):
    screen.blit(playerimg, (x, y))
def enemy(x, y):
    screen.blit(enemyimg, (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 24, y))
running = True
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -5
            if event.key == pygame.K_RIGHT:
                player_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0
    playerX += player_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    enemyX += enemy_change
    if enemyX <= 0:
        enemy_change = 4
        enemyY += 40
    if enemyX >= 736:
        enemy_change = -4
        enemyY += 40
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_change
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
pygame.quit()