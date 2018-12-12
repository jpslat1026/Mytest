#5.py
#by John Slattery on December 12, 2018
#This Script will make a flag

import graphics

from graphics import *

def main():
    #Graphics Window
    win = GraphWin("Ireland Flag", 700,500)
    win.setCoords(0,0,3,3)

    #green
    rec = Rectangle(Point(0,0), Point(1,3))
    rec.setFill("green")
    rec.draw(win)

    #white
    rec = Rectangle(Point(1,3), Point(2,0))
    rec.setFill("white")
    rec.draw(win)

    #orange
    rec = Rectangle(Point(2,0), Point(3,3))
    rec.setFill("orange")
    rec.draw(win)

    #close
    win.getMouse()
    win.close()
main()