'''American Flag
July 4, 2019'''
import time
import random

RED = color(255,0,0)
WHITE = color(255)
BLUE = color(0,0,155)
t = 0
stripe_num = 0
starList = []
star_nums = random.sample(range(50),50)
star_num = 50

class Star:
    def __init__(self,x,y,sz):
        self.x = x
        self.y = y
        self.sz = sz
        self.on = False
    
    def render(self):
        if self.on:
            fill(WHITE)
            pushMatrix()
            beginShape()
            for i in range(5):
                vertex(self.x+self.sz*cos(i*radians(144)-PI/2),
                    self.y+self.sz*sin(i*radians(144)-PI/2))
            endShape(CLOSE)
            popMatrix()

class Stripe:
    def __init__(self,col,_width,_height,x,y):
        self.col = col
        self._width = _width
        self._height = _height
        self.x = x
        self.y = y
        self.drawn = False
        
    def render(self,ratio):
        fill(self.col)
        #for i in range(100):
        if not self.drawn:
            rect(self.x,self.y,self._width*ratio,self._height)
        else:
            rect(self.x,self.y,self._width,self._height)
            
class Flag:
    def __init__(self):
        global starList
        self.loc = (0,0)
        stripe_height = height / 13.0
        self.stripeList = []
        for i in range(6):
            if i < 3:
                stripe_x = 0
                stripe_width = width
            else:
                stripe_x = (0.76/1.9)*width
                stripe_width = ((1.9-0.76)/1.9)*width
            self.stripeList += [Stripe(RED,stripe_width,stripe_height,
                                       stripe_x,height-(2*i+1)* \ 
                                    stripe_height),
                                Stripe(WHITE,stripe_width,stripe_height,
                                       stripe_x,height-(2*i+2)* \ 
                                    stripe_height)]
        self.stripeList += [Stripe(RED,stripe_width,stripe_height,(0.76/1.9)*width,height-13* \ 
                                  stripe_height)]
        

def setup():
    global flag1,starList
    flag1 = Flag()
    size(1200,600)
    noStroke()
    for x in range(6):
        for y in range(5):
            starList.append(Star(30+x*80,30+y*65,15))
    for c in range(5):
        for r in range(4):
            starList.append(Star(70+c*80,60+r*65,15))
    
def draw():
    global flag1,t,stripe_num,starList,star_num
    background(BLUE)
    #t = 0
    for stripe_num2 in range(13):
        s = flag1.stripeList[stripe_num2]
        if s.drawn:
            s.render(1)
    flag1.stripeList[stripe_num].render(t)
    t += 0.05
    if t >= 1:
        t = 0
        flag1.stripeList[stripe_num].drawn = True
        stripe_num += 1
        if stripe_num == 13:
            star_num = 0
            stripe_num = 0
    # println(len(starList))
    # if star_num < 50:
    #     starList[star_num].render()
    if star_num > 49:
        star_num += 1
    else:
        starList[star_nums[star_num]].on = True
        star_num += 1
    for s in starList:
        s.render()
    saveFrame("####.png")
