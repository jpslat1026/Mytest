#ch3.py
#by John Slattery on November 15, 2018
# This script will calculate how much the bike shop makes averging the helmet costs
def main():
    print("This script will calculate how much the bike shop makes averging the helmet cost")
    bikes = eval(input("How many bikes were purched? "))
    bikeamount = bikes * 250
    helmet = bikes / 5
    helmet = helmet * 50
    total = bikeamount + helmet
    print("The bike shop matkes a total average of", total, "dollars")
main() 