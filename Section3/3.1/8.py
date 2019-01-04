#8.py
#by John Slattery on January 4, 2019
#this script will tell you if you can run for house or senet
def main():
    age = int(input("how old are you: "))
    cit = int(input("How long have you been a us citizen: "))
    if age >= 25 and cit > 7:
        print("You could be a US house representative")
    elif age > 30 and cit > 9:
        print("You could be a US house representative and a US senato")
    else:
        print("you can not be nothing")
main()