#7.py
#by John Slattery on January 4, 2019
#this script will tell you how much you have to pay the baby sitter
def main():
    start = int(input("what time did you start(1-24): "))
    end = int(input("what time did you end(1-24): "))
    x = 0
    enda = end - 21
    if enda > 0:
        x = enda * 1.75
    time = end - start
    time = time - enda
    x = time * 2.50 + x
    x = str(x)
    print("You pay the baby sitter $" + x )
main()