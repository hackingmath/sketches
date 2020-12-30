#Astroid

import pygame
from capture import capture
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

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if pygame window is closed by user
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xpos -= 20
    if keys[pygame.K_RIGHT]:
        xpos += 20

    if keys[pygame.K_p]:
        if FPS == 60:
            FPS = 300  #faster display
        else:
            FPS = 60

    #assign mouse's position to variables
    mouseX,mouseY = pygame.mouse.get_pos()

    # fill the screen with background color
    screen.fill(BLACK)
    map_min,map_max = 2,50
    d = 2+(48/600)*mouseX
    for i in range(int(300/d)+1):
        pygame.draw.line(screen, VIOLET, [300 + d*i,300],[300,d*i],1)
        pygame.draw.line(screen, VIOLET, [300 - d * i, 300], [300, d * i], 1)
        pygame.draw.line(screen, VIOLET, [300 + d * i, 300], [300, 600-d * i], 1)
        pygame.draw.line(screen, VIOLET, [300 - d * i, 300], [300, 600 - d * i], 1)

    #pygame.draw.polygon(screen, WHITE, [(100, 200), (xpos,ypos), (524, 307), (500, 200)], 0)
    #pygame.draw.rect(screen, WHITE, [xpos,ypos, 150,200])
    #pygame.draw.line(screen, GREEN, [300,300],[300,0],1)
    #pygame.draw.circle(screen,RED,[400,100],50)

    counter += 1

    pygame.display.update()

    # for saving screenshots
    if counter %5 == 0:
        capture(screen, 'Astroid{}.png'.format(counter), (0, 0), (600, 600))

    clock.tick(FPS)
pygame.quit()