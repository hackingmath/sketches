'''Cloning the November picture on my math calendar
November 5, 2018'''

pos = color(255)
neg = color(0)
RED = color(255,0,0)
sz = 100

class Square:
    def __init__(self,sz,divisions):
        self.sz = sz
        self.divisions = divisions
        
    def render(self):
        scl = self.sz/(self.divisions)
        #top left half
        for i in range(self.divisions):
            if i % 2 ==0:
                fill(neg)
            else:
                fill(pos)
         
            beginShape()
            vertex(0,i*scl)
            vertex(0,(i+1)*scl),
            vertex(((self.divisions -(i+1))/float(self.divisions))*self.sz,(i+1)*scl)
            vertex(((self.divisions -i)/float(self.divisions))*self.sz,i*scl)
            endShape(CLOSE)
        if i % 2 == 0:
            fill(neg)
        else:
            fill(pos)
        beginShape()
        vertex(0,0)
        vertex(0,0.2*scl)
        vertex(sz-0.2*scl,0.2*scl)
        vertex(sz-0.2*scl,0)
        endShape(CLOSE)
        
        #bottom right half
        pushMatrix()
        translate(self.sz,self.sz)
        rotate(PI)
        for i in range(self.divisions):
            if i % 2 ==0:
                fill(pos)
            else:
                fill(neg)
         
            beginShape()
            vertex(i*scl,0)
            vertex((i+1)*scl,0),
            vertex((i+1)*scl,((self.divisions -(i+1))/float(self.divisions))*self.sz)
            vertex(i*scl,((self.divisions -i)/float(self.divisions))*self.sz)
            endShape(CLOSE)
        if i % 2 == 0:
            fill(pos)
        else:
            fill(neg)
        beginShape()
        vertex(0,0)
        vertex(0.2*scl,0)
        vertex(0.2*scl,sz-0.2*scl)
        vertex(0,sz-0.2*scl)
        endShape(CLOSE)
        popMatrix()
        #little square
        if self.divisions % 2 == 0:
            fill(pos)
        else:
            fill(neg)
        beginShape()
        vertex(self.sz-scl,scl/2.0)
        vertex(self.sz-scl/2.0,scl/2.0)
        vertex(self.sz-scl,scl)
        endShape(CLOSE)
        
        if self.divisions % 2 == 0:
            fill(neg)
        else:
            fill(pos)
        beginShape()
        vertex(self.sz-scl/2.0,2*scl/2.0)
        vertex(self.sz-scl/2.0,scl/2.0)
        vertex(self.sz-scl,scl)
        endShape(CLOSE)

s = Square(sz,4)

def square4():
    for i in range(4):
        translate(0,-sz)
        s.render()
        translate(0,sz)
        rotate(PI/2.0)

def setup():
    size(600,600)
    stroke(100)
    
def draw():
    background(0)
    translate(sz,sz)
    for i in range(4):
        for j in range(4):
            pushMatrix()
            translate(2*sz*i,2*sz*j)
            square4()
            popMatrix()
    
