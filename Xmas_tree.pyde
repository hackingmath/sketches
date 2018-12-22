from random import choice

YELLOW = color(255,255,0)
RED = color(255,0,0)
GREEN = color(0,255,0)
BLUE = color(0,0,255)
WHITE = color(255)

colors = [RED,GREEN,WHITE]

class Bulb:
    def __init__(self,t):
        self.pos = PVector(6*t*cos(t),15*t,6*t*sin(t))
        self.col = choice(colors)
    
    def update(self):
        pushMatrix()
        translate(self.pos.x,
                  self.pos.y,
                  self.pos.z)
        fill(self.col)#choice(colors))
        sphere(20)
        popMatrix()

def setup():
    global bulbList
    size(600,800,P3D)
    noStroke()
    bulbList = []
    t = 0
    while t < 70:
        bulbList.append(Bulb(t))
        t += 0.25
    
def draw():
    global bulbList
    background(0)
    translate(width/2,0,-width)
    
    pushMatrix()
    #translate(0,-height/2.0,0)
    rot = map(mouseX,0,width,0,TWO_PI)
    tilt = map(mouseY,0,height,0,PI/4.0)
    rotateX(tilt)
    rotateY(rot)
    pushMatrix()
    translate(0,-100,0)
    rotateX(PI)
    star()
    popMatrix()
    for b in bulbList:
        b.update()
    
    popMatrix()
    saveFrame("####.png")
    
def star():
    sz = 100
    fill(YELLOW)
    
    beginShape()
    for i in range(5):
        vertex(0,sz*cos(i*radians(144)),sz*sin(i*radians(144)))
    endShape(CLOSE)
    
