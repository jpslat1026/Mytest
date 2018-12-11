#14.py
#by John Slattery on November 15, 2018
# This script will approximate the value of pi
import math
def main():
    print("This script will approximate the value of pi")
    n = eval(input("Enter the numbers of terms to be summed: "))
    apr = 0
    for i in range(n):
        apr = apr + 4.0 * (-1) ** i / (2 * i + 1)
    accuracy = (math.pi * n) - apr
    print("pi is the approxamation with", n, "terms is", apr)
    print("The accuracy is", accuracy, "%.")
main()