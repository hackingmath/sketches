'''Cloning the Netflix spinning circle of circles
Peter F.
February 1, 2019'''

NUM = 12
locs = []
t = 0
dt = 0.08

def setup():
    size(600,600)
    noStroke()
    
def draw():
    global NUM, locs, t, dt
    fill(0,20)
    rect(0,0,width,height)
    translate(width/2,height/2)
    rotate(t)
    for i in range(NUM):
        fill(255,0,0)
        sz = 20*(1-i*0.075)
        ellipse(100*cos((t-2*i)/float(20)),
                100*sin((t-2*i)/float(20)),
                sz,sz)
    t += dt
