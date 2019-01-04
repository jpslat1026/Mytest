# 2.py
#by John Slattery on January 4, 2019
#this script will tell you your grade
def main():
    letters = ["A", "B", "C", "D", "F"]
    num = eval(input("what was your score: "))
    if num == 5:
        print("Your grade was a", letters[0])
    elif num == 4:
        print("Your grade was a", letters[1])
    elif num == 3:
        print("Your grade was a", letters[2])
    elif num == 2:
        print("Your grade was a", letters[3])
    elif num == 1:
        print("Your grade was a", letters[4])
    elif num == 0:
        print("Your grade was a", letters[4])
main()