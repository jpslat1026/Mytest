# 1.py
#by John Slattery on January 3, 2019
#this script will calculate the distances of 2 cities using lonatude and latudie
import math
def main():
    latitude = input("What is the are the coordnits of a city(ex. 100,100): ")
    latitude = latitude.split(",")
    print(latitude)
    x1 = eval(latitude[0])
    y1 = eval(latitude[1])
    longitude = input("What are the second pair of coordnits of a city(ex. 100,100): ")
    x2 = eval(longitude[0])
    y2 = eval(longitude[1])
    longitude = longitude.split(",")
    awn = math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)
    print(awn)
main()