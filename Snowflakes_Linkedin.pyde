'''Cloning the background at the Bay Piggies meeting
at LinkedIn last night
December 21, 2018'''

GRAV = PVector(0,.005) #force of gravity

class Snowflake:
    def __init__(self):
        self.sz = random(5,80)
        self.loc = PVector(random(width),-random(height))
        self.vel = PVector(random(-1,1),self.sz/20.0)
        
    def update(self):
        #self.loc.x += 0.0125*self.sz*random(-3,3) #left-right wiggle
        self.vel.add(GRAV)
        self.loc.add(self.vel)
        stroke(255,100)
        strokeWeight(self.sz/5.0)
        pushMatrix()
        translate(self.loc.x,self.loc.y)
        for i in range(6):
            rotate(radians(60))
            pushMatrix()
            line(0,0,0,-self.sz)
            translate(0,-2*self.sz/3.0)
            rotate(radians(60))
            line(0,0,0,-self.sz/3.0)
            rotate(radians(-120))
            line(0,0,0,-self.sz/3.0)
            popMatrix()
        popMatrix()
        if self.loc.y > height + self.sz:
            snowflakeList.append(Snowflake())
            snowflakeList.remove(self)
            
            

def setup():
    global snowflakeList
    size(600,600)
    snowflakeList = [Snowflake() for i in range(75)]
    
def draw():
    #frameRate(40)
    global snowflakeList
    background(0)
    for s in snowflakeList:
        s.update()
    if frameCount % 2 == 0:
        saveFrame("####.png")
