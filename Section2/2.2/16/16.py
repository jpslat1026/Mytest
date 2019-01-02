import graphics
from graphics import *
import time

def drawFace():
    win = GraphWin("Face", 500, 500)
    flowerimage = Image(Point(250, 250), "loss.png")
    flowerimage.draw(win)
    win.getMouse()
    win.close

drawFace()