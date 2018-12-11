#3.py
#by John Slattery on December 11, 2018
#This Script will make a cherckers board
import graphics

from graphics import *

def main():

    #Graphics Window
    win = GraphWin("This will make graph paper", 500,500)
    win.setCoords(8,8,0,0)

    #red
    a = Rectangle(Point(0,0),Point(1,1))
    a.setFill("black")
    a.draw(win)
    x = 1
    y = 2
    for i in range(4):
        a = Rectangle(Point(x,1),Point(y,0))
        a.setFill("red")
        a.draw(win)
        x = x + 2
        y = y + 2
    x=2
    y=3
    for i in range(3):
        a = Rectangle(Point(x,0),Point(y,1))
        a.setFill("black")
        a.draw(win)
        x=x+2
        y=y+2

        #sssssss
    a = Rectangle(Point(0,1),Point(1,2))
    a.setFill("red")
    a.draw(win)
    x = 1
    y = 2
    for i in range(4):
        a = Rectangle(Point(x,2),Point(y,1))
        a.setFill("black")
        a.draw(win)
        x = x + 2
        y = y + 2
    x=2
    y=3
    for i in range(3):
        a = Rectangle(Point(x,1),Point(y,2))
        a.setFill("red")
        a.draw(win)
        x=x+2
        y=y+2

    #sssssssss
    a = Rectangle(Point(0,2),Point(1,3))
    a.setFill("black")
    a.draw(win)
    x = 1
    y = 2
    for i in range(4):
        a = Rectangle(Point(x,3),Point(y,2))
        a.setFill("red")
        a.draw(win)
        x = x + 2
        y = y + 2
    x=2
    y=3
    for i in range(3):
        a = Rectangle(Point(x,2),Point(y,3))
        a.setFill("black")
        a.draw(win)
        x=x+2
        y=y+2
    #fsff
    a = Rectangle(Point(0,3),Point(1,4))
    a.setFill("red")
    a.draw(win)
    x = 1
    y = 2
    for i in range(4):
        a = Rectangle(Point(x,4),Point(y,3))
        a.setFill("black")
        a.draw(win)
        x = x + 2
        y = y + 2
    x=2
    y=3
    for i in range(3):
        a = Rectangle(Point(x,3),Point(y,4))
        a.setFill("red")
        a.draw(win)
        x=x+2
        y=y+2
    #dfdfsd
    a = Rectangle(Point(0,4),Point(1,5))
    a.setFill("black")
    a.draw(win)
    x = 1
    y = 2
    for i in range(4):
        a = Rectangle(Point(x,5),Point(y,4))
        a.setFill("red")
        a.draw(win)
        x = x + 2
        y = y + 2
    x=2
    y=3
    for i in range(3):
        a = Rectangle(Point(x,4),Point(y,5))
        a.setFill("black")
        a.draw(win)
        x=x+2
        y=y+2
    

    #close
    win.getMouse()
    win.close()
main()