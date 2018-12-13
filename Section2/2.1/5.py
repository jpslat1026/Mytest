# 5.py
#by John Slattery on December 13, 2018
#This will tell you your last name in numaric numbers

def main():
    name = input("Enter your last name: ")
    b = 0
    for l in name:
        a = ord(l) - 96
        b = b + a
    print(b)
main()