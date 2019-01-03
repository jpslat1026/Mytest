# 15.py
#by John Slattery on January 3, 2019
#this script will darw a face where you click
import graphics
from graphics import *
import time

def drawFace(x,y, size, win):
    win = GraphWin("Face")
    cir = Circle(Point((x -50),(y - 40)), size)
    cir.setFill("tan")
    cir.draw(win)
    ov = Oval(Point(y - 15, x- 13), Point(x - 50, y - 16))
    ov.setFill("red")
    ov.draw(win)
    eye = Circle(Point((size - 10),(size - 10)), (size - 35))
    eye.setFill("green")
    eye.draw(win)
    eye2 = Circle(Point((size + 25),(size - 10)), (size - 35))
    eye2.setFill("blue")
    eye2.draw(win)
    cir = Circle(Point((x +50),(y + 40)), size)
    cir.setFill("tan")
    cir.draw(win)
    ov = Oval(Point(y + 15, x+ 13), Point(x + 50, y + 16))
    ov.setFill("red")
    ov.draw(win)
    eye = Circle(Point((size + 100),(size + 100)), (size - 35))
    eye.setFill("green")
    eye.draw(win)
    eye2 = Circle(Point((size - 250),(size + 100)), (size - 35))
    eye2.setFill("blue")
    eye2.draw(win)
    win.getMouse()
    win.close()
drawFace(100,100, 50, "win")