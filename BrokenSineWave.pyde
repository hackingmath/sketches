'''Clone of a "Pen" on Codepen by bertdida
November 2, 2018
wiht Curtis'''

t = 0
dt = 0.5
H_BOX = 300 #height of "box"

def setup():
    size(600,600)
    strokeWeight(10)
    colorMode(HSB)
    
def draw():
    global t, dt
    background(0)
    translate(100,100)
    for i in range(20):
        y = H_BOX/2.0+H_BOX*0.45*sin(t/20.0+0.125*i)
        col = 255/2.0+(200/2.0)*sin(frameCount/50.0)
        stroke(col+i,255,255)#0.85*y,255,255)
        line(20*i,0,20*i,y)
        stroke((col+i+100)%255,255,255)
        line(20*i,H_BOX,20*i,y+20)
        
    t += dt
