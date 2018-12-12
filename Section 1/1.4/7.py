#7.py
#by John Slattery on November 19, 2018
#This script wil make a circle for a given radius

import graphics
from graphics import *
import time

def main():
    #question
    win = GraphWin("Circle", 300, 300)
    Text(Point(75, 200), " Radius: "). draw(win)
    r = Entry(Point(200, 200), 10).draw(win)
    Text(Point(100, 10), "Click to exit").draw(win)
    win.getMouse()
    r = r.getText()
    r = eval(r)
    
    #other
    win = GraphWin("cir", 500,500)
    win.setCoords(-10,-10,10,10)
    center = Point(0,0)
    cir = Circle(center, r)
    cir.setFill("yellow")
    cir.draw(win)

    
    #line
    l = Line(Point(0,0), Point(r,0))
    l.draw(win)

    #text raduis = ?
    r = str(r)
    t = Text(Point(0.020040080160320883, 0.4208416833667332), "r = " + r)
    t.draw(win)

    #close
    a = win.getMouse()
    print(a)
    win.close()
main()
