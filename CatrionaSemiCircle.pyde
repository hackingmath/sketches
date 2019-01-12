ratio = 2/3.0
radius = 3.5 #semicircle

def setup():
    size(600,600)
    textSize(1)
    noFill()
    
def draw():
    background(255) #white background
    translate(width/2,height/2)
    scale(width/10)
    scale(1,-1) #flip the y-values
    grid()
    strokeWeight(0.04)
    ratio = map(mouseX,0,width,0,1.0)
    w_rect = (1+ratio)*radius
    x = ratio*radius
    y = sqrt(radius**2 - x**2)
    d = dist(-radius,0,x,y)
    stroke(0,0,255) #blue
    line(-radius,0,x,y)
    stroke(0,255,0)
    arc(0,0,2*radius,2*radius,0,PI)
    stroke(0,150,150)
    rect(-radius,0,w_rect,radius)
    if abs(d-6.0) < 0.004:
        println(str(radius**2*(1+ratio)))
        '''fill(0,0,255)
        text("6",-0.5,1.5)
        fill(0,255,0)
        text(str(radius**2*(1+ratio)),2,4)
        noFill()'''
    
def grid():
    #cyan lines
    strokeWeight(0.02)
    stroke(0,255,255)
    for i in range(-10,11):
        line(i,-10,i,10)
        line(-10,i,10,i)
    stroke(0) #black axes
    line(0,-10,0,10)
    line(-10,0,10,0)
    #fill(0) #black
    #graphFunction()
    
def f(x):
    return 6*x**3 + 31*x**2 + 3*x - 10
    
def graphFunction():
    x = -10
    while x <= 10:
        line(x,f(x),x+0.1,f(x+0.1))
        x += 0.1
    
