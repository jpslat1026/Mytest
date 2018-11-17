#12.py
#by John Slattery on November 15, 2018
# asd
import math
def main():
    n = eval(input("what is the number that you would like to find the sum cubed of: "))
    t = 0
    a = 1
    for i in range(n):
        t = t + a ** 3
        a = a + 1
    print("your awnser is", t)
main()