#11.py
# by John Slattery November 14, 2018
# A program to convert cups temps to US fluid ounces

print("This script Will calculate the cups to US fluid ounces")
def main () :
   Cups = eval(input("How Many Cups? "))
   oz = Cups * 8
   print(Cups, "cups is", oz, "US fluid ounces.")
   input("Press the <Enter> key to quit.")

main ()
