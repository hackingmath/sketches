rad = 100
num = 9

def setup():
    size(600,600)
    noStroke()
    
def draw():
    background(0)
    sz = width/(float(num))
    translate(sz/2.0,sz/20)
    for x in range(num+1):
        for y in range(num+1):
            thingy(x*sz,y*sz,sz/2.0)
    
def thingy(x,y,r):
    pushMatrix()
    translate(x,y)
    rotate(frameCount/100.0)
    fill(255,102,0)
    ellipse(0,0,2*r,2*r)
    fill(0)
    arc(r,r,2*r,2*r,PI,3*PI/2)
    arc(-r,r,2*r,2*r,3*PI/2,TWO_PI)
    popMatrix()
    
