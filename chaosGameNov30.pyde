'''Chaos Game
inspired by Shiffman
November 30, 2018'''

from random import randint, choice, sample

PURPLE = color(153,50,204)

def setup():
    size(600,600)
    stroke(0,255,0)
    
def draw():
    background(255)
    #fill(255,50)
    #rect(0,0,width,height)
    #chaosReg(7)
    chaosPentagram()
    noLoop()
    
def midpt(A,B):
    '''returns the midpoint of points A and B'''
    return ((A[0]+B[0])/2.0,
        (A[1]+B[1])/2.0)
    
def chaos(num_sides):
    '''Chaos game with random n-gon'''
    
    #start with n random points for vertices of 
    pts = [(randint(0,width),randint(0,height)) \ 
             for i in range(num_sides)]
    
        #ellipse(pt[0],pt[1],20,20)
    #first internal random point
    random_pt = (randint(0,width),randint(0,height))
    for i in range(10000):
        pts.append((random_pt[0],random_pt[1]))
        random_vertex = choice(pts[:4])
        random_pt = midpt(random_pt,random_vertex)
    stroke(PURPLE)
    for pt in pts:
        point(pt[0],pt[1])
    
def chaosReg(num_sides):
    '''Chaos game with regular n-gon'''
    
    r = width/2
    pts = [(r+250*cos(radians(i*360/float(num_sides))),
            r+250*sin(radians(i*360/float(num_sides)))) \ 
             for i in range(num_sides)]
    
    #first internal random point
    random_pt = (randint(0,width),randint(0,height))
    for i in range(1000000):
        pts.append((random_pt[0],random_pt[1]))
        random_vertex = choice(pts[:num_sides])
        random_pt = midpt(random_pt,random_vertex)
    for pt in pts:
        point(pt[0],pt[1])
        
def chaosPent(num_sides=5):
    '''A point inside a pentagon repeatedly jumps half of the 
    distance towards a randomly chosen vertex, but the currently 
    chosen vertex cannot be the same as the previously chosen 
    vertex.'''
    
    r = width/2
    pts = [(r+250*cos(radians(i*360/float(num_sides))),
            r+250*sin(radians(i*360/float(num_sides)))) \ 
             for i in range(num_sides)]
    #keep track of "current vertex" chosen
    current = 0 #the real one will be assigned later
    #first internal random point
    random_pt = (randint(0,width),randint(0,height))
    for i in range(1000000):
        pts.append((random_pt[0],random_pt[1]))
        choice1,choice2 = sample(pts[:num_sides],2)
        if choice1 == current:
            random_vertex = choice2
            current = choice2
        else:
            random_vertex = choice1
            current = choice1
        random_pt = midpt(random_pt,random_vertex)
    stroke(0,50)
    for pt in pts:
        point(pt[0],pt[1])
        
def chaosPentagram(num_sides=5):
    '''A point inside a pentagon repeatedly jumps half of the 
    distance towards a randomly chosen vertex, but the currently 
    chosen vertex cannot be 1 or 4 places, respectively away from 
    the two previously chosen vertices.'''
    #Vertices you can't choose from 
    no_verts = []
    r = width/2
    #generate vertices of regular n-gon
    pts = [(r+250*cos(radians(i*360/float(num_sides))),
            r+250*sin(radians(i*360/float(num_sides)))) \ 
             for i in range(num_sides)]
    #keep track of "current vertex" chosen
    current = 0 #the real one will be assigned later
    #first internal random point
    random_pt = (randint(0,width),randint(0,height))
    for i in range(10000000):
        pts.append((random_pt[0],random_pt[1]))
        choice1,choice2,choice3 = sample(pts[:num_sides],3)
        if choice1 in no_verts:
            if choice2 in no_verts:
                random_vertex = choice3
            else:
                random_vertex = choice2
        else:
            random_vertex = choice1
            current = random_vertex

        if current == pts[0]:
            no_verts.append(pts[1])
            no_verts.append(pts[4])
        elif current == pts[1]:
            no_verts.append(pts[2])
            no_verts.append(pts[0])
        elif current == pts[2]:
            no_verts.append(pts[3])
            no_verts.append(pts[1])
        elif current == pts[3]:
            no_verts.append(pts[4])
            no_verts.append(pts[2])
        elif current == pts[4]:
            no_verts.append(pts[0])
            no_verts.append(pts[3])
        if len(no_verts)>4:
            no_verts.remove(no_verts[0])
            no_verts.remove(no_verts[1])
            
        random_pt = midpt(random_pt,random_vertex)
    stroke(0,50)
    for pt in pts:
        point(pt[0],pt[1])
    
def chaosRand():
    '''Chaos game with 3 random points'''
    pt1 = (randint(0,width),randint(0,height))
    pt2 = (randint(0,width),randint(0,height))
    pt3 = (randint(0,width),randint(0,height))
    point(pt1[0],pt1[1])
    point(pt2[0],pt2[1])
    point(pt3[0],pt3[1])
    #first internal random point
    random_pt = (randint(0,width),randint(0,height))
    for i in range(100000):
        point(random_pt[0],random_pt[1])
        random_vertex = choice([pt1,pt2,pt3])
        random_pt = midpt(random_pt,random_vertex)
