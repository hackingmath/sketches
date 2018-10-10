'''Shiffman's Lissajous Curve Table
Coding Challenge
October 9, 2018
with Aryan'''

w = 70
t = 0
dt = 0.003
dotList = []

def setup():
    global w,cols
    size(600,600)
    
    
    cols = width/w - 1
    
def draw():
    global cols,w, t,dotList
    
    background(0)
    d = w - 10
    r = d / 2
    for i in range(cols):
        stroke(255)
        noFill()
        #top row
        x = w + i * w + w/2.0
        y = w / 2.0
        ellipse(x,y,d,d)
        x2 = x + r*cos(t*(i+1))
        y2 = y + r*sin(t*(i+1))
        line(x2,0,x2,height)

        ellipse(x2,y2,5,5)
        t += dt
        
        #left column:
        y = w + i * w + w/2.0
        x = w / 2.0
        ellipse(x,y,d,d)
        x3 = x + r*cos(t*(i+1))
        y3 = y + r*sin(t*(i+1))
        line(0,y3,width,y3)
        ellipse(x3,y3,5,5)
        
        #dot
        #fill(255,0,0)
        dotList.append((x2,y3))
    if len(dotList) > 1:
        for i,dot in enumerate(dotList):
            if i < len(dotList) - 1:
                stroke(0,255,0)
                line(dot[0],dot[1],
                    dotList[i+1][0],dotList[i+1][1])
        
def design(horiz,vert):
    '''draws the Lissajous with a given horizontal
    and vertical frequency'''
    
