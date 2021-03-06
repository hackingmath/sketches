#Pygame Template

import pygame
import time
from random import randint, uniform
from math import pi, sqrt, cos, sin, atan2

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)
YELLOW = (255,255,0)

width,height = 600,600

# set up display
pygame.init()
screen = pygame.display.set_mode([width, height])

#in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)

pygame.display.set_caption('Pygame Window') #add your own caption!
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0 #frame count

# loop until user clicks the close button
done = False

#Rendering the Game
xpos,ypos = 300,300
xvel,yvel = 5,3
radius = 10

#display loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if pygame window is closed by user
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pygame.key.set_repeat(1000)
        xvel -= 5
    if keys[pygame.K_RIGHT]:
        pygame.key.set_repeat(1000)
        xvel += 5

    if keys[pygame.K_p]:
        if FPS == 60:
            FPS = 300  #faster display
        else:
            FPS = 60
    # fill the screen with background color
    screen.fill(CYAN)

    #pygame.draw.polygon(screen, WHITE, [(100, 200), (xpos,ypos), (524, 307), (500, 200)], 0)
    #pygame.draw.rect(screen, WHITE, [xpos,ypos, 150,200])
    #pygame.draw.line(screen, GREEN, [100,100],[200,300],3)
    pygame.draw.circle(screen,YELLOW,[xpos,ypos],2*radius)
    xpos += xvel
    ypos += yvel

    if xpos >= 600-radius:
        xpos = 600 - radius
        xvel *= (-1)
    if xpos <= radius:
        xpos = radius
        xvel *= (-1)
    if ypos >= 600-radius:
        ypos = 600 - radius
        yvel *= (-1)
    if ypos <= radius:
        ypos = radius
        yvel *= (-1)

    #print("xvel:",xvel)
    counter += 1

    pygame.display.update()

    clock.tick(FPS)
pygame.quit()
