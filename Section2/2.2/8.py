# 8.py
#by John Slattery on January 1, 2019
#This script will show you how close you are to guessing a square root

import math
def nextGuess(guess, x):
    print("This Script calculates square root using Newton's method")
    awnser = ( guess + (x / guess ) ) / 2 
    close = math.sqrt(x) - awnser
    print("Square root of ", x,"is", awnser)
    print("it is", close, "% close")
nextGuess(3,6)