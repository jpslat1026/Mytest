# 2.py
#by John Slattery on January 14, 2019
#this script will tell you if 2 or more are correct

def main():
    a,b,c = eval(input("What are the three results(ex. 1,2,1): "))
    putin = [a,b,c]
    if putin[0] == putin[1]:
        print(putin[0])
    elif putin[1] == putin[2]:
        print(putin[1])
    elif putin[0] == putin[2]:
        print(putin[0])
    else:
        print("ERROR")
main()