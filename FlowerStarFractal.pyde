
def setup():
    size(600,600)
    stroke(255) #white lines
    
def draw():
    background(0)
    translate(width/2.0,height/2.0)
    flower(200,1)
    
def flower(sz,level):
    h = sz*cos(radians(15))
    b = sz*sin(radians(15))
    line(h,-b,sz*0.67,0)
    line(h,b,sz*0.67,0)
    line(h,-b,sz*1.5,0)
    line(h,b,sz*1.5,0)
