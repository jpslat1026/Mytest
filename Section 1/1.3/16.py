#16.py
#by John Slattery on November 15, 2018
# This script shows the Fibonacci sequence
import math
def main():
    print("This script shows the Fibonacci sequence")
    howfar = eval(input("how far do you want to go?: "))
    a = 1
    b = 1
    for i in range(0, howfar -2):
        a, b=b , a+b
    print(b)
main()