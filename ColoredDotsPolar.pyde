'''Recreating Bees and Bombs' Dots Sketch
November 26, 2018'''

NUM_DOTS = 30
PURPLE = color(204,0,204)
ratio = 0

def setup():
    size(600,600)
    #colorMode(HSB)
    noStroke()
    
def draw():
    frameRate(20)
    global ratio
    background(0)
    ratio += 0.01
    textSize(24)
    text(ratio,100,100)
    translate(width/2, height/2)
    
    for i in range(NUM_DOTS):
        pushMatrix()
        rotate(TWO_PI*i/float(NUM_DOTS))
        fill(PURPLE)#20*i,255,200)
        #ratio = map(mouseX,0,600,0,5)
        
        translate(100+100*sin(frameCount/15.0 + ratio*i),0)
        #stroke(6*i,255,255)
        ellipse(0,0,10,10)
        popMatrix()
