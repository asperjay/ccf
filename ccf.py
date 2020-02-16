#imports/init
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *

#pygame init
pygame.init()
width, height=640,480
screen=pygame.display.set_mode((width, height))

#variables
#togglable
cooldownTicks=5
#default
largeTicks=0
clicks=0

#image loads
#__=pygame.image.load('directory')
squareSmall=pygame.image.load('images/square1.png')
squareBig=pygame.image.load('images/square2.png')
background=pygame.image.load('images/background.png')
while True: #mainloop
    screen.fill(0)
    #screen.blit
    for x in range(int(width/background.get_width()+4)):
        for y in range(int(height/background.get_height()+4)):
            screen.blit(background,(x*100,y*100))
    if largeTicks>0:
        largeTicks-=1
        screen.blit(squareBig, (240,160))
    else:
        screen.blit(squareSmall, (245,165))
    #events
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if largeTicks==0:
                x, y=pygame.mouse.get_pos()
                if x>245 and x<395 and y>165 and y<315:
                    largeTicks=cooldownTicks
                    clicks+=1
                    print(clicks)
                
