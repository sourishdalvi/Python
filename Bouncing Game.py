import pygame 
import random
pygame.init()
screen=pygame.display.set_mode((500,400))
pygame.display.set_captio("Moving Sprite")
clock=pygame.time.Clock()
bg_colours=["Blue,""Lightblue","Darkblue",]
Sprite_colours=["Yellow,""Magenta","Orange","White"]
bg_colour="blue"
sprite=pygame.Rect(100,100,30,20)
sprite_colour="White"
dx=4
dy=4
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    sprite.x+=dx
    sprite.y+=dy
    if sprite.left<=0 or sprite.right>=500:
        dx=-dx
        bg_colour=random.choice(bg_colours)
        sprite_colour=random.choice(Sprite_colours)
    if sprite.top<=0 or sprite.bottom>=400:
        dy=-dy
        sprite_colour=random.choice(Sprite_colours)
        bg_colour=random.choice(bg_colours)
    screen.fill(bg_colour)
    pygame.draw.rect(screen,sprite_colour,sprite)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
