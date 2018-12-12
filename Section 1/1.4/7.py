#7.py
#by John Slattery on November 19, 2018
#This script wil make a circle for a given radius

import math
import graphics
from graphics import *
import time

def main():
    #question
    win = GraphWin("Circle", 300, 300)
    Text(Point(75, 200), " Radius: "). draw(win)
    r = Entry(Point(200, 200), 10).draw(win)
    Text(Point(75, 100), " Y intercept: "). draw(win)
    yint = Entry(Point(200,100), 10).draw(win)
    Text(Point(100, 10), "Click to exit").draw(win)
    win.getMouse()
    r = r.getText()
    r = eval(r)
    yint = yint.getText()
    yint = eval(yint)
    
    #other
    win = GraphWin("cir", 500,500)
    win.setCoords(-10,-10,10,10)
    center = Point(0,0)
    cir = Circle(center, r)
    cir.setFill("yellow")
    cir.draw(win)

    
    #line
    l = Line(Point(-10,yint), Point(10,yint))

    l.draw(win)

    

    #Y intercept
    x = math.sqrt(abs(((r ** 2) - (yint **2))))
    print(x)
    cir = Circle(Point(x,yint), 0.5)
    cir.setFill("red")
    cir.draw(win)
    cir = Circle(Point(-x,yint), 0.5)
    cir.setFill("red")
    cir.draw(win)
    x = str(x)
    #text raduis = ?
    t = Text(Point(0.020040080160320883, 0.4208416833667332), "The X intercept is " + x + " and -" + x)
    t.draw(win)

    #close
    win.getMouse()
    win.close()
main()
