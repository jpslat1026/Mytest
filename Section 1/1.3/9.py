#9.py
#by John Slattery on November 15, 2018
#This script will calculate the area fo a triangle
import math
def main():
    print("This script will calculate the area fo a triangle")
    a = eval(input("What is the length of sid a: "))
    b = eval(input("What is the length of sid b: "))
    c = eval(input("What is the length of sid c: "))
    s = (a + b + c)/2
    A = math.sqrt(s * ( s - a ) * ( s -b) * ( s - c))
    print(A)
main()