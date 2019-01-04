#2.py
#by John Slattery on November 19, 2018
#This script will Display a archery target for 5 seconds

import time
import graphics
from graphics import *

def main():
    win = GraphWin("Circle")
    cir = Circle(Point(100,100), 90)
    cir.setFill("white")
    cir.draw(win)
    cir = Circle(Point(100,100), 70)
    cir.setFill("black")
    cir.draw(win)
    cir = Circle(Point(100,100), 50)
    cir.setFill("blue")
    cir.draw(win)
    cir = Circle(Point(100,100), 30)
    cir.setFill("red")
    cir.draw(win)
    cir = Circle(Point(100,100), 10)
    cir.setFill("yellow")
    cir.draw(win)
    time.sleep(5)
main()
    