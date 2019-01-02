# 3.py
#by John Slattery on January 1, 2019
#This script will find the first n natural numbers 
def square(n):
    num=0
    for x in range(1,n+1):
        num = num + x
    numa = num
    print("The sum of the first squared natural numbers is: ", numa)
def cube(n):
    num=0
    for x in range(1,n+1):
        num = num + (x**3)
    numb = num
    print("The sum of the first cubed natural numbers is: ", numb)

def main(number):
    square(number)
    cube(number)
main(2)