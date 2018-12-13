# 12.py
#by John Slattery on December 13, 2018
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("how many years would you like to go: "))
    print("year", "\t", "Value")
    x = 0
    for i in range (year) :
        principal = principal * (1 + apr)
        print(x, "\t", "$" + str(principal))
        x = x + 1

main()