import math
def main():
    print("This program is for the Fibonacci sequence")
    howfar = eval(input("How far do you wish to go?: "))
    a = 1
    b = 1
    for i in range(0, howfar -2):
        a, b=b , a+b
    print(b)
main()