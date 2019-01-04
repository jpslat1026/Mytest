#9.py
#by John Slattery on January 4, 2019
#this script will tell you easter's date
def main():
    loop = 0
    while loop == 0:
        year = int(input("what year: "))
        if year >= 1900 and year <= 2099:
            a = year % 19 
            b = year % 4
            c = year % 7
            d = (19*a + 24) % 30
            e = (2*b + 4*c + 6*d + 5) % 7
            easter = d + e
            if easter > 10:
                easter = easter - 9
            else:
                easter = easter + 22
            loop = 2
            if year == 1954:
                print("Easter is April ", easter - 7, "in", year)
            elif year == 1981:
                print("Easter is April ", easter - 7, "in", year)
            elif year == 2049:
                print("Easter is April ", easter - 7, "in", year)
            elif year == 2076:
                print("Easter is April ", easter - 7, "in", year)
            else:
                print("Easter is April ", easter, "in", year)
            
            loop = 2
        else:
            print("Your year is invalid try again")
main()
'''if year == 1954:
                print("Easter is April ", easter - 7, "in", year)
            elif year == 1981:
                print("Easter is April ", easter - 7, "in", year)
            elif year == 2049:
                print("Easter is April ", easter - 7, "in", year)
            elif year == 2076:
                print("Easter is April ", easter - 7, "in", year)
            else:
                print("Easter is April ", easter, "in", year)'''