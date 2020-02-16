#imports/init
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
class Renderer:
    def __init__(self,screen):
        self.screen=screen
    def render(self,image,pos):
        self.screen.blit(image, pos)
class Square:
    def __init__(self,largeTicks):
        self.largeTicks=largeTicks
    def getLargeTicks(self):
        return self.largeTicks
    def incrementLargeTicks(self,modifier):
        self.largeTicks+=modifier
    def setLargeTicks(self,new):
        self.largeTicks=new
#pygame init
pygame.init()
width, height=640,480
screen=pygame.display.set_mode((width, height))

#variables
#togglable
cooldownTicks=5
#default
clicks=0
#objects
main=Renderer(screen)
mainSq=Square(0)

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
    if mainSq.getLargeTicks()>0:
        mainSq.incrementLargeTicks(-1)
        main.render(squareBig, (240,160))
    else:
        main.render(squareSmall, (245,165))
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str(clicks), False, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    main.render(survivedtext, textRect)
    #events
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type==pygame.MOUSEBUTTONDOWN:
            if mainSq.getLargeTicks()==0:
                x, y=pygame.mouse.get_pos()
                if x>245 and x<395 and y>165 and y<315:
                    mainSq.setLargeTicks(cooldownTicks)
                    clicks+=1
                
