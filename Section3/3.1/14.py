#14.py
#by John Slattery on January 19, 2019
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

    

    #Y intercept
    x = math.sqrt(abs(((r ** 2) - (yint **2))))
    dd = Circle(Point(x,yint), 0.5)
    dd.setFill("red")
    cir = Circle(Point(-x,yint), 0.5)
    cir.setFill("red")
    x = math.floor(x)
    w = str(x)
    #text raduis = ?
    t = Text(Point(0.020040080160320883, 0.4208416833667332), "The X intercept is " + w + " and -" + w)

     #line
    if x > r:
        t = Text(Point(0.020040080160320883, 0.4208416833667332), "error sorry i can not do this")
        t.draw(win)
        win.getMouse()
        win.close()
    else:
        t.draw(win)
        cir.draw(win)
        dd.draw(win)    
        l = Line(Point(-10,yint), Point(10,yint))
        l.draw(win)
        win.getMouse()
        win.close()
main()
