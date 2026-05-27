import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Space Invaders")
bg=pygame.image.load("background.jpeg")
playerimg=pygame.image.load("player.png")
enemyimg=pygame.image.load("enemy.png")
bulletimg=pygame.image.load("bullet.png")
playerX=370
playerY=480
player_change=0
