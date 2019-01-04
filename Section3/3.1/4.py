# 4.py
#by John Slattery on January 4, 2019
#this script will tell you your class
def main():
    aclass = ["freshmen", "Sophomore", "Junior", "Senior"]
    num = int(input("Homany credits do you have: "))
    if num >= 26:
        print("Your class is a", aclass[3])
    elif num >= 16 and num < 26:
        print("Your class is a", aclass[2])
    elif num >= 7 and num < 16:
        print("Your class is a", aclass[1])
    elif num < 7:
        print("Your class is a", aclass[0])
main()