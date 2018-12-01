'''Chaos Game 
Inspired by Shiffman
November 30, 2018'''

from random import random, randint, choice, sample

NUM_VERTICES = 6
PURPLE = color(153,50,204)
x,y = 0,0

def setup():
    size(800,800)
    stroke(0,255,0)
    
def draw():
    global x,y
    background(0)
    #chaosReg(NUM_VERTICES)
    for i in range(100000):
        drawPoint(x,y)
        x,y = nextPoint(x,y)
    noLoop()
    
def midpt(A,B):
    '''returns the midpoint of pts A and B'''
    return ((A[0] + B[0])/2.0,(A[1] + B[1])/2.0)

def chaosReg(n):
    '''Plays Chaos Game with regular n-gon'''
    stroke(PURPLE)
    #put n random points on screen
    r = 400
    pts = [(width/2 + r*cos(i*TWO_PI/float(n)),
            height/2 + r*sin(i*TWO_PI/float(n))) for \
           i in range(n)]
    #create random point
    random_pt = (randint(0,width),randint(0,height))
    
    for i in range(100000):
        pts.append(random_pt)
        random_vertex = choice(pts[:n])
        random_pt = midpt(random_pt,random_vertex)
        
        
    #draw points
    for pt in pts:
        point(pt[0],pt[1])
    
def chaos(n):
    '''Plays Chaos Game with n random vertices'''
    #put n random points on screen
    pts = [(randint(0,width),randint(0,height)) for \
           i in range(n)]
    #create random point
    random_pt = (randint(0,width),randint(0,height))
    
    for i in range(100000):
        pts.append(random_pt)
        random_vertex = choice(pts[:n])
        random_pt = midpt(random_pt,random_vertex)
        
        
    #draw points
    for pt in pts:
        point(pt[0],pt[1])
        
###CODE FOR BARNSLEY FERN###
        
def drawPoint(x,y):

    stroke(34, 139, 34)
    strokeWeight(1)
    px = map(x,-2.1820, 2.6558,0,width)
    py = map(y,0,9.9983,height,0)
    point(px,py)
    #return (px,py)
    
def nextPoint(x,y):

    r = random()
    if r<0.01:
        nextX = 0
        nextY = 0.16*y
    elif r < 0.86:
        nextX = 0.85 * x + 0.04 * y
        nextY = -0.04 * x + 0.85 *y + 1.6
    elif r < 0.93:
        nextX = 0.20 * x - 0.26 *y
        nextY = 0.23 * x + 0.22 *y + 1.6
    else:
        nextX = -0.15 *x + 0.28 *y
        nextY = 0.26 * x + 0.24 *y + 0.44
        
    x,y = nextX, nextY
    return (x,y)
