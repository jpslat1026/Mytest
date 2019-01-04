#12.py
#by John Slattery on January 4, 2019
#this script will tell you if a date is valid or invald
def main():
    date = input("what is the date you would like to check(ex. 10/12/2019): ")
    date = date.split("/")
    day = int(date[1])
    month = int(date[0])
    year = int(date[2])
    yeara = year % 4
    centry = year % 400
    if centry == 0:
        if yeara == 0:
            leap = 1
    else:
        leap = 0
    if month == 1:
        if day <= 31:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 2:
        if leap == 0:
            if day <= 28:
                print("your date is valid")
            else:
                print("your date is invalid")
        else:
            if day <= 29:
                print("your date is valid")
            else:
                print("your date is invalid")
    elif month == 3:
        if day <= 31:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 4:
        if day <= 30:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 5:
        if day <= 31:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 6:
        if day <= 30:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 7:
        if day <= 31:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 8:
        if day <= 31:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 9:
        if day <= 30:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 10:
        if day <= 31:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 11:
        if day <= 30:
            print("your date is valid")
        else:
            print("your date is invalid")
    elif month == 12:
        if day <= 31:
            print("your date is valid")
        else:
            print("your date is invalid")
    else:
        print("your date is invalid")

    
main()