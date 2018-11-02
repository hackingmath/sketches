'''Cloning the revolving circles sketch of 
Martin Holtham @GHSMaths on Twitter
November 2, 2016'''

RED = color(255,0,0)
GREEN = color(0,255,0)
BLUE = color(0,0,255)
PURPLE = color(153,0,153)
ORANGE = color(238,125,13)

t = 0
dt = 0.075

class Wheel:
    def __init__(self,num):
        self.num = num
        self.divisions = 2*self.num
        self.radius = 25*(self.num)
        
    def update(self):
        ang = TWO_PI/float(self.divisions) #central angle
        pushMatrix()
        rotate(-t/float(self.num))
        for i in range(self.divisions):
            if i % 2 == 0:
                fill(PURPLE)
            else:
                fill(ORANGE)
            
            arc(0,0,2*self.radius,2*self.radius,
                i*ang,(i+1)*ang,PIE)
        popMatrix()
       
wheelList = [Wheel(i) for i in range(1,13)]
    
def setup():
    size(600,600)
    
def draw():
    global wheelList,t
    background(0)
    translate(width/2.0,height/2.0)
    for w in wheelList[::-1]:
        w.update()
    if t < TWO_PI:
        saveFrame("####.png")
    t += dt
