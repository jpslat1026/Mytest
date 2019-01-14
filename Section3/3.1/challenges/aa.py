# 5.py
#by John Slattery on January 14, 2019
#this script will tell you if your password is strong

def main():
    g = input("What is the Phone Number: ")
    g = list(g)
    total = len(g)
    a = ""
    for i in g:
        if ord(i) >= 49 and ord(i) <= 57:
            a = a + i
    f = len(a)
    if f == 10:
        print("This is a valid phone number")
    else:
        print("This is an invalid phone number")
main()