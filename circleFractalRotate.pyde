diam = 200
t = 0

def setup():
  size(500,500)
  fill(255,255,0,50)
  stroke(255)
  noStroke()
  
def draw():
    global t
    background(76,0,153) #red,green,blue
    fractal(width/2,height/2,250,8)
    translate(width/2.0,height/2.0)
    #rotate the design with the mouse
    ang = map(mouseX,0,500,0,180)
    rotate(t)
    fractal(0,0,250,8)
    t += 0.01
    saveFrame("###.png")
    if t > PI: noLoop()
  
def fractal(x,y,diam,level):
  if level > 0:
    strokeWeight(1)#level/3.0)
    ellipse(x,y, diam, diam)
    fractal(x-diam/2.0,y,diam/2.0,level-1)
    fractal(x+diam/2.0,y,diam/2.0,level-1)
