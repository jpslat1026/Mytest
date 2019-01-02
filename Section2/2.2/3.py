# 3.py
#by John Slattery on January 1, 2019
#This script will find the given radius for a sphere
from math import*
def sphereArea(r):
  A = 4*pi*r**2
  return A
def sphereVolume(r):
  V = (4/3)*pi*r**3
  return V
def main(radiusa):
  V = sphereVolume(radiusa)
  A = sphereArea(radiusa)
  print("The area is", A)
  print("The volume is", V)
main(1)