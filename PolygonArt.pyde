'''Random shape Generator from Coding Beauty
November 16, 2018
with Curtis and Callum'''

from random import randint, choice

cols = 6

class Polygon:
    def __init__(self,SZ):
        self.pointList1 = [(randint(0,SZ/3),randint(0,SZ/3)) for \
                          i in range(3)]
        self.pointList2 = [(randint(0,SZ/3),randint(0,SZ/3)) for \
                          i in range(3)]
        self.hue1 = randint(20,255)
        self.hue2 = randint(20,255)
        self.alph = randint(150,255)
        self.col = color(self.hue1,255,200,self.alph)
        self.col2 = color(self.hue2,255,200,self.alph)
        self.strok = color(self.hue1,255,255)
        self.strok2 = color(self.hue2,255,255)
        self.polys = choice([3,4,5,6,12,24])
    
    def render(self):
        for i in range(self.polys):
            fill(self.col)
            stroke(self.strok)
            beginShape()
            for pt in self.pointList1:
                vertex(pt[0],pt[1])
            endShape(CLOSE)
            rotate(TWO_PI/self.polys)
        for i in range(self.polys):
            fill(self.col2)
            stroke(self.strok2)
            beginShape()
            for pt in self.pointList2:
                vertex(pt[0],pt[1])
            endShape(CLOSE)
            rotate(TWO_PI/self.polys)

def setup():
    global polyList, SZ
    size(600,600)
    colorMode(HSB)
    #noStroke()
    SZ = width / cols
    polyList = [Polygon(SZ) for i in range(cols**2)]
    
def draw():
    background(0)
    translate(SZ / 2.0,SZ/2.0)
    for i,poly in enumerate(polyList):
        pushMatrix()
        translate(SZ*(i%cols), SZ*(i//cols))
        poly.render()
        popMatrix()
    
