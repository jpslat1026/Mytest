# 10.py
#by John Slattery on January 1, 2019
#This script will give you an acronym for a phrase

def acronym(phrase):
    #words = [all , words, in, a, string, that, the, user, inputs.]
    words = phrase.split()
    #y = nothing so we con add y combine nothing with the first letter
    y = ""
    #for loop in that adds y to y plus the first letter of the word
    for i in words:
        y = y + i[0].upper()
    #prints your acronym
    print("Your acronym is:  " + "\" " + y + " \"")
acronym("john was here")
