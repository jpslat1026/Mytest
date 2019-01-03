# 17.py
#by John Slattery on January 3, 2019
#this will move a shape to where you click
from graphics import *

win = GraphWin("cir", 500,500)
 
def moveTo(shape,point):
    c = shape.getCenter()
    point = win.getMouse()
    dx = point.getX() - c.getX()
    dy = point.getY() - c.getY()
    shape.move(dx,dy)
 
def main():
    newCenter = win.getMouse()
    cir = Circle(newCenter, 30)
    cir.setFill("pink")
    cir.draw(win)
    for i in range(9):
         moveTo(cir,newCenter)
    win.getMouse()
    win.close()
 
main()