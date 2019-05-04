def setup():
  size(600,600)
  stroke(255)
  strokeWeight(0.5)
  
def draw():
  background(0)
  translate(width/2,height/2)
  #grid()
  for i in range(50):
      pushMatrix()
      translate(random(-width/2.0,width/2),
                random(-width/2.0,width/2))
      rotate(radians(frameCount))
      astroid(random(5,150),20)
      popMatrix()
  #noLoop()
  
def astroid(sz,num):
  '''Draws an astroid of size sz  
  with num lines.'''
  seg = sz/float(num) #length of each step
  for i in range(num+1):
    line(-sz+i*seg,0,0,-i*seg)
    line(sz-i*seg,0,0,-i*seg) 
    line(0,sz-i*seg,-i*seg,0)
    line(0,sz-i*seg,i*seg,0)
  
  

def grid():
  stroke(0,255,255) #cyan
  #horizontal lines
  for i in range(-int(width/2),int(width/2),25):
    line(-width/2,i,width/2,i)
  #vertical lines
  for i in range(-int(width/2),int(width/2),25):
    line(i,-width/2,i,width/2)
  stroke(0)
  line(0,-width/2,0,width/2)
  line(-width/2,0,width/2,0)
