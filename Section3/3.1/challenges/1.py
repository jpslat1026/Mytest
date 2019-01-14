# 1.py
#by John Slattery on January 14, 2019
#this script will tell you your credit card brand

def main():
    cardnum = input("What is Your Credit Card Number(ex. 4 8 3 4 8 9 2 3 7 4 8 7 4): ")
    cardnum = cardnum.split(" ")
    if cardnum[0] == "4":
        cardtype = "Visa"
    elif cardnum[0] == "5":
        cardtype = "MasterCard"
    elif cardnum[0] == "6":
        cardtype = "Discover"
    else:
        cardtype = "Unknown"
    print("Your credit card type is: ", cardtype)
main()