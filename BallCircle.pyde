num = 20

def setup():
    size(600,600)
    colorMode(HSB)
    
def draw():
    #map the mouse location to the num variable
    num = int(map(mouseX,0,width,0,24))
    background(0) #black
    translate(width/2, height/2) #move origin to center of screen
    for i in range(num): #"make this many lines"
        stroke(255) #white lines
        line(0,-height/2,0, height/2)
        rotate(PI/float(num))
    for i in range(num): #"Make this many balls"
        shift = i*PI/float(num) #phase shift for sine function
        ball(50+width/float(num)*i,20,shift,i) #call ball function
        rotate(PI/float(num))
    #saveFrame("####.png") #uncomment to save every frame as a png to make a gif
        
def ball(distance,sz,shift,i):
    '''num balls in a circular wave'''
    pushMatrix() #save this orientation
    noStroke() #no outline on circles
    #here's the scary sine wave function
    y = ((height - sz)/2.0)*sin(frameCount/30.0-shift)
    fill(10*i,255,255) #Make the balls rainbow colored
    ellipse(0,y,sz,sz)
    popMatrix() #return to saved orientation
    
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
    
