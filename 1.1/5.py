# File: 5.py
# Created 11/13/18 by John Slattery Jr.
# A simple program illustrating chaotic behavior.

# Defining the function
def main():
    #puting variable n and printing how many lins sholud it print
    n = eval(input("how many numbers should i print? "))
    #printing a line
    print("This program illustrates a chaotic function")
    #setting a varaible to the in put 0-1 and making a number
    x = eval(input("Enter a number between 0 and 1: "))
    #setting a loop
    for i in range(n) :
        #dose math
        x = 2.0 * x * (1 - x)
        # prints X
        print(x)
main()
