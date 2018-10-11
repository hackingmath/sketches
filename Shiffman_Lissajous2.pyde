'''Shiffman's Lissajous Curve Table
Coding Challenge
October 9, 2018
with Aryan'''

w = 70
t = 0
dt = 0.003

class Lissajous:
    def __init__(self,x,y,vert,horiz):
        self.x = x #horizontal location
        self.y = y #vertical location
        #self.r = r #size of figure
        self.vert = vert #vertical frequency
        self.horiz = horiz #horizontal frequency
        self.pointList = []
        d = w - 10
        self.r = d / 2
        self.col = self.x + self.y
        
    def update(self,t):
        x = self.x + self.r*cos(t*self.horiz)
        y = self.y + self.r*sin(t*self.vert)
        self.pointList.append([x,
                               y])
        stroke(255)
        ellipse(x,y,5,5)
        
    def render(self):
        if len(self.pointList) > 1:
            for i,dot in enumerate(self.pointList):
                if i < len(self.pointList) - 1:
                    stroke(self.col/4.5,255,255)
                    line(dot[0],
                        dot[1],
                        self.pointList[i+1][0],
                        self.pointList[i+1][1])
                
def setup():
    global w,cols,lissajousList
    size(600,600)    
    colorMode(HSB)
    cols = width/w - 1
    lissajousList = []
    for j in range(cols):
        for i in range(cols):
            lissajousList.append(Lissajous(w + i * w + w/2.0,
                                           w + j * w + w/2.0,
                                           j + 1,
                                           i + 1))
    
def draw():
    global cols,w, t,dotList
    
    background(0)
    d = w - 10
    r = d / 2
    for i in range(cols):
        stroke(255)
        noFill()
        #top row
        x = w + i * w + w/2.0
        y = w / 2.0
        stroke(255)
        ellipse(x,y,d,d)
        x2 = x + r*cos(t*(i+1))
        y2 = y + r*sin(t*(i+1))
        stroke(50)
        line(x2,0,x2,height)
        stroke(255)
        ellipse(x2,y2,5,5)
        t += dt
        
        #left column:
        y = w + i * w + w/2.0
        x = w / 2.0
        ellipse(x,y,d,d)
        x3 = x + r*cos(t*(i+1))
        y3 = y + r*sin(t*(i+1))
        stroke(50)
        line(0,y3,width,y3)
        stroke(255)
        ellipse(x3,y3,5,5)
        
        #dot
        #fill(255,0,0)
        #dotList.append((x2,y3))
    for l in lissajousList:
        l.update(t)
        l.render()
    '''if frameCount % 2 == 0:
        saveFrame("####.png")
    if frameCount == 300:
        noLoop()'''
