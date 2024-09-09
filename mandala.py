"""Mandala
Sept. 8, 2024"""

from turtle import *
from math import pi,sqrt

shape('turtle')

def circle(r):
    """C = 2*pi*r
    if you only turned 1 degree
    the 'fd' would be 2*pi*r/360
    but using 90 it's pi*r/45"""
    d = 2*pi*r/360#pi*r/45
    pensize(3)
    pu()
    fd(r)
    lt(90)
    pd()
    for i in range(360):
        fd(d)
        lt(1)

def mandala(d):
    """d is distance between centers"""
    ds = d*sqrt(3)
    locations = [
        (0,0),
        (0,d),
        (0,2*d),
        (0,-d),
        (0,-2*d),
        (ds/2,d/2),
        (ds/2,d*1.5),
        (ds/2,-d/2),
        (ds/2,-d*1.5),
        (ds,d),
        (ds,0),
        (ds,-d),
        (-ds/2,d/2),
        (-ds/2,d*1.5),
        (-ds/2,-d/2),
        (-ds/2,-d*1.5),
        (-ds,d),
        (-ds,0),
        (-ds,-d)
        ]
    for loc in locations:
        pu()
        goto(loc[0],loc[1])
        circle(d)
        ht()

tracer(10)
mandala(100)
