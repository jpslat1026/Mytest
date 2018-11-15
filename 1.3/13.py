#13.py
#by John Slattery on November 15, 2018
# This is a script that will add numbers
import math
def main():
    n = eval(input("How many numbers would you like to add: "))
    v = 0
    for i in range(n):
        x = eval(input("a number: "))
        v = x + v
    print("your awnser is", v)
main()