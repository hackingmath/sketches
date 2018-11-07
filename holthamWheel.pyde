'''Cloning the revolving circles sketch of 
Martin Holtham @GHSMaths on Twitter
November 2, 2016'''

RED = color(255,0,0)
GREEN = color(0,255,0)
BLUE = color(0,0,255)
PURPLE = color(153,0,153)
ORANGE = color(238,125,13)

t = 0 #time variable
dt = 0.075 #the change in time

class Wheel:
    def __init__(self,num):
        self.num = num #the "number" of each wheel object
        self.divisions = 2*self.num #the number of "slices" in this wheel
        self.radius = 25*(self.num) #the radius of this wheel
        
    def update(self):
        ang = TWO_PI/float(self.divisions) #central angle
        pushMatrix() #save this orientation
        rotate(-t/float(self.num)) #spin the wheel a little
        for i in range(self.divisions): #draw the slices
            if i % 2 == 0: #alternate colors
                fill(PURPLE)
            else:
                fill(ORANGE)
            #here's the magic: each slice goes from this angle to the next angle!
            arc(0,0,2*self.radius,2*self.radius,
                i*ang,(i+1)*ang,PIE)
        popMatrix() #return to the saved orientation
       
wheelList = [Wheel(i) for i in range(1,13)] #save the wheels in a list
    
def setup():
    size(600,600) #size of the display screen
    
def draw():
    global wheelList,t #declare global variables in Python
    background(0) #background color is black
    translate(width/2.0,height/2.0) #start in center of screen
    for w in wheelList[::-1]: #reverse the wheelList to draw the smallest one last!
        w.update()
    if t < TWO_PI: #saves PNG screenshots for making a gif. Otherwise comment this part out 
        saveFrame("####.png")
    t += dt #increment the time variable each loop
