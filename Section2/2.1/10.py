# 10.py
#by John Slattery on December 13, 2018
#This will tell you the average amount of words you havre in a sentce

def main():
    words = input("Enter a sentce: ")
    words = words.split(" ")
    k = len(words)
    c = 0
    for i in words:
        v = len(i)
        c = c + v
    aw = c / k
    print(aw, "is the average amount of words you have in a sentce")
main()