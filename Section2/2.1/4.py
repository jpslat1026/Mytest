# 4.py
#by John Slattery on December 11, 2018
#This will tell you your grade

def main():
    #input
    x = input("enter a phrase: ")
    #words = [all , words, in, a, string, that, the, user, inputs.]
    words = x.split()
    #y = nothing so we con add y combine nothing with the first letter
    y = ""
    #for loop in that adds y to y plus the first letter of the word
    for i in words:
        y = y + i[0].upper()
    #prints your acronym
    print("Your acronym is:  " + "\" " + y + " \"")
main()
