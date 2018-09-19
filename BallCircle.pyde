num = 20

def setup():
    size(600,600)
    colorMode(HSB)
    
def draw():
    num = int(map(mouseX,0,width,0,24))
    #background(255)
    background(0)
    translate(width/2, height/2)
    #fill(0)
    #ellipse(0,0,width,height)
    for i in range(int(num)):
        line(0,-height/2,0, height/2)
        rotate(PI/float(num))
    for i in range(num):
        shift = i*PI/float(num)
        ball(50+width/float(num)*i,20,shift,i)
        rotate(PI/float(num))
    saveFrame("####.png")
        
def ball(distance,sz,shift,i):
    '''num balls in a circular wave'''
    pushMatrix()
    #translate(distance,width/2)
    stroke(255)
    line(0,-height/2,0, height/2)
    noStroke()
    y = ((height - sz)/2.0)*sin(frameCount/30.0-shift)
    fill(10*i,255,255)
    ellipse(0,y,sz,sz)
    popMatrix()
    
def ballLine(distance,sz,shift):
    '''num balls in a vertical wave'''
    pushMatrix()
    translate(distance,width/2)
    stroke(255)
    line(0,-height/2,0, height/2)
    noStroke()
    y = ((height - sz)/2.0)*sin(frameCount/20.0)
    fill(255)
    ellipse(0,y,sz,sz)
    popMatrix()
    
