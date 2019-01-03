# 3.py
#by John Slattery on January 3, 2019
#this script will tell you the discount of an item
import math
from math import *
def main():
    v = eval(input("What is the precent in decimal(ex. 0.24 = 24%): "))
    m = eval(input("how much in dollars (ex. 30.50 = $30 ¢50): "))
    discount = v * m
    final = m - discount
    final = str(final)
    print("You pay: $" + final)
main()