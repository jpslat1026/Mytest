# 11.py
#by John Slattery on December 13, 2018
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    print("Index", "\t","\t", x,"\t","\t","\t",y)
    print("------------------------------------------------")
    a = 1
    for i in range(10) :
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(a, "\t ", x, "\t ", y)
        a = a + 1
main()