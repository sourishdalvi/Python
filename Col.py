import pygame
import random
pygame.init()
WIDTH,HEIGHT=500,400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sprite Collision")
BG_COLOUR=(173,216,230)
font=pygame.font.SysFont("Arial",50)
class Sprite(pygame.sprite.Sprite):
  def __init__(self,colour):
    super().__init__()
    self.image=pygame.Surface((30,20))
    self.image.fill(colour)
    self.rect=self.image.get_rect()
  def move(self,x,y):
      self.rect.x+=x
      self.rect.y+=y
player=Sprite("Black")
player.rect.x=random.randint(0,WIDTH-30)
player.rect.y=random.randint(0,HEIGHT-20)
enemy=Sprite("red")
enemy.rect.x=random.randint(0,WIDTH-30)
enemy.rect.y=random.randint(0,HEIGHT-20)
sprites=pygame.sprite.Group()
sprites.add(player,enemy)
enemy2=Sprite("red")
enemy2.rect.x=random.randint(0,WIDTH-30)
enemy2.rect.y=random.randint(0,HEIGHT-20)
sprites.add(enemy2)
enemy3=Sprite("red")
enemy3.rect.x=random.randint(0,WIDTH-30)
enemy3.rect.y=random.randint(0,HEIGHT-20)
sprites.add(enemy3)
enemy4=Sprite("red")
enemy4.rect.x=random.randint(0,WIDTH-30)
enemy4.rect.y=random.randint(0,HEIGHT-20)
sprites.add(enemy4)
enemy5=Sprite("red")
enemy5.rect.x=random.randint(0,WIDTH-30)
enemy5.rect.y=random.randint(0,HEIGHT-20)
sprites.add(enemy5)
enemy6=Sprite("red")
enemy6.rect.x=random.randint(0,WIDTH-30)
enemy6.rect.y=random.randint(0,HEIGHT-20)
sprites.add(enemy6)
enemy7=Sprite("red")
enemy7.rect.x=random.randint(0,WIDTH-30)
enemy7.rect.y=random.randint(0,HEIGHT-20)
sprites.add(enemy7)
running=True
won=False
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  player.move(-5, 0)
        if keys[pygame.K_RIGHT]: player.move(5, 0)
        if keys[pygame.K_UP]:    player.move(0, -5)
        if keys[pygame.K_DOWN]:  player.move(0, 5)
        for enemy in [enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7]:
            if player.rect.colliderect(enemy.rect):
                sprites.remove(enemy)
        if len(sprites) == 2:   
            won = True
    screen.fill(BG_COLOUR)
    sprites.draw(screen)
    if won:
        text = font.render("You Win", True, (0, 0, 0))
        screen.blit(text, (150, 150))
    pygame.display.update()
    clock.tick(60)
pygame.quit()