#2.py
#by John Slattery on November 19, 2018
#This script wil display a face for 5 seconds

import graphics
from graphics import *
import time

def main():
    win = GraphWin("Face")
    cir = Circle(Point(100,100), 90)
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
main()