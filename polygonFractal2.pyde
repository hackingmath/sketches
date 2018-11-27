'''Polygon Fractal
with Jared
November 20, 2018'''

def setup():
    global sides
    size(600,600)
    noFill()
    colorMode(HSB)
    sides = 3 #beginning value
    
def draw():
    global sides
    background(0) #black background
    translate(width/2,height/2) #center the sketch
    #change the polygons every 100 frames
    if frameCount % 100 == 0:
        sides = int(random(3,7))
    #call the pFractal function
    pFractal(sides,300,20)
    #uncomment to save screenshots to create a gif:
    '''if frameCount % 3 == 0:
        saveFrame("####.png")'''
    
def pFractal(sides, r,level):
    '''Creates a fractal of "level" nested polygons with given
    number of sides, "radius" from center.'''
    if level > 0:
        #half apex (interior) angle
        angle_C = 0.5*radians(180-360/float(sides))
        #angle_A = map(mouseX,0,600,0,PI/2) #to change angle manually
        #oscillate angle of smaller polygons in fractal
        angle_A = radians(30 + 30*sin(frameCount/float(100)))
        angle_B = PI -(angle_C+angle_A)
        #calculate new radius using Law of Sines
        newr = r*sin(angle_C)/sin(angle_B)
        stroke(level*10,255,255) #color of outline varies with level
        polygon(sides,r) #create a polygon
        rotate(angle_A) #rotate the figure
        pFractal(sides,newr,level-1) #recursion! Make more fractals inside polygon.
    
    
def polygon(sides,radius):
    '''Draws a polygon of given number of sides
    and radius from center.
    Uses a sort of polar coordinates method.'''
    central_angle = TWO_PI/float(sides)
    beginShape()
    for i in range(sides):
        vertex(radius*cos(central_angle*i),
               radius*sin(central_angle*i))
    endShape(CLOSE)
