#Making fireworks! July 2, 2016
#Particles fade out

class Particle:
    def __init__(self,x,y,angle,vel,ran,rocket=False):
        self.x = x #initial x-cor
        self.y = y #initial y=cor
        self.dx = vel*cos(angle) #initial dx
        self.dy = vel*sin(angle) #initial dy
        self.ran = ran
        self.c = 255 #color amount
               
        self.rocket = rocket
        
    def update(self,listA):
        #update the position by the velocity
        self.x += self.dx 
        self.dy += grav #update y-velocity by gravity
        self.y += self.dy 
        if self.y > 600:
            listA.remove(self)
        if self.rocket: #if it's a rocket
            if abs(self.dy)<0.1: #when it gets to it's max y-value
                for i in range(500):
                    firework_list.append(Particle(self.x,
                                    self.y,
                                    random(6.3),
                                    random(6),
                                    self.ran))
                firework_list.remove(self)
                    
        #draw particle
        if self.ran == 0:
            fill(self.c,0,0) #red
        elif self.ran == 1:
            fill(self.c,self.c,self.c)#white
        else:
            fill(0,0,self.c) #blue
        ellipse(self.x,self.y,5,5) #particle
        #make color fade a little
        self.c -= 1
        if self.c == 0:
            listA.remove(self)
        

    
#declare variables:
grav = 0.1 #gravity
firework_list = []
ignite = False #ignite fireworks off

def setup(): #this only happens once
    size(600,600)
    noStroke()
    
def draw():
    background(0) #black "sky"
    frameRate(60)
    for f in firework_list:
        f.update(firework_list)
    '''if frameCount % 2 == 0:
        saveFrame("####.png")'''
    
def mousePressed():
    ran = int(random(3))
    explodeX,explodeY = mouseX,mouseY
    
    firework_list.append(Particle(explodeX,
                                  height,
                                  radians(-90),
                                  sqrt(2*(height -explodeY)*grav),
                                  int(random(3)),True))

    draw()
    
    
    
