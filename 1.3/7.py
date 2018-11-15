#7.py
#by John Slattery on November 15, 2018
#This script will calculat the distance between 2 cordinates
import math
def main():
    print("This script will calculat the distance between 2 cordinates")
    x1 = eval(input("What is x1: "))
    x2 = eval(input("What is x2: "))
    y1 = eval(input("What is y1: "))
    y2 = eval(input("What is y2: "))
    total = math.sqrt((( x2 - x1 ) ** 2 ) + (( y2 - y1 ) ** 2))
    print("The distance is ", total, "u^2")

main()