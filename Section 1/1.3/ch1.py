#1ch.py
#by John Slattery on November 15, 2018
# This script will find x and put it to the power of y
import math
def main():
    print("this is a script that will calculate  to the power of y")
    x = eval(input("What is the number to put the power of y on: "))
    y = eval(input("What is the number to power x: "))
    power = math.pow(x, y)
    print(x, "to the power of", y, "is", power)
main()