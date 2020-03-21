
import time

sz = 70 #radius of hexagon
counter = 0

def setup():
  size(500,500)
  
def draw():
    global counter
    background(255)
    #translate(width/2.0,height/2.0)
    for x in range(5):
        for y in range(6):
            pushMatrix()
            translate(x*1.732*sz-(y%2)*0.866*sz,y*1.5*sz)
            #stroke(0) #black
            #polygon(6,sz)
            stroke(255,0,255) #red lines
            if 5*x + y < counter:
                lines(165/200.0*sz,sz*3/20.0)
            popMatrix()
    counter += 1

def polygon(sides,radius):
  rotate(radians(360/12))
  angle = radians(360/sides)
  for i in range(sides):
    line(radius*cos(i*angle),radius*sin(i*angle),
        radius*cos((i+1)*angle),radius*sin((i+1)*angle))
        
def lines(length,r):
  rotate(radians(360/12))
  for i in range(12):
    strokeWeight(2)
    line(-r,17/30*r,-r,length)
    line(r,17/30*r,r,length)
    strokeWeight(1)
    line(-r,length,r,length*1.1)
    line(r,length,-r,length*1.1)
    rotate(radians(360/12))
