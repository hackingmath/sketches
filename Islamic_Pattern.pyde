from time import sleep
sz = 400 #size of big square
step = 0

def setup():
    size(600,600)
    rectMode(CENTER)
    noFill()
    
def draw():
    global step,sz
    background(255) #white
    stroke(0) #black
    strokeWeight(1)
    if step < 26:
        translate(width/2,height/2)
    stroke(0) #gray
    if step > 0:
        rect(0,0,sz,sz)
    if step > 1:
        circle(0,0,sz)
    if step > 2:
        polygon(sz/2.0,8)
    if step > 3:
        polygon(sz/2,4)
    if step > 4:
        pushMatrix()
        rotate(PI/4.0)
        polygon(sz/2,4)
        popMatrix()
    if step > 5:
        pushMatrix()
        rotate(PI/8.0)
        for i in range(8):
            line(-sz/2.0,-sz/2.0,sz/2.0,sz/2.0)
            rotate(PI/4.0)
        popMatrix()
    if step > 6:
        h = 0.5*sz*tan(PI/8.0)
        pt1 = PVector(-sz/2.0,-h)
        pt2 = PVector(-0.5*sz/sqrt(2),-0.5*sz/sqrt(2))
        ellipse(pt1[0],pt1[1],10,10)
    if step > 7:
        ellipse(pt2[0],pt2[1],10,10)
        d = dist(pt1[0],pt1[1],pt2[0],pt2[1])
        old_hyp = sqrt(h**2+(sz/2.0)**2)
        hyp = old_hyp - d
        x,y = -hyp*cos(PI/8.0),-hyp*sin(PI/8.0)
    if step > 8:
        ellipse(x,y,10,10)
        stroke(0)
    if step > 9:
        circle(0,0,2*hyp)
        reflectedx,reflectedy = x,-y
        
    if step > 10:
        line(x,-y,-y,x)
    if step > 11:
        ellipse(0.173*x,y,10,10)
    if step > 12:
        stroke(0,0,255) #blue
        strokeWeight(2)
        line(0.173*x,y,1.45*x,y)
    if step > 13:
        #reflect the line
        line(0.173*x,-y,1.45*x,-y)
    if step > 14:
        pushMatrix()
        translate(1.45*x,y)
        rotate(5*PI/8)
        line(0,0,115/400.0*sz,0)
        popMatrix()
        
    if step > 15:
        pushMatrix()
        translate(1.45*x,-y)
        rotate(-5*PI/8)
        line(0,0,115/400.0*sz,0)
        popMatrix()
    pushMatrix()
    if step > 16:
        rotate(PI/4.0)
        tile(sz)
    if step > 17:
        rotate(PI/4.0)
        tile(sz)
    if step > 18:
        rotate(PI/4.0)
        tile(sz)
    if step > 19:
        rotate(PI/4.0)
        tile(sz)
    if step > 20:
        rotate(PI/4.0)
        tile(sz)
    if step > 21:
        rotate(PI/4.0)
        tile(sz)
            
    if step > 22:
        rotate(PI/4.0)
        tile(sz)
    if step > 23:
        background(255)
        design(sz)
    if step > 24:
        background(255)
        sz = 150.0
        design(sz)
    popMatrix()
    if step > 25:
        background(255)
        for x in range(5):
            for y in range(5):
                pushMatrix()
                translate(sz*x,sz*y)
                
                design(sz)
                popMatrix()
    if frameCount % 4 == 0:
        pass#saveFrame("####.jpg")
    
def design(sz):
    for i in range(8):
        tile(sz)
        rotate(PI/4.0)
                
def tile(sz):
    h = 0.5*sz*tan(PI/8.0)
    pt1 = PVector(-sz/2.0,-h)
    pt2 = PVector(-0.5*sz/sqrt(2),-0.5*sz/sqrt(2))
    #ellipse(pt1[0],pt1[1],10,10)
    #ellipse(pt2[0],pt2[1],10,10)
    d = dist(pt1[0],pt1[1],pt2[0],pt2[1])
    old_hyp = sqrt(h**2+(sz/2.0)**2)
    hyp = old_hyp - d
    x,y = -hyp*cos(PI/8.0),-hyp*sin(PI/8.0)
    #ellipse(x,y,10,10)
    stroke(0)
    #circle(0,0,2*hyp)
    reflectedx,reflectedy = x,-y
    stroke(0,0,255) #red
    strokeWeight(2)
    #line(x,-y,-y,x)
    #ellipse(0.173*x,y,10,10)
    line(0.173*x,y,1.45*x,y)
    #reflect the line
    line(0.173*x,-y,1.45*x,-y)
    
    pushMatrix()
    translate(1.45*x,y)
    rotate(5*PI/8)
    line(0,0,115/400.0*sz,0)
    popMatrix()
    
    pushMatrix()
    translate(1.45*x,-y)
    rotate(-5*PI/8)
    line(0,0,115/400.0*sz,0)
    popMatrix()
    

    
def polygon(r,num):
    """Draws a polygon of num sides
    with radius r"""
    a = TWO_PI/num
    for i in range(num):
        line(r*cos(i*a),r*sin(i*a),
             r*cos((i+1)*a),r*sin((i+1)*a))
        
def keyPressed():
    global step
    if key == CODED:
        if keyCode == UP:
            step += 1
        if keyCode == DOWN:
            step -= 1
    
