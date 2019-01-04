#6.py
#by John Slattery on November 15, 2018
#this script will calculate the slope between 2 coordinates
import math
def main():
    print("this script will calculate the slope between 2 coordinates")
    x1 = eval(input("What is x1: "))
    x2 = eval(input("What is x2: "))
    y1 = eval(input("What is y1: "))
    y2 = eval(input("What is y2: "))
    total= y2 - y1 / x2 - x1
    print("the slope is", total)
main()