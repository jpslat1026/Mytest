# 3.py
#by John Slattery on January 14, 2019
#this script will tell you if a bill passes

def main():
    g = input("What are voting to pass: ")
    votesa = int(input("How many people are voting: "))
    voteyes = int(input("How many people vated yes: "))
    total = voteyes / votesa
    if total > .5:
        print("The law of", g, "passed")
    else:
        print("The law of", g, "did not pass")
main()