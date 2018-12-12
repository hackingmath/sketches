
def setup():
    size(600,600)
    colorMode(HSB)
    rectMode(CENTER)
    noStroke()
    
diam = 5 #diameter of each circle
    
def draw(): #infinite loop
    translate(diam/2,diam/2)
    num = width/diam
    for j in range(num):
        for i in range(num):
            fill((4*frameCount+(i+j+5))%255,255,255)
            rect(i*diam,j*diam,diam,diam)
