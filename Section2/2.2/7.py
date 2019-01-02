#7.py
#by John Slattery on November 15, 2018
# This script shows the Fibonacci sequence

def math(howfar, a, b):
    for i in range(0, howfar -2):
        a, b=b , a+b
    return b
def main(far):
    x = 1
    y = 1
    v = math(far, x, y)
    print("the last number for the fibinatuci sequence of ",far, v)
main(10)