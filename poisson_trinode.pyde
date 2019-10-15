#https://www.facebook.com/michel.poisson/posts/10156597025576723?comment_id=10156598962286723&reply_comment_id=10156599214236723

"""Michael Poisson's sketch on FB
October 15, 2019"""

PINK = color(255,0,255)

def setup():
    size(600,600)
    stroke(PINK)
    
    
def draw():
    
    sz = 100
    fill(0,25)
    rect(0,0,width,height)
    translate(width/2,height/2)
    for (x,y) in [(sz,0),(0,sz),(-sz,0),(0,-sz)]:
        fill(PINK)
        ellipse(x,y,20,20)
    for i in range(4):
        pushMatrix()
        rotate(i*radians(90))
        translate(sz,0)
        trinode(sz,45+45*sin(frameCount/100.0),5)
        popMatrix()
    #if frameCount %2 == 0:
    #    saveFrame("####.png")
    #if frameCount > 648:
    #    noLoop()
        
def trinode(sz,ang,level):
    fill(PINK)
    if level > 0:
        for j in range(2):
            pushMatrix()
            rotate(radians((-1)**j*ang))
            line(0,0,sz,0)
            translate(sz,0)
            ellipse(0,0,8,8)
            trinode(sz,ang,level-1)
            popMatrix()
