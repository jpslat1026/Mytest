#5.py
#by John Slattery on November 19, 2018
#This script wil display a face for 5 seconds

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
    win.close()

    #other
    win = GraphWin("cir")
    win.setCoords(-10,-10,10,10)
    center = Point(0,0)
    cir = Circle(center, r)
    cir.setFill("yellow")
    cir.draw(win)
    win.getMouse()
main()
