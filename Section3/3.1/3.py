# 3.py
#by John Slattery on January 4, 2019
#this script will tell you your grade
def main():
    letters = ["A", "B", "C", "D", "F"]
    num = int(input("what was your score: "))
    if num >= 90:
        print("Your grade was a", letters[0])
    elif num >= 80 and num < 90:
        print("Your grade was a", letters[1])
    elif num >= 70 and num < 80:
        print("Your grade was a", letters[2])
    elif num >= 60 and num < 70:
        print("Your grade was a", letters[3])
    elif num < 60:
        print("Your grade was a", letters[4])
main()