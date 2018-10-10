'''Cloning Jo's (@jn3008) Sierpinski Polygon Sketch
with Jared
October 9, 2018'''

DIAM = 500

def setup():
    size(600,600)
    colorMode(HSB)
    
def draw():
    global DIAM
    background(0)
    translate(width/2,height/2)
    num_sides = int(map(mouseX,0,600,3,12))
    polygon(num_sides,DIAM,60)
    
def polygon(num_sides,sz,level):
    if level > 0:
        r = sz/2.0
        ang = 360/float(num_sides)
        fill(255*((level+1)%2))
        beginShape()
        rotate(0.5*radians(360/float(num_sides)))
        for i in range(num_sides):
            vertex(r*cos(radians(i*ang)),
                r*sin(radians(i*ang)))
        endShape(CLOSE)
        
        #internal angle of polygon
        a = 180 - (360/float(num_sides))
        new_sz = sz* cos(radians((180 - a)/2.0))
        polygon(num_sides,new_sz,level-1)
