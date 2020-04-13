#from __future__ import division

'''Grid for graphing'''

from slider import Slider

slider1 = Slider(0,50,6)
slider2 = Slider(0,80,14)

def setup():
    size(600,600)
    slider1.position(20,20)
    slider2.position(20,50)
    fill(255)
    
rangex = 5
rangey = 5
xscl = 600/rangex
yscl = -600/rangey
t = 7 
    
def draw():
    fill(0,10)
    global xscl, yscl,t
    #rect(0,0,width,height)
    background(0)
    #translate(width/2,height/2)
    a = slider1.value()
    b = slider2.value()
    slider1.label = str(a)
    slider2.label = "b"
    
    
    #graphFunction()
    stroke(255,0,255)
    strokeWeight(1)
    
    # a = 20*cos(t/100)
    # b = 20*sin(t/50)

    a2 = [[i,2*i+5] for i in range(-10,11)]
    d = [f(i,a,b) for i in arange(-10,11,0.001)]
    graphPoints2(d)
    t += 0.01
    # if frameCount % 2 == 0:
    #     saveFrame("####.png")
    
def grid():
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(-10,11):
        line(i*xscl,-10*yscl,i*xscl,10*yscl)
        line(-10*xscl,i*yscl, 10*xscl,i*yscl)
        
    stroke(0) #black axes
    line(0,-10*yscl,0,10*yscl)
    line(-10*xscl,0, 10*xscl,0)
    
def graphPoints(pointList):
    '''Graphs the points in a list'''
    for p in pointList:
        point(p[0]*xscl,p[1]*yscl)
        
'''def f(x):
    return 6*x**3 + 31*x**2 + 3*x - 10'''

def f(t,a,b):
    return [cos(t)+cos(a*t)/2+sin(b*t)/3, sin(t)+sin(a*t)/2+cos(b*t)/3]

def graphFunction():
    global xscl, yscl
    x = -10
    while x <= 10:
        stroke(255,0,0) #red function
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1

a = list() #or a = []

for i in range(-10,11):
    a.append([i,2*i+5])
    
def graphPoints(pointList):
    '''Graphs the points in a list'''
    for p in pointList:
        point(p[0]*xscl,p[1]*yscl)
    
def graphPoints2(pointList):
    '''Graphs the points in a list using segments'''
    global xscl, yscl
    for i,p in enumerate(pointList):
        if i<len(pointList)-1:
            line(p[0]*xscl+width/2.0,p[1]*yscl+height/2.0,
                 pointList[i+1][0]*xscl+width/2.0,pointList[i+1][1]*yscl+height/2.0)


def arange(start,stop,step):
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output


def graphx(x):
    '''converting point to canvas form'''
    return x * width/rangex

def graphy(y):
    '''convert y-coord to canvas form'''
    return y * height/rangey


    
