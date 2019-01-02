# 5.py
#by John Slattery on January 1, 2019
#This script will find the cost for a square inch of yor pizzia
import math
def matha(r, c):
    a = math.pi * r ** 2
    print(a)
    p = c / a
    return a, p
def main(radius,cost):
    print("this script calculate the cost per square in of your pizzia")
    matha(radius,cost)
    print("the area of the pizzia is: ", radius)
    print("the cost per square inch is: ", cost)
main(2,7)