#ch3.py
#by John Slattery on November 15, 2018
# This script will calculate how much the bike shop makes averging the helmet costs
def main():
    print("This script will calculate how much the bike shop makes averging the helmet cost")
    bikes = eval(input("How many bikes were purched? "))
    bickeamount = bikes * 250
    for i in [5,10]:
        bickeamount = bickeamount + 50
    print(bickeamount)
main() 