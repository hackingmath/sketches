sz = 5
ang = 0

def setup():
  size(800,800)
  noFill()
  ellipseMode(CORNER)
  #stroke(0,100)
  background(255)
  
def draw():
  global sz,ang
  sz += 1
  ang += 1
  #background(255)
  translate(width/2,height/2)
  rotate(radians(-ang))
  my_ellipse(0,0,sz,1.5*sz)
  '''if frameCount %4 == 0:
      saveFrame("####.png")'''
  
def my_ellipse(a,b,c,d):
  pushMatrix()
  translate(-c/2.0,0)
  ellipse(a,b,c,d)
  popMatrix()
