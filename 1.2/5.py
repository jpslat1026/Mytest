#5.py
# by John Slattery November 14, 2018
# A program to convert Celsius temps to Fahrenheit

print("This script Will calculate the Celsius temp to Fahrenheit")
def main () :
   x = 0
   for i in range(10) :
       celsius = x
       fahrenheit = 9 / 5 * celsius + 32
       print("The temperature is", fahrenheit, "degrees Fahrenheit.")
       x = x + 10

main ()
