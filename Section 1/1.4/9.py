#9.py
#by John Slattery on December 10, 2018
#This Script displays information about a rectangle drawn by the user

import graphics
from graphics import *
import time
import math

def main():
    win = GraphWin("Rectangle Satatics")
    win.setCoords(-10,-20,20,20)
    p = win.getMouse()
    c = win.getMouse()
    lengthr = c.getX() - p.getX()
    widthr = c.getY() - p.getY()
    length = abs(round(lengthr))
    width = abs(round(widthr))
    rectangle = Rectangle(Point(p.getX(),p.getY()), Point(c.getX(),c.getY()))
    rectangle.draw(win)
    area = length*width
    print("Your Area is: ", area)
    permiter = 2*(length + width)
    print("Your Permiter is: ", permiter)
    win.getMouse()
    win.close()
main()
