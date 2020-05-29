#Cloning a tweet by Vincent Pantaloni
#https://twitter.com/panlepan/status/1266010656232427525
#May 28, 2020

sz = 20;
t=0;
GREEN = color(0,255,0);
YELLOW = color(255,255,0);
RED = color(255,0,0);
CYAN = color(0,255,255);
PURPLE = color(255,0,255);
ORANGE = color(255,140,0);

def setup():
    size(600,600);
    noStroke();

def draw():
    global t
    background(0);
    translate(width/2.0,height/2.0);
    t+=0.5;
    field(sz,GREEN,t);
    rotate(PI/3);
    field(sz,YELLOW,t);
    rotate(PI/3);
    field(sz,CYAN,t);
    rotate(PI/3);
    field(sz,PURPLE,t);
    rotate(PI/3);
    field(sz,ORANGE,t);
    rotate(PI/3);
    field(sz,RED,t);
    saveFrame("####.jpg")
  

def rhombus(x,y,sz,col):
    pushMatrix();
    translate(x,y);
    fill(col);
    beginShape();
    vertex(0,0);
    vertex(sz/2.0,sz*0.5*sqrt(3));
    vertex(0,sz*sqrt(3));
    vertex(-sz/2.0,sz*0.5*sqrt(3));
    endShape(CLOSE);
    popMatrix();

def field(sz,col,t):
    rhombus(-t,0,sz,col);
    gridsz = 6*sz;
    for i in range(-5,6):
        for j in range(-5,6):
            if j%2==0:
                rhombus(i*gridsz-t,j*gridsz*0.5*sqrt(3),sz,col);
            else:
                rhombus(i*gridsz-t+gridsz/2.0,j*gridsz*0.5*sqrt(3),sz,col);
