#10.py
#by John Slattery on November 15, 2018
# This script will calculate the length you need for the ladder
import math
def main():
    print("This script will calculate the length you need for the ladder")
    h = eval(input("What is the height of the house: "))
    a = eval(input("What is the angle of the ladder: "))
    radians = (math.pi / 180) * a
    length = h / (math.sin(radians))
    print(length)
main()