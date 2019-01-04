#1.py
#by John Slattery on November 19, 2018
#this script will print a box in a graphic window an when you click the box will follow
import graphics
from graphics import *

def main():
    win = GraphWin("cir")
    shape = Rectangle(Point(50,50), Point(60,60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        add = shape.clone()
        add.move(dx, dy)
        add.draw(win)

    s = Text(Point(100,100), "Click again to quit")
    s.draw(win)
    win.getMouse()
    win.close()
main()
