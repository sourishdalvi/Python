import pygame
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Demo Screen")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 40)
text = font.render("Welcome to Pygame!", True, BLACK)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (250, 200, 300, 150))
    pygame.draw.rect(screen, RED, (240, 190, 320, 170), 5)
    screen.blit(text, (200, 100))
    pygame.display.update()
pygame.quit()
sys.exit()