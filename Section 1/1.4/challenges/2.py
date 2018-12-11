#2.py
#by John Slattery on December 11, 2018
#This Script will make a 12inc ruler

import graphics

from graphics import *

def main():

    #Graphics Window
    win = GraphWin("This will make graph paper", 1153,500)
    win.setCoords(1153,10,0,0)

    #base
    rulebase = Rectangle(Point(0,2), Point(1153,8))
    rulebase.setFill("red")
    rulebase.draw(win)

    #inches
    x = 1
    for i in range(12):
        lineinch = Line(Point(x,2), Point(x,4))
        lineinch.draw(win)
        x = x+97
    n= 0
    q=12
    for i in range(12):
        words = Text(Point(n,4.5), q)
        words.draw(win)
        n = n+97
        q = q-1
    #1/4 inches
    x = 1
    for i in range(48):
        lineinch = Line(Point(x,2), Point(x,3.5))
        lineinch.draw(win)
        x = x+24

    #close
    win.getMouse()
    win.close()
main()