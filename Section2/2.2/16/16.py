# 16.py
#by John Slattery on January 3, 2019
#this script will draw a face
from graphics import *
import math


img = Image(Point(0, 0), "loss.gif")
h = img.getHeight()
w = img.getWidth()
m1 = h/2
m2 = w/2
img = Image(Point(m2,m1), "loss.gif")
win = GraphWin('Smiley Faces', w, h)
img.draw(win)
 
def drawFace(center, size,window,h):
 
    head = Circle(center,h)
    head.setFill("green")
    head.draw(win)
 
    mouth = Circle(center, size*6.5)
    mouth.setFill("red")
    mouth.setOutline("red")
    mouth.draw(win)
    m = Circle(center, size*7)
    m.move(0,size*4)
    m.setFill("green")
    m.setOutline("green")
    m.draw(win)
 
    eye = Circle(center, size*1.5)
    eye.move(-size*4,size*3)
    eye.setFill('orange')
    eye.draw(win)
    eye = eye.clone()
    eye.draw(win)
    eye.move(size*8, 0)
 
def main(z):
 
    i = 0
    for i in range(5):
        center = win.getMouse()
        s = win.getMouse()
        xx = s.getX() - center.getX()
        yy = s.getY() - center.getY()
        g = math.sqrt((xx ** 2) + (yy ** 2))
        Face = drawFace(center,z,win, g)
    win.getMouse()
    win.close()
 
main(5)