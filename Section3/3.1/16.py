#16.py
#by John Slattery on Janury 14, 2019
#This script will Display a archery target and leet you shoot at it and score plus it will tell you how many points you scored

import graphics
from graphics import *
import math

win = GraphWin("Circle",900,900)
win.setCoords(-50,-50,50,50)
globalcenter = Point(0,0)

def color(x):
    if x < 10:
        x = 9
    elif x < 20:
        x = 7
    elif x < 30:
        x = 5
    elif x < 40:
        x = 3
    elif x < 50:
        x = 1
    else:
        x = 0
    return x
def points():
    x = win.getMouse()
    cir = Circle(x,3)
    cir.setFill("green")
    cir.draw(win)
    center = cir.getCenter()
    centerX = center.getX()
    centerY = center.getY()
    distance = math.sqrt((0 - centerX)**2 + (0 - centerY)**2)
    return distance

def main():
    cir = Circle(Point(0,0), 50)
    cir.setFill("white")
    cir.draw(win)
    cornerPoint = cir.getP1()
    cornerPointa = cir.getP2()
    cir = Circle(Point(0,0), 40)
    cir.setFill("black")
    cir.draw(win)
    cornerPoint = cir.getP1()
    cornerPointa = cir.getP2()
    cir = Circle(Point(0,0), 30)
    cir.setFill("blue")
    cir.draw(win)
    cornerPoint = cir.getP1()
    cornerPointa = cir.getP2()
    cir = Circle(Point(0,0), 20)
    cir.setFill("red")
    cir.draw(win)
    cornerPoint = cir.getP1()
    cornerPointa = cir.getP2()
    cir = Circle(Point(0,0), 10)
    cir.setFill("yellow")
    cir.draw(win)
    cornerPoint = cir.getP1()
    cornerPointa = cir.getP2()
    a = points()
    a = color(a)
    b = points()
    b = color(b)
    c = points()
    c = color(c)
    d = points()
    d = color(d)
    e = points()
    e = color(e)
    sums = a + b + c + d + e
    print("Your Score is", sums, "Points")
    win.getMouse()
    win.close()
main()
    