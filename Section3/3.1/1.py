# 1.py
#by John Slattery on January 4, 2019
#this script will give you your wages
def main():
    hours = eval(input("How many hours do you work(ex. 10): "))
    paid = eval(input("How much do you get paid per hour(ex. 11.56): "))
    if hours > 40:
        total = (40* paid) + ((hours - 40) * (paid * 1.5))
    else:
        total = hours * paid
    print(total)
main()