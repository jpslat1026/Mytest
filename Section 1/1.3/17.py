import math
def main():
    print("This Script calculates square root using Newton's method")
    x = eval(input("what do you want to find the square root of?: "))
    guess = eval(input("What do you think it is?: "))
    awnser = ( guess + (x / guess ) ) / 2 
    close = math.sqrt(x) - awnser
    print("Square root of ", x,"is", awnser)
    print("it is", close, "%  close")
main()