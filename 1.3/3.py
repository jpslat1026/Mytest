#2.py
#by John Slattery on November 15, 2018
#This script finds the weight of atoms
import math
def main():
    print("This script will help you calculate the weight of atoms ")
    H = 1.00794
    C = 12.0107
    O = 15.9994
    h = eval(input("How many Hydrogen atoms: "))
    c = eval(input("How many carbon atoms: "))
    o = eval(input("How many Oxygen atoms: "))
    output = (H * h) + ( C *c ) + (O * o )
    print("The weight is", output, "grams/mole")
main()