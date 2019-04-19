'''Cloning Hazel Clementine's sea sketch
https://twitter.com/clementinehazel/status/1113305640502538241
April 19, 2019'''

def setup():
    global freq,t,dt
    size(1000,400)
    freq = 0.00001*width
    t = 0
    dt = 1
    
def draw():
    global freq,t,dt
    background(255)
    strokeWeight(1)
    # graph_function(f1)
    # graph_function(f2)
    # graph_function(f3)
    # graph_function(f4)
    strokeWeight(8)
    for i in range(20,width-20,15):
        stroke(145,187,211)
        line(i,10,i,f1(i))
        stroke(197, 222, 226)
        line(i,f1(i)+20,i,f2(i))
        stroke(136, 211, 226)
        line(i,f2(i)+20,i,f3(i))
        stroke(100,134,140)
        line(i,f3(i)+20,i,f4(i))
        stroke(50,81,86)
        line(i,f4(i)+20,i,height-40)
    t += dt
    if frameCount % 2 == 0:
        saveFrame("####.png")
    if frameCount > TWO_PI / freq:
        noLoop()
    
def f1(x):
    global freq
    return 60 + 50*sin(freq*(x-t))

def f2(x):
    return 130 + 80*sin(freq*(x-t)+19.5)

def f3(x):
    return 210 + 80*sin(freq*(x-t)+20.25)

def f4(x):
    return 280 + 60*sin(freq*(x-t)+21)

def graph_function(f):
    point_list = [f(x) for x in range(width)]
    x = 0
    while x < width:
        line(x,f(x),x+1,f(x+1))
        x += 1
        
    
