# 15.py
#by John Slattery on December 13, 2018
#This will tell you your grade

import graphics
from graphics import *

def main():
    grade = eval(input("How many points did computerwell get 0-100: "))
    grade2 = eval(input("How many points did Dibblebit get 0-100: "))
    grade3 = eval(input("How many points did jones get 0-100: "))
    grade4 = eval(input("How many points did smith get 0-100: "))

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -2, 11.5, 100)
    Text(Point(1, -0.5), 'Computerwell').draw(win)


    bar = Rectangle(Point(1, 0), Point(2, grade))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    bar = Rectangle(Point(3, 0), Point(4, grade2))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    bar = Rectangle(Point(4, 0), Point(5, grade3))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    bar = Rectangle(Point(5, 0), Point(6, grade4))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    win.getMouse()
    win.close()

main()