#8.py
#by John Slattery on November 15, 2018
#This script will calculate the epact using the year
import math
def main():
    print("This script will calculate the epact using the year")
    year = eval(input("What is the year in 4 digits(ex. 2018): "))
    C = (year // 100)
    epact = (8 + (C//4) - C + ((8*C + 13)//25) + 11 * (year%19))%30
    print("the epact is", epact)
main()