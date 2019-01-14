# 4.py
#by John Slattery on January 14, 2019
#this script will tell you if your password is strong

def main():
    g = input("What is the password: ")
    total = len(g)
    if total >= 8 and total <= 12:
        print("Your password is Verry Strong")
    elif total < 8:
        print("Your password is Weak")
    elif total > 12:
        print("Your password is moderately strong")
main()