# 6.py
#by John Slattery on November 19, 2018
# updated the future value program to be graphical
import graphics
from graphics import *
import time

def main():
    win = GraphWin("Future value calculator", 300, 300)
    Text(Point(75, 200), " Enter principal: "). draw(win)
    Text(Point (75, 150), "Enter interest rate: ").draw(win)
    p = Entry(Point(200, 200), 10).draw(win)
    a = Entry(Point(200, 150), 10).draw(win)
    Text(Point(100, 10), "Click to exit").draw(win)
    win.getMouse()
    principal = p.getText()
    principal = eval(principal)
    apr = a.getText()
    apr = eval(apr)
    win.close()

    win = GraphWin("Grades", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), '0.0K').draw(win)
    Text(Point(-1, 2500), '2.5K').draw(win)
    Text(Point(-1, 5000), '5.0K').draw(win)
    Text(Point(-1, 7500), '7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1 , 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    
    win.getMouse()
    win.close()

main()