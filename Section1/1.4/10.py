#10.py
#by John Slattery on December 10, 2018
#This Script displays information about a rectangle drawn by the user

import graphics
from graphics import *
import time
import math

def main():
    win = GraphWin("Triangle Satatics")
    win.setCoords(-10,-20,20,20)
    p = win.getMouse()
    c = win.getMouse()
    g = win.getMouse()
    rectangle = Polygon(Point(p.getX(),p.getY()), Point(c.getX(),c.getY()), Point(g.getX(),g.getY()))
    rectangle.draw(win)
    px = abs(p.getX())
    py = abs(p.getY())
    cx = abs(c.getX())
    cy = abs(c.getY())
    gx = abs(g.getX())
    gy = abs(g.getY())
    sidea = math.sqrt((px - cx)**2 + (py - cy))
    sidea = abs(sidea)
    sideb = math.sqrt((cx - gx)**2 + (cy - gy))
    sideb = abs(sideb)
    sidec = math.sqrt((gx - px)**2 + (gy - py))
    sidec = abs(sidec)
    s = (sidea + sideb +sidec)/2
    abs(s)
    area = math.sqrt(s * abs(s - sidea) * abs(s - sideb) * abs(s - sidec))
    print("The area is: ", math.floor(area))
    permiter = sidea + sideb + sidec
    print("The Permiter is: ", math.floor(permiter))
    win.getMouse()
    win.close()
main()