#ch4.py
#by John Slattery on November 15, 2018
# This script will calculate what change you need
def main():

    print("This script will calculate what change you need")
    c=eval(input('How much is the item between 0-99: '))
    print(c // 25, "quarters")
    c = c % 25
    print(c // 10, "dimes")
    c = c % 10
    print(c // 5, "nickles")
    c = c % 5
    print(c // 1, "pennies")
main()