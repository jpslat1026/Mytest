#11.py
#by John Slattery on November 15, 2018
# This script will get the sum of a whole number
import math
def main():
    n = eval(input("what is the number that you would like to find the sum of: "))
    t = 0
    a = 1
    for i in range(n):
        t = t + a
        a = a + 1
    print("your awnser is", t )
main()