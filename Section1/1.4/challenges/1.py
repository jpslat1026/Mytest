#1.py
#by John Slattery on December 11, 2018
#This Script will make a cordnit plane

import graphics

from graphics import *

def main():

    #Graphics Window
    win = GraphWin("This will make graph paper", 1000,1000)
    win.setCoords(0,0, 20,20)

    #x axis lines
    x1 = 0.5
    y1 = 0
    x2 = 0.5
    y2 = 20
    for i in range (39):
        xlines = Line(Point(x1,y1), Point(x2,y2))
        xlines.draw(win)
        x1 = x1+0.5
        x2 = x2+0.5
    #y axis lines
    x1 = 0
    y1 = 0.5
    x2 = 20
    y2 = 0.5
    for i in range (39):
        xlines = Line(Point(x1,y1), Point(x2,y2))
        xlines.draw(win)
        y1 = y1+0.5
        y2 = y2+0.5

    #x axis tics
    x1 = 0.5
    y1 = 9.5
    x2 = 0.5
    y2 = 10.5
    for i in range (39):
        xlines = Line(Point(x1,y1), Point(x2,y2))
        xlines.setFill("black")
        xlines.setWidth(2)
        xlines.draw(win)
        x1 = x1+1
        x2 = x2+1
    z = -10
    a = 0.5
    for i in range(10):
        nums = Text(Point(a,11), z)
        nums.draw(win)
        z = z+1
        a = a + 1
    a = 10.5
    z = 1
    for i in range(10):
        nums = Text(Point(a,11), z)
        nums.draw(win)
        z = z+1
        a = a + 1
    
    #y axis tics
    x1 = 9.5
    y1 = 1
    x2 = 10.5
    y2 = 1
    for i in range (39):
        ylines = Line(Point(x1,y1), Point(x2,y2))
        ylines.setFill("black")
        ylines.setWidth(2)
        ylines.draw(win)
        y1 = y1+1
        y2 = y2+1
    z = -10
    a = 0.5
    for i in range(10):
        nums = Text(Point(11,a), z)
        nums.draw(win)
        z = z+1
        a = a + 1
    a = 10.5
    z = 1
    for i in range(10):
        nums = Text(Point(11,a), z)
        nums.draw(win)
        z = z+1
        a = a + 1


    #y axis
    y = Line(Point(10, 0), Point(10, 20))
    y.setFill("red")
    y.setWidth(2)
    y.draw(win)

    #x axis
    x = Line(Point(0, 10), Point(20, 10))
    x.setWidth(2)
    x.setFill("red")
    x.draw(win)

    #close
    win.getMouse()
    win.close()
main()