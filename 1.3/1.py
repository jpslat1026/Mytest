#1.py
#by John Slattery on November 15, 2018
#this script will calculate a the area and volume of a circule using the radius
import math
def main() :
    print("this script will calculate a the area and volume of a circule using the radius")
    r = eval(input("What is the Radius of your circule: "))
    v = 4 / 3 * math.pi * r ** 3
    a = 4 * math.pi * r ** 2

    print("The Area of your circule is ", a)
    print("The Volume of your Circule is ", v)
main()