#ch4.py
#by John Slattery on November 15, 2018
# This script will calculate the anwser for the weat and chess board problem
def main():
    print("This script will calculate the anwser for the weat and chess board problem")
    x = 1
    n = eval(input("What square do you want to now How many grains are there: "))
    for i in range(n):
        x = x * 2
    print(x)
main()