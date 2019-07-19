def setup():
  size(500,500)
  stroke(128,0,255)#white lines
  colorMode(HSB)
  
def draw():
  step = int(map(mouseX,0,500,2,20))
  step2 = int(map(mouseY,0,500,1,255))
  background(0) #0 is black
  #translate(width/2,height/2)
  for i in range(step+1):
    for j in range(step+1):
      scl = width/step
      pushMatrix()
      translate(i*scl,j*scl)
      #rotate(radians(step))
      #stroke(step2,0,step)
      strokeWeight(1)
      stroke(10*(i+j),255,255)
      astroid(100,10)
      popMatrix()
  #saveFrame("####.png")
  
  
def astroid(sz,step):
  for i in range(0,sz+1,step):
    line(i,0,0,sz-i)
    line(-i,0,0,sz-i)
    line(i,0,0,i-sz)
    line(-i,0,0,-sz+i)
