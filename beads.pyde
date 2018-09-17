'''Clone of Fermat's Library and Al Sweigart's sketch
https://twitter.com/AlSweigart/status/1041803628602777600
September 17,2018'''

#sz = 600
t = 0

def setup():
    size(600,600)
    colorMode(HSB)
    
def draw():
    global t
    background(0) #black
    translate(width/2,height/2)
    stroke(255)
    for i in range(8):
        line(-width/2,0,width/2,0)
        rotate(radians(360/16))
    for i in range(8):
        bead(i,t)
        rotate(radians(360/16))
    t += 0.1
    saveFrame("####.png")
    if t >= 8*PI:
        noLoop()
    
def bead(n,t):
    pushMatrix()
    fill(30*n,255,255)
    x = width/2*sin(t/4+n*PI/8.0)
    noStroke()
    ellipse(x,0,40,40)
    popMatrix()
    
