# 8.py
#by John Slattery on December 13, 2018
#This will encrypt and decrypt messages using your key
# my favorite one ##

def main():
    loop = 1
    x = 3
    while loop == 1:
        

        loose = input("would you like to encrypte(e) or decrypte(d): ")
        if loose == "e":
            infileedName = input("where is the file you would like to decode? ")
            infilee = open(infileedName, "r")
            infilee = infilee.read()
            x = input("what is the key(ex: 7,8,2): ")
            x.split(",")
            y = eval(x[2])
            z = eval(x[3])
            x = eval(x[0])
            b = 0
            c = ""
            for l in infilee:
                a = ord(l) + x - z + y
                c = chr(a) + c
            print(c)
            s = input("Would you like output your file(y/n): ")
            if s == "y":
                outfileName = input("where is the output file located? ")
                outfile = open(outfileName, "w")
                outfile.write(c)
                outfile.close()
            if s == "n":
                loop = 2
            x = input("Would you like to do it again(y/n): ")
        if loose == "d":
            infiledName = input("where is the file you would like to decode? ")
            infiled = open(infiledName, "r")
            infiled = infiled.read()
            x = input("what is the key(ex: 7,8,2): ")
            x.split(",")
            y = eval(x[2])
            z = eval(x[3])
            x = eval(x[0])
            b = 0
            c = ""
            for l in infiled:
                a = ord(l) - x + z - y
                c = chr(a) + c
            print(c)
            s = input("Would you like output your file(y/n): ")
            if s == "y":
                outfileName = input("where is the output file located? ")
                outfile = open(outfileName, "w")
                outfile.write(c)
                outfile.close()
            if s == "n":
                loop = 2
            x = input("Would you like to do it again(y/n): ")
        if not (loose != "e") or (loose != "d"):
            print("please choose an option")
        if x == "y":
            loop = 1
        if x == "n":
            loop = 2
main()