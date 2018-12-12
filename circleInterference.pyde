'''Webbster's circle interference patterns
December 11, 2018
with Jared'''

sz = 75
WHITE = color(255)
BLACK = color(0)

def setup():
    size(600,600)
    noStroke()
    blendMode(DIFFERENCE)
    
def draw():
    translate(width/2,height/2)
    circleThing(0,0)
    circleThing(-width/2,0)
    circleThing(0,-height/2)
    circleThing(width/2,0)
    circleThing(0,height/2)
    noLoop()
    
def circleThing(x,y):
    pushMatrix()
    translate(x,y)
    for i in range(1,9):
        if i % 2 == 1:
            fill(0)
        else: fill(255)
        ellipse(0,0,width-sz*i,width-sz*i)
    popMatrix()
