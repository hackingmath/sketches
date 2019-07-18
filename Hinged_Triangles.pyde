'''cloning beesandbombs' hinged triangles sketch
https://twitter.com/beesandbombs/status/1148571860449341440
July 18, 2019'''

class TrianglePair:
  def __init__(self,x,y,sz,col):
    self.x = x
    self.y = y
    self.sz = sz
    self.col = col
    self.angle = 0
    self.state = 0 #0-60,60-120, etc
    #hinge states to "rotate" colors appropriately
    if self.col == RED:
      self.hinge_state = 1
    if self.col == BLACK:
      self.hinge_state = 2
    if self.col == BLUE:
      self.hinge_state = 3
    
  def update(self,t):
    fill(self.col)
    pushMatrix()
    translate(self.x,self.y) #go to rotation center
    for i in range(self.state//4+self.hinge_state):
      self.rotate_hinge()
    pushMatrix() #save this orientation
    for i in range(2):
      triangle(0,0,
              -self.sz,0,
              -self.sz/2.0,-self.sz*0.866)
      #put "ease" to work to speed/slow rotation
      rot = ease(t,5)*60 + 60*(self.state%4)  
      #add that to the rotation angle
      rotate(radians(self.angle + 60 +rot))
    popMatrix() #return to saved orientation
    popMatrix()
      
  def rotate_hinge(self): #change hinge location
    translate(-self.sz/2,-self.sz/(2*1.732)) #to center of stationary tri
    rotate(TWO_PI/3) #rotate hinge
    translate(self.sz/2,self.sz/(2*1.732))
    
class Triple: #the "triplet" of triangles
  def __init__(self,x,y,sz):
    self.x = x
    self.y = y
    self.sz = sz
    self.trilist = [TrianglePair(self.x,self.y,self.sz,RED),
                    TrianglePair(self.x-self.sz*2,self.y,self.sz,BLACK),
                    TrianglePair(self.x-self.sz,self.y-1.732*self.sz,self.sz,BLUE)]
  
  def update(self,t): #draw the triangles
    for tri in self.trilist:
      tri.update(t)
      
  def update_state(self):
    for tri in self.trilist:
      tri.state += 1 #next rotation range
    
def setup():
  global sz,triplist,t,BLACK,BLUE,RED
  size(500,500)
  BLACK = color(0)
  BLUE = color(0,150,200)
  RED = color(200,0,0)
  noStroke()
  sz = 30
  t = 0
  triplist = []
  for r in range(8):
    for c in range(8):
      if c % 2 == 0:
        triplist.append(Triple(c*3*sz,
                                r*2*1.732*sz,sz))
      else: #move every other column down a bit
        triplist.append(Triple(c*3*sz,
                                r*2*1.732*sz-1.732*sz,sz))
  
  
def draw():
  global t,triplist
  background(255)

  for trip in triplist:
    trip.update(t)
  t += 0.04
  if t > 1:
    t = 0
    for trip in triplist:
      trip.update_state()
  saveFrame("####.png")
  
def ease(p,g):
  if p < 0.5:
    return 0.5 * (2*p)**g
  else:
    return 1 - 0.5 * (2*(1 - p))**g
  
  
def triangleCENTER(x,y,sz): #not used anymore
  beginShape()
  for i in range(3):
    vertex(x+sz*cos(radians(i*120+30)),
          y + sz*sin(radians(i*120+30)))
  endShape(CLOSE)
