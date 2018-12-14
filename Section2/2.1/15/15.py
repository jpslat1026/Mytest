# 15.py
#by John Slattery on December 13, 2018
#This will tell you your grade

import graphics
from graphics import *

def main():
    filea = input("where is the file you would like to decode? ")
    files = open(filea, "r")
    filesa = files.read()
    files = filesa.split(", ")
    l = filesa.splitlines()
    na = l[0].split(", ")
    gr = l[1].split(", ")

    grade = eval(gr[0])
    grade2 = eval(gr[1])
    grade3 = eval(gr[2])
    grade4 = eval(gr[3])

    name = na[0]
    name1 = na[1]
    name2 = na[2]
    name3 = na[3]

    win = GraphWin("Investment Growth Chart", 500, 500)
    win.setBackground("white")
    win.setCoords(0,0,155,95)


    Text(Point(25,26), name).draw(win)
    bar = Rectangle(Point(50, 20), Point(grade + 50, 30))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    Text(Point(25,46), name1).draw(win)
    bar = Rectangle(Point(50, 40), Point(grade2 + 50,50))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    Text(Point(25,66), name2).draw(win)
    bar = Rectangle(Point(50,60), Point(grade3 + 50,70))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    Text(Point(25,86), name3).draw(win)
    bar = Rectangle(Point(50,80), Point(grade4 + 50,90))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    win.getMouse()
    win.close()

main()