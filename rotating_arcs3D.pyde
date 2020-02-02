import random

sz = 50

class Arcs:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #self.sz = 50
        self.direction = random.choice([1,2])
        self.rotating = False
        self.ang = 0
        
    def update(self):
        pushMatrix()
        translate(self.x,self.y)
        if not self.rotating and random.randint(1,600) < 6:
            self.rotating = True
            self.ang = 90
            if self.direction == 1:
                self.direction = 2
            else:
                self.direction = 1
        if self.rotating:
            rotate(radians(90*self.direction-self.ang))
            self.ang -= 10
            if self.ang <= 0:
                self.rotating = False
            
        else:
            rotate(self.direction*PI/2.0)
        rotate(PI/4.0)#offset angle
        shift = 0.94#map(mouseX,0,width,0.9,1.1)#0.92
        arc(-2*sz/3.0,
            0,
            sz*shift,sz*shift,
            -radians(49),radians(49))
        arc(2*sz/3.0,
            0,sz*shift,sz*shift,
            radians(131),radians(229))
        popMatrix()

def setup():
    global arc_list
    size(600,600,P3D)
    
    arc_list = []
    for i in range(60):
        for j in range(60):
            arc_list.append(Arcs(i*sz,j*sz))
    stroke(255,0,255)
    strokeWeight(3)
    noFill()
    
def draw():
    background(0)
    translate(-300,-500,-700)
    rotateX(radians(45))
    for a in arc_list:
        a.update()
    saveFrame("####.png")
    
