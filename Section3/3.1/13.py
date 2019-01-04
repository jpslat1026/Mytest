#13.py
#by John Slattery on January 4, 2019
#this script will tell you
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
    dayNum = 31*(month - 1) + day
    if month > 2:
        dayNum = dayNum - (4*(month) + 23) // 10
    if leap == 1:
        dayNum = dayNum + 1
    print("The day number", dayNum)
main()