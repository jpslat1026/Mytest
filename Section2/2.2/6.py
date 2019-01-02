# 6.py
#by John Slattery on January 1, 2019
#This script will calculate the area fo a triangle
import math
def main(a,b,c):
    print("This script will calculate the area fo a triangle")
    s = (a + b + c)/2
    A = math.sqrt(s * ( s - a ) * ( s -b) * ( s - c))
    print(A)
main(2,3,4)