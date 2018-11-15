#4.py
#by John Slattery on November 15, 2018
import math
def main():
    print("This script determines the distance to a lightning strike based on time elapsed")
    t = eval(input("How many seconds did it take to hear the thunder after the lighting: "))
    df = t * 1100
    dm = df / 5280
    print("The storm is", df, "feet or", dm, "miles away")
main()