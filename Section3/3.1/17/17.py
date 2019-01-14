# 17.py
#by John Slattery on January 4, 2019
#will do the windows xp screen saver
from graphics import *
import time
import random
win = GraphWin('windows xp', 900, 900)
win.setCoords(0,0,290, 290)
win.setBackground("black")
def bouncing(ball, dx, dy):
    for i in range(10000):
        ball.move(dx, dy)
        center = ball.getAnchor()
        x = center.getX()
        y = center.getY()
        if x < 10:
            dx = -dx
        elif x > 280:
            dx = -dx
        if y < 10:
            dy = -dy
        elif y > 280:
            dy = -dy
        update(30)

def getRandomPoint():
    x = random.randrange(10, 281)
    y = random.randrange(10, 281)
    return Point(x, y)   

def circles(center):
    x = Image(center, "xp.gif")
    #x = Rectangle(center, centerr)
    x.draw(win)
    return x

def main(dx, dy):
    
    center = getRandomPoint()
    x = Image(center, "xp.gif")
    x.draw(win)
    bouncing(x, dx, dy)    

    win.close()
    
main(2,2)
