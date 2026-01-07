import pygame 
import random
SCREENWIDTH,SCREENHIEGHT=500,400
MOVEMENTSPEED=5
FONTSIZE=72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load('img34.png'),

(SCREENWIDTH, SCREENHIEGHT))
font=pygame.font.SysFont("Times Tew Roman",FONTSIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,hieght,width):
        super().__init__()
        self.image=pygame.Surface([width,hieght])
        self.image.fill(pygame.Color('green'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,hieght))
        self.rect=self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x=max(min(self.rect.x+xchange,SCREENWIDTH-self.rect.width),0)
        self.rect.x=max(min(self.rect.y+ychange,SCREENHIEGHT-self.rect.height),0)
screen=pygame.display.set_mode((SCREENWIDTH,SCREENHIEGHT))
pygame.display.set_caption("sprite collison")
allsprites=pygame.sprite.Group()
sprite1=Sprite(pygame.Color('black'),25,25)
sprite1.rect.x,sprite1.rect.y=random.randint(0,SCREENWIDTH-sprite1.rect.width),random.randint(
    0,SCREENHIEGHT-sprite1.rect.height)
allsprites.add(sprite1)
sprite2=Sprite(pygame.Color('red'),25,25)
sprite2.rect.x,sprite2.recty=random.randint(0,SCREENWIDTH-sprite1.rect.width),random.randint(
    0,SCREENHIEGHT-sprite1.rect.height)
allsprites.add(sprite2)
running,won=True,False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or( event.type==pygame.KEYDOWN and event.key==pygame.K_x):
            runninge=False
    if not won:
        keys=pygame.key.get_pressed()
        xchange=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*MOVEMENTSPEED
        ychange=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*MOVEMENTSPEED
        sprite1.move(xchange,ychange)
        if sprite1.rect.colliderect(sprite2.rect):
            allsprites.remove()
            won=True
    screen.blit(background_image,(0,0))
    allsprites.draw(screen)
    if won:
        wintext=font.render("you win",True,pygame.Color('black'))
        screen.blit(wintext,((SCREENWIDTH-wintext.get_width)//2,((SCREENWIDTH-wintext.get_height)//2)))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()
