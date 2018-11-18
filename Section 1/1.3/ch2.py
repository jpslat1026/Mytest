#ch2.py
#by John Slattery on November 15, 2018
# This script will calculate how long it will take to serve every body in line
def main():
    print("This script will calculate how long it will take to serve every body in line")
    people = eval(input("How Many people are waiting in line: "))
    time = people * 4
    print("it will take", time, "minuets to serve everybody in line")
main()