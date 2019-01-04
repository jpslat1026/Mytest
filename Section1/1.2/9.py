#9.py
# by John Slattery November 14, 2018
# A program to convert Fahrenheit temps to Celsius
print("This script Will calculate the Celsius temp to Fahrenheit")
def main () :
   fahrenheit = eval(input("What is the fahrenheit temperature? "))
   celsius = (fahrenheit - 32) * 5/9
   print("The temperature is", celsius, "degrees Fahrenheit.")
   input("Press the <Enter> key to quit.")

main ()
