import pygame
import time
from random import randint, uniform
from math import pi, sqrt, cos, sin, atan2,degrees
#from capture import capture

# define constants
BLACK = (0, 0,0,25)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)
PINK = (255,0,255)

width,height = 600,600

# set up display
pygame.init()
screen = pygame.display.set_mode([width, height])
draw_surface = pygame.Surface((width,height),pygame.SRCALPHA)

#in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 72)

pygame.display.set_caption('Poisson Trees') #add your own caption!
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0 #frame count
angle = 0 #angle of tree branches

# loop until user clicks the close button
done = False

#Rendering the Game
xpos,ypos = 300,300

def tree(position,sz,heading,ang,level):

    pygame.draw.circle(draw_surface, PINK, position, 5, 0)
    if level > 0:
        newposition1 = (position[0] + sz * cos(heading+ang),
                    position[1] + sz * sin(heading+ang))
        newposition2 = (position[0] + sz * cos(heading-ang),
                        position[1] + sz * sin(heading-ang))
        pygame.draw.line(draw_surface, PINK,position, newposition1, 3)
        pygame.draw.line(draw_surface, PINK, position, newposition2, 3)
        tree(newposition1,sz, heading+ang,ang,level-1)
        tree(newposition2, sz, heading-ang,ang, level - 1)


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
    # fill the draw surface with background color
    draw_surface.fill(BLACK)

    level = 7#int(pygame.mouse.get_pos()[0]/50)
    locs = ((400,300),(300,200),(200,300),(300,400))
    angle = pi / 4 + pi / 4 * sin(counter / 150)

    for i, loc in enumerate(locs):
        pygame.draw.circle(screen, PINK, loc, 10, 0)
        tree(loc,100,-pi/2*i,angle,level)

    counter += 1

    screen.blit(draw_surface,(0,0))
    pygame.display.update()

    # for saving screenshots:
    # if counter %5 == 0:
    #     capture(screen, 'Poisson{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)
pygame.quit()
