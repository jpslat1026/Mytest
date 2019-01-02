import graphics
from graphics import *
import time

def drawFace(x,y, size, win):
    win = GraphWin("Face")
    cir = Circle(Point(x,y), size)
    cir.setFill("tan")
    cir.draw(win)
    ov = Oval(Point(150, 130), Point(50, 160))
    ov.setFill("red")
    ov.draw(win)
    eye = Circle(Point(65,60), 10)
    eye.setFill("green")
    eye.draw(win)
    eye2 = Circle(Point(130,60), 10)
    eye2.setFill("blue")
    eye2.draw(win)
    time.sleep(5)
drawFace(100,100, 90, "win")