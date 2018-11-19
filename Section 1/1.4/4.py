#2.py
#by John Slattery on November 19, 2018
#This script wil display a face for 5 seconds

import graphics
from graphics import *
import time

def main():
    win = GraphWin("Winter :(")
    tri = Polygon(Point(70,150), Point(100,100), Point(130,150))
    tri.setFill("green")
    tri.draw(win)
    tri2 = Polygon(Point(80,110), Point(100,60), Point(120,110))
    tri2.setFill("green")
    tri2.draw(win)
    trunk = Rectangle(Point(90,150), Point(110,165))
    trunk.setFill("brown")
    trunk.draw(win)
    ortment = Circle(Point(90,100), 5)
    ortment.setFill("red")
    ortment.draw(win)
    time.sleep(0.2)
    ortment = Circle(Point(110,100), 5)
    ortment.setFill("purple")
    ortment.draw(win)
    time.sleep(0.2)
    ortment = Circle(Point(100,85), 5)
    ortment.setFill("yellow")
    ortment.draw(win)
    time.sleep(0.2)
    ortment = Circle(Point(115,140), 5)
    ortment.setFill("pink")
    ortment.draw(win)
    time.sleep(0.2)
    ortment = Circle(Point(100,140), 5)
    ortment.setFill("blue")
    ortment.draw(win)
    time.sleep(0.2)
    ortment = Circle(Point(85,140), 5)
    ortment.setFill("orange")
    ortment.draw(win)
    time.sleep(0.2)
    ortment = Circle(Point(100,120), 5)
    ortment.setFill("gray")
    ortment.draw(win)
    snowbut = Circle(Point(30,150), 30)
    snowbut.setFill("white")
    snowbut.draw(win)
    snowhead = Circle(Point(30,100), 25)
    snowhead.setFill("white")
    snowhead.draw(win)
    eye = Circle(Point(20,90), 5)
    eye.setFill("pink")
    eye.draw(win)
    eye1 = Circle(Point(40,90), 5)
    eye1.setFill("pink")
    eye1.draw(win)
    noes = Polygon(Point(23,102), Point(35,103), Point(30,109))
    noes.setFill("Orange")
    noes.draw(win)
    for i in range(4):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())
    time.sleep(7)
main()