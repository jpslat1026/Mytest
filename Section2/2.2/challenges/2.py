# 2.py
#by John Slattery on January 3, 2019
#this script will calculate a baseball player's ERA
def main():
    e = eval(input("how many earned runs: "))
    i = eval(input("how many innings did you piched: "))
    era = (9 * (e/i))
    era = round(era, 2)
    print(era)
main()