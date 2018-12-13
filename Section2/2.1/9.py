# 9.py
#by John Slattery on December 13, 2018
#This will tell you how many words you have in a sentce

def main():
    words = input("Enter a sentce: ")
    words = words.split(" ")
    c = len(words)
    print("You have", c, "words in your sentce")
main()