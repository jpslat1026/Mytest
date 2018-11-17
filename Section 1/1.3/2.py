#2.py
#by John Slattery on November 15, 2018
#this script calculate the cost per square in of your pizzia
import math

def main():
    print("this script calculate the cost per square in of your pizzia")
    r = eval(input("What is The Radius of your pizzia: "))
    c = eval(input("how much was yor pizzia: "))
    a = math.pi * r ** 2
    print("the area of the pizzia is: ", a)
    p = c / a
    print("the cost per square inch is: ", p)
main()