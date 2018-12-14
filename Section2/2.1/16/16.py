import graphics
from graphics import *

def main():

    filename = input("where is your file located: ")
    scores = []
    infile = open(filename, "r")
    for line in infile:
        score = line[:-1]
        scores.append(score)

    verifyscores = " ".join(scores)

    xs = []
    for i in range(11):
        x = str(i)
        x = verifyscores.count(x)
        xs.append(x)


    win = GraphWin("Histogram", 600, 400)
    win.setCoords(0, 0, 115, (len(scores) + 10))

    for i in range(11):
        bar = Rectangle(Point((5 + (10 * i)), 5), Point((10 + (10 * i)), (xs[i] + 5)))
        bar.setFill("green")
        bar.draw(win)
        label = Text(Point((7 + (10 * i)), 2), str(i))
        label.draw(win)
    #close
    infile.close()
    win.getMouse()
    win.close()


main()