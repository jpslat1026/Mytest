#12.py
#by John Slattery on January 1, 2019
#This script will converts a list into numbers
def toNumber(strlist):
    for x in range(len(strlist)):
      strlist[x] = eval(strlist[x])

def main(numbers):
   toNumber(numbers)
   print(numbers)
main(["288","77","78"])