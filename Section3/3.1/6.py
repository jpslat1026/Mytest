#6.py
#by John Slattery on January 4, 2019
#this script will tell you your cost for your speeding tickit
def main():
    mph = int(input("How fast were you going: "))
    limit = int(input("What is the speed limit: "))
    if mph > limit:
        x = ((mph - limit)*5) + 50
        if mph > 90:
            x = x + 200
        x = str(x)
        print("You have to pay $" + x )
    else:
        print("No fines here")
main()