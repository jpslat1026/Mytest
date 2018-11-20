#5.py
#by John Slattery on November 19, 2018
#This script wil display a face for 5 seconds

import graphics
from graphics import *
import time

def main():
    # Graphics window
    win = GraphWin("Strait Roller")

    #shapes
    die = Rectangle(Point(2,2), Point(32,32))
    die.setFill("red")
    pointx = 33
    pointy = 0
    for i in range(5): 
        die2 = die.clone()
        die2.move(pointx,pointy)
        die2.draw(win)
        pointx = pointx + 33
        a2 = die2.getCenter()
        number = Text(a2, i + 1)
        number.draw(win)
        time.sleep(0.2)

main()