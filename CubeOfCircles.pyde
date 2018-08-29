'''Clone of Bees and Bombs
Aug 28, 2018
with Jared'''

class Wheel:
    def __init__(self,x,y,z,sz,space):
        self.x = x
        self.y = y
        self.z = z
        self.sz = sz
        self.ang = 0
        self.ran = random(2)
        self.space = space
        
    def update(self):
        stroke(255)
        fill(0)
        pushMatrix()
        translate(0,0,self.space)
        for i in range(3):
            
            pushMatrix()
            translate(self.x,self.y,0)
            self.spin(self.ran)
            self.ang += 1
            ellipse(0,0,self.sz,self.sz)
            line(-self.sz/2.0,0,self.sz/2.0,0)
            rotateX(PI/2.0)
            ellipse(0,0,self.sz,self.sz)
            line(0,-self.sz/2.0,0,0,self.sz/2.0,0)
            rotateY(PI/2.0)
            ellipse(0,0,self.sz,self.sz)
            line(-self.sz/2.0,0,self.sz/2.0,0)
            popMatrix()
            translate(0,0,-self.space)
            
        popMatrix()
        if self.ang >= PI/4.0:
            self.ran = (self.ran + 1) % 3
            self.ang = 0
            
    def spin(self,ran):
        
        if ran == 0:
            rotateX(radians(1))
        elif ran == 1:
            rotateY(radians(1))
        else:
            rotateZ(radians(1))
        
            

def setup():
    global t, dt,WheelList
    size(600,600,P3D)
    space = 200
    WheelList = [Wheel(x,y,z,100,space) for x in range(-space,space+1,space) \
                  for y in range(-space,space+1,space) \
                  for z in range(-space,space+1,space)]
    t = 0
    dt = 0.01
    
def draw():
    global t, dt,WheelList
    background(0) #black
    translate(width/2,height/2,-width)
    tilt = map(mouseY,0,width,0,PI)
    rot = map(mouseX,0,width,0,PI)
    rotateX(.8*PI)
    rotateY(rot)#t)
    noFill()
    stroke(150,150,255)#white lines
    box(600)
    for c in WheelList:
        c.update()
    #t += dt
