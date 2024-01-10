import math
from pickle import TRUE
from platform import platform
from hitbox import hitbox
import sys
import pygame



WIDTH=1440
HEIGHT=700
BLACK = (0, 0, 0)
BGC=(60,60,60)
WHITE=(255,255,255)
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 150
RED=(255,0,0)
GRAY=(169,169,169)
clock=pygame.time.Clock()




FPS=240
firexpos=1300
icexpos=-20

fireypos=500
iceypos=500

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stickfight")

hitbox_1 = hitbox(1350,500)
hitbox_2 = hitbox(15,500)

bg=pygame.image.load("images/spiel/Background.png")
bg=pygame.transform.scale(bg,(1440,700))

plattform=pygame.image.load("images/spiel/plattform.png")
plattform=pygame.transform.scale(plattform, (1440, 115))


running = True

while running:
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # if event.key==pygame.K_w:
            #     counterice = 0
            #     icejumping=True
            #     icestanding=False
            # if event.key==pygame.K_UP:
            #     firejumping=True
            #     firestanding=False
            # if event.key==pygame.K_LEFT:
            #     fireleft=True
            #     firestanding=False
    screen.fill(WHITE)
    screen.blit(bg,pygame.rect.Rect(0,0, 128, 128))
    
    screen.blit(plattform,pygame.rect.Rect(0,585, 128, 128))
    hitbox_1.draw(screen)
    hitbox_2.draw(screen)
    pygame.display.flip()

pygame.quit()   