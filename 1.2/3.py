# 3.py
# by John Slattery November 14, 2018
# A simple program to average three exam scores
# Illustrates use of multiple input

def main():
   print("This program computes the average of three exam scores. ")

   score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
   average = (score1 + score2 + score3) / 2

   print("The average of the scores is: ", average)
   input("Press the <Enter> key to quit.")
main()
