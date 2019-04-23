def setup(): #run once
    global step, diam,t 
    colorMode(HSB)
    noStroke() #no outline
    global diam,t #let other functions use this variable
    size(600,600)
    diam = 20 #diameter of circles
    t = 0 #time
    step = 0
  
def draw(): #infinite loop
    global t,step
    background(0)
    if step == 0:
        pass
    elif step == 1:
        fill(255)
        ellipse(0,0,diam,diam)
    elif step == 2:
        ellipse(0,height/2,diam,diam)
    elif step == 3:
        for i in range(int(width/diam)+1):
            ellipse(i*diam,height/2,diam,diam)
    elif step == 4:
        for i in range(int(width/diam)+1):
            ellipse(i*diam,height/2+sin(t),diam,diam)
    elif step == 5:
        for i in range(int(width/diam)+1):
            ellipse(i*diam,height/2+200*sin(t),diam,diam)
    elif step == 6:
        for i in range(int(width/diam)+1):
            ellipse(i*diam,height/2+200*sin(t+i),diam,diam)
    elif step == 7:
        for i in range(int(width/diam)+1):
            ellipse(i*diam,height/2+200*sin(t+i/5.0),diam,diam)
    elif step == 8:
        for i in range(int(width/diam)+1):
            fill(7*i,255,255) #hue (color), saturation, brightness
            ellipse(i*diam,height/2+200*sin(t+i/5.0),diam,diam) #(x,y,width,height)
    t += 0.05 #increment time
    #saveFrame("####.png")

def keyPressed():
    global step
    if key == CODED:
        if keyCode == UP:
            step = (step + 1) % 9
        if keyCode == DOWN:
            step = (step - 1) % 9
