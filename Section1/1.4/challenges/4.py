#4.py
#by John Slattery on December 12, 2018
#This Script will make a ruler wit milameters and centmeterson it

import graphics

from graphics import *

def main():

    #Graphics Window
    win = GraphWin("This will make a ruler", 1153,500)
    win.setCoords(1153,10,0,0)

    #base
    rulebase = Rectangle(Point(0,2), Point(1153,8))
    rulebase.setFill("red")
    rulebase.draw(win)

    #inches
    x = 0
    for i in range(12):
        lineinch = Line(Point(x,2), Point(x,4))
        lineinch.draw(win)
        x = x+96
    n= 0
    q=12
    for i in range(12):
        words = Text(Point(n,4.5), q)
        words.draw(win)
        n = n+97
        q = q-1
    #1/4 inches
    x = 0
    for i in range(48):
        lineinch = Line(Point(x,2), Point(x,3.5))
        lineinch.draw(win)
        x = x+24
    #centimeters
    x = 0
    for i in range(300):
        lineinch = Line(Point(x,8), Point(x,7))
        lineinch.draw(win)
        x = x+4
    #cenimeters
    x = 0
    for i in range(300):
        lineinch = Line(Point(x,8), Point(x,6))
        lineinch.draw(win)
        x = x+36

    #close
    win.getMouse()
    win.close()
main()