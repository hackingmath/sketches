''' Cloning Arjan van der Meij's sketch
https://twitter.com/arjanvandermeij/status/1121882861517398016
April 30, 2019'''

sz = 10;

def setup():
    size(600,600);
    rectMode(CENTER);

def draw():
    background(255); 
    translate(width/2,height/2);
    circle_square_thing(10);

def circle_square_thing(c):
    bin_c = binary(c); # converts c to binary
    println(bin_c);
    for i in range(7, -1,-1):
        if (bin_c[i] == '0'):
            ellipse(0,0,sz*(8-i),sz*(8-i));
        else:
            rect(0,0,sz*(8-i),sz*(8-i));
