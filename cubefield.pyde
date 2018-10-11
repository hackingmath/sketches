'''Cloning a Bees and Bombs sketch from Oct 2.
Oct. 5, 2016
with Callum and Curtis'''

side = 8 #number of cubes on a side
setting = 1 #black background

def setup():
    size(600,600,P3D)
    rectMode(CENTER)
    noStroke()
    
def draw():
    global side,setting
    if dist(mouseX,mouseY,0,600)<20:
        setting = 2
    if dist(mouseX,mouseY,600,0)<20:
        setting = 1
    if setting == 1:
        background(0) 
        translate(width/2,height/2,-500)
        sz = width/float(side)*2
        rot = map(mouseX,0,width,0,TWO_PI)
        tilt = map(mouseY,0,width,0,TWO_PI)
        #println(str(mouseX)+","+str(mouseY))
        for x in range(-4,5):
            for y in range(-4,5):
                if (x + y) % 2 == 0:
                    pushMatrix() #save this orientation
                    translate(x*sz,y*sz,0)
                    rotateY(rot)
                    rotateX(tilt)
                    fill(255)
                    cube(sz)
                    popMatrix() #resets the orientation
    if setting == 2:
        background(255) 
        translate(width/2,height/2,-500)
        sz = width/float(side)*2
        rot = map(mouseX,0,width,0,TWO_PI)
        tilt = map(mouseY,0,width,0,TWO_PI)
        #println(str(mouseX)+","+str(mouseY))
        for x in range(-4,5):
            for y in range(-4,5):
                if (x + y) % 2 == 1:
                    pushMatrix() #save this orientation
                    translate(x*sz,y*sz,0)
                    rotateY(rot)
                    rotateX(tilt)
                    fill(0)
                    cube(sz)
                    popMatrix() #resets the orientation
    #saveFrame("####.png")
            
def cube(sz):
    #fill(fillnum)
    box(sz)
    #right face
    fill(0,255,255)#CYAN
    beginShape()
    vertex(sz/2.0,sz/2.0,sz/2.0)
    vertex(sz/2.0,sz/2.0,-sz/2.0)
    vertex(sz/2.0,-sz/2.0,-sz/2.0)
    vertex(sz/2.0,-sz/2.0,sz/2.0)
    endShape(CLOSE)
    
    #top Face
    fill(255,0,0)#RED
    beginShape()
    vertex(sz/2.0,sz/2.0+1,sz/2.0)
    vertex(sz/2.0,sz/2.0+1,-sz/2.0)
    vertex(-sz/2.0,sz/2.0+1,-sz/2.0)
    vertex(-sz/2.0,sz/2.0+1,sz/2.0)
    endShape(CLOSE)
