#11.py
#by John Slattery on December 11, 2018
#This Script will make a house using user input

import graphics
from graphics import *

def main():
    win = GraphWin("house maker", 500, 500)
    win.setCoords(0,0, 10,10)
    
    #Rectangle
    words = Text(Point(5, 0.5), "Click on the bottom left to make the first point of the rectangle")
    words.setTextColor("green")
    words.draw(win)
    p1 = win.getMouse()
    x=p1.getX()
    y=p1.getY()
    words.undraw()
    words = Text(Point(5, 0.5), "Click on the top right to make the second point of the rectangle")
    words.setTextColor("green")
    words.draw(win)
    p2 = win.getMouse()
    x=p2.getX()
    y=p2.getY()
    rectangle = Rectangle(p1, p2)
    rectangle.setFill("tan")
    rectangle.draw(win)
    words.undraw()
    
    #Door
    words = Text(Point(5,0.5), "To make the Door click some where inside your house frame")
    words.setTextColor("green")
    words.draw(win)
    p4 = win.getMouse()
    x=p4.getX()
    y=p4.getY()
    p8=Point(p4.getX()+1.1,p1.getY())
    door = Rectangle(p4,p8)
    door.setFill("brown")
    door.draw(win)
    words.undraw()
    
    #window
    words = Text(Point(5,0.5), "To make the Window click some where inside your house frame")
    words.setTextColor("green")
    words.draw(win)
    p5 = win.getMouse()
    x=p5.getX()
    y=p5.getY()
    p9=Point(p5.getX()+0.4,p5.getY()-0.4)
    window = Rectangle(p5,p9)
    window.setFill("white")
    window.draw(win)
    words.undraw()
    
    #triangle
    words = Text(Point(5,0.5), "To make the Roof click some where outside your house frame")
    words.setTextColor("green")
    words.draw(win)
    p3 = win.getMouse()
    x=p3.getX()
    y=p3.getY()
    p7=Point(p2.getX(),p2.getY())
    p12=Point(p1.getX(),p2.getY())
    tri = Polygon(p12, p7, p3)
    tri.setFill("red")
    tri.draw(win)
    words.undraw()
    words = Text(Point(5,0.5), "Click again to close")
    words.setTextColor("green")
    words.draw(win)
    win.getMouse()
    win.close()
main()