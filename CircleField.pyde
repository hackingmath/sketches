'''Cloning another B&B sketch
https://twitter.com/beesandbombs/status/1039972818467868673
Sept. 12, 2018'''

ROWS = 34
COLS = 34
sz = 24 #small size of circle
t = 0
dt = 0.1

def setup():
    size(600,600)
    noFill()
    
def draw():
    global t, dt
    #frameRate(10)
    background(255)
    translate(width/2,height/2)
    for r in range(ROWS):
        for c in range(COLS):
            if r % 2 == 0:
                x = -15*sz + sz*c
                y = -15*sz + r*sz/2.0*sqrt(3)
            else:
                y = -15*sz + r*sz/2.0*sqrt(3)
                x = -15.5*sz + sz*c
            #diam = sz#map(mouseX,0,600,sz,sz*2)
            #d2 = sz+diam*sin(t/1.0*((x/10.0)**2+(y/10.0)**2))
            #d = constrain(d2,sz,sqrt(2)*sz)
            if (r*COLS + c) % 4 ==0:
                stroke(255,0,0)
            elif (r*COLS + c) % 4 ==1:
                stroke(255,0,255)
            elif (r*COLS + c) % 4 ==2:
                stroke(155,155,0)
            else:
                stroke(0,155,155)
            if frameCount < 50:
                ellipse(x,y,sz,sz)
            elif frameCount > 50 and frameCount < 200:
                fc = frameCount-100
                d = lerp(sz,sz*sqrt(3),fc/20.0+(10000-((x)**2+(y)**2))/100000.0)
                #d = *)
                d = constrain(d,sz,sz*sqrt(3))
                ellipse(x,y,d,d)
            else:
                fc = frameCount-200
                d = lerp(sz*sqrt(3),sz,fc/20.0+(10000-((x)**2+(y)**2))/100000.0)
                #d = *)
                d = constrain(d,sz,sz*sqrt(3))
                ellipse(x,y,d,d)
            if frameCount > 400:
                noLoop()
    #if frameCount % 2 == 0:
        #saveFrame('####.png')
