# 4.py
#by John Slattery on January 3, 2019
#this script will go blast off
import time
def countdown():
    i = 0
    for i in range(10):
        print(10 - i)
        time.sleep(1)
    time.sleep(1)
    print("LIFTOFF!!")
countdown()