#5.py
#by John Slattery on January 4, 2019
#this script will tell you your bmis
def main():
    lbs = int(input("How many pounds do you weigh: "))
    inches = int(input("How tall are you in inches: "))
    bmi = (lbs * 720) / (inches ** 2)
    if bmi > 19 and bmi < 26:
        print("You are at healthy weight and your bmi is", bmi)
    elif bmi > 26:
        print("You are above the healthy weight and your bmi is", bmi)
    elif bmi < 19:
        print("You are below the healthy weight and your bmi is", bmi)
main()

