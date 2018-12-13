# 7.py
#by John Slattery on December 13, 2018
#This will encrypt and decrypt messages using your key
def main():
    loop = 1
    x = 3
    while loop == 1:
        loose = input("would you like to encrypte(e) or decrypte(d): ")
        if loose == "e":
            message = input("Enter your Message to encrypte: ")
            x = eval(input("what is the key: "))
            b = 0
            c = ""
            for l in message:
                a = ord(l) - x
                c = chr(a) + c
            print(c)
            x = input("Would you like to do it again(y/n): ")
        if loose == "d":
            message = input("Enter your Message to decrypt: ")
            x = eval(input("what is the key: "))
            b = 0
            c = ""
            for l in message:
                a = ord(l) + x
                c = chr(a) + c
            print(c)
            x = input("Would you like to do it again(y/n): ")
        if not (loose != "e") or (loose != "d"):
            print("please choose an option")
        if x == "y":
            loop = 1
        if x == "n":
            loop = 2
main()