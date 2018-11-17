#5.py
#by John Slattery on November 15, 2018
#This script will calculat how much you will pay for Konditorei coffee
import math
def main():
    print("This script will calculat how much you will pay for Konditorei coffee")
    lbs = eval(input("How Many pounds do you want: "))
    total = (lbs * 0.86) + 1.50
    print("It cost", total, "dollars for", lbs, "pounds")
main()