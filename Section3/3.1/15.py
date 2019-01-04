#15.py
#by John Slattery on January 19, 2019
#This Script will make a line with 2 mouse clicks

import graphics
from graphics import *
import time
import math

def main():
    win = GraphWin("Line Drawer")
    p = win.getMouse()
    c = win.getMouse()
    dx = p.getX()
    dy = p.getY()
    cx = c.getX()
    xx = c.getX() - p.getX()
    yy = c.getY() - p.getY()
    cy = c.getY()
    if xx == 0.0:
        print("sorry i can not do this ")
        win.close()
    else:
        print("Point 1 is : " + str(dx) + "," + str(dy))
        print("Point 2 is : " + str(cx) + "," + str(cy))
        line = Line(Point(dx,dy), Point(cx,cy))
        line.draw(win)
        slope = (str(xx) + " / " + str(yy))
        print("The slope is: ", slope)
        length = math.sqrt((xx ** 2) + (yy ** 2))
        print("The length is: ", length)
        midpointx = (dx + cx)/2
        midpointy = (dy + cy)/2
        point = Circle(Point(midpointx,midpointy), 3)
        point.setFill("cyan")
        print("The cyan point on the graph repesents the midpoint")
        point.draw(win)
        win.getMouse()
        win.close()

    
main()