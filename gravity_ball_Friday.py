#Pygame Template

import pygame
import time
from random import randint, uniform
from math import pi, sqrt, cos, sin, atan2
from capture import capture

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

width,height = 600,600

GRAV = 5 #acceleration due to gravity

class Ball(object):
    def __init__(self):
        #properties of the ball
        self.radius = 40
        self.x_position = randint(0,width)
        self.y_position = randint(0,height)
        self.x_velocity = 5
        self.y_velocity = 5

    def update(self):
        # increment the velocity by the acceleration
        self.y_velocity += GRAV
        self.y_position += self.y_velocity
        self.x_position += self.x_velocity
        # if on edge, bounce
        if self.x_position >= width - self.radius:
            self.x_position = width - self.radius
            self.x_velocity *= -1
        if self.x_position < self.radius:
            self.x_position = self.radius
            self.x_velocity *= -1

        if self.y_position >= height - self.radius:
            self.y_position = height - self.radius
            self.y_velocity *= -1
        if self.y_position < self.radius:
            self.y_position = self.radius
            self.y_velocity *= -1

        pygame.draw.circle(screen, RED, [self.x_position, self.y_position], self.radius)
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
ball_list = [Ball() for i in range(10)] #initialize a ball

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if pygame window is closed by user
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xpos -= 20
    if keys[pygame.K_RIGHT]:
        xpos += 20

    # fill the screen with background color
    screen.fill(BLACK)
    for b in ball_list:
        b.update()
    counter += 1

    pygame.display.update()

    # for saving screenshots
    # if counter %5 == 0:
    #     capture(screen, 'Name{}.png'.format(counter), (0, 0), (600, 600))

    clock.tick(FPS)
pygame.quit()