#11.py
#by John Slattery on January 4, 2019
#this script will tell you
def main():
    year = int(input("what year would yould you like to check if it is a leap year(ex. 2019): "))
    yeara = year % 4
    centry = year % 400
    if centry == 0:
        if yeara == 0:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
    
main()