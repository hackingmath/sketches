'''Grid of Pendulums
Peter Farrell with Curtis
Friday the 13th! October 13, 2017'''

def setup():
    size(600,600,P3D)
    colorMode(HSB)
    
sz = 100 #length of pendulum
t = 0
dt = 0.5 #change in time
    
def draw():
    global t,dt,sz
    frameRate(200)
    background(255)
    translate(width/2.0,height/3.0,-width/2)
    rotateX(-0.75)
    rotateY(t/20.0)
    for x in range(-200,201,100):
        for y in range(-200,201,100):
            for z in range(-200,201,100):
                pushMatrix()
                translate(x,y,z)
                pendulum(t-y/200.0,sz)
                popMatrix()
    t += dt
                
    
def pendulum(time,sz):
    stroke(0)
    stroke((20*time)%255,255,255)
    rotateZ(0.75*sin(time))
    line(0,0,0,sz)
    translate(0,sz,0)
    sphere(sz/15.0)
    