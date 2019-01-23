'''Ellipse Wave
January 22, 2019
with Aaron'''

sz = 30 #diameter of the ellipses
t = 0 #time
dt = 0.05 #change in time

def setup():
    size(600,600)
    colorMode(HSB)
    
def draw():
    global t,dt,sz
    background(0) #black
    for i in range(21):
        fill(10*i,255,255)
        ellipse(sz*i,300+200*sin(t-i/4.0),sz,sz)
        
    t += dt
    
