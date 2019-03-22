'''From the Inspiring Maths twitter feed:
https://twitter.com/inspiringmaths/status/1108777036544245761
'''

SZ = 20 #size of Equilateral Triangle

def setup():
    size(600,600)
    #noStroke()
  
def draw():
    #translate(width/2,height/2)
    rotate(radians(15))
    for x in range(10):
        for y in range(-2,9):
            if x % 2 == 0:
                design(x*3*sqrt(3)*SZ,y*6*SZ-3*SZ)
            else:
                design(x*3*sqrt(3)*SZ,y*6*SZ)
  
def design(x,y):
    pushMatrix()
    translate(x,y)
    hexagon()
    star()  
    popMatrix()
  
def tri():
    global SZ
    beginShape()
    for i in range(3):
        vertex(SZ*cos(radians(120*i)),
               SZ *sin(radians(120*i)))
    endShape(CLOSE)
  
def diamond():
    global SZ
    pushMatrix()
    translate(2*SZ,0)
    tri()
    translate(-SZ,0)
    rotate(PI)
    tri()
    popMatrix()
  
def star():
    rotate(radians(-90))
    fill(100) #dark gray
    stroke(100)
    for i in range(3):
        diamond()
        rotate(radians(120))
    rotate(radians(60))
    fill(200) #light gray
    stroke(200)
    for i in range(3):
        diamond()
        rotate(radians(120))
    
def hexagon():
    global SZ
    fill(255)
    stroke(101, 67, 33) #brown
    beginShape()
    for i in range(6):
        vertex(2*sqrt(3)*SZ*cos(radians(60*i)),
            2*sqrt(3)*SZ*sin(radians(60*i)))
    endShape(CLOSE)
    noStroke()
