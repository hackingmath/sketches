'''Cloning the rotating squares grid
from Bees and Bombs
https://twitter.com/beesandbombs/status/1128694433426354178
May 15, 2019'''

def setup():
    global sz,gap
    size(600,600)
    strokeWeight(5)
    rectMode(CENTER)
    noFill()
    sz = 50
    gap = sz/3.0
    
def draw():
    translate(width/2,height/2)
    background(255)
    grid()
    
def grid():
    global sz,gap
    for i in range(-4,4):
        for j in range(-4,4):
            pushMatrix()
            translate((sz+gap)*i+40,(sz+gap)*j+40)
            rect(0,0,sz,sz)
            popMatrix()
    for m in range(-4,3):
        for n in range(-4,3):
            pushMatrix()
            translate((sz+gap)*m+40+2*gap,(sz+gap)*n+40+2*gap)
            rect(0,0,sz,sz)
            popMatrix()
