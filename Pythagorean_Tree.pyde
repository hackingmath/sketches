"""Pythagorean Tree 
Inspired by Lauwerier's book
"""
    
def setup():
    size(600,600)
    noStroke()
    colorMode(HSB)
    
def draw():
    background(0)
    translate(250,450)
    ang = map(mouseX,0,width,0,90)
    level = map(mouseY,0,height,1,20)
    tree(80,ang,level)
    saveFrame("####.png")
    
def tree(sz,ang,level):
    if level > 0:
        fill(level*20,255,255)
        rect(0,0,sz,sz)
        leftsz = sz*cos(radians(ang))
        rightsz = sz*sin(radians(ang))
        pushMatrix()
        rotate(radians(-ang))
        translate(0,-leftsz)
        tree(leftsz,ang,level-1)
        popMatrix()
        pushMatrix()
        rotate(radians(90-ang))
        translate(0,-(leftsz+rightsz))
        tree(rightsz,ang,level-1)
        popMatrix()
