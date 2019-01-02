#12.py
#by John Slattery on January 1, 2019
#This script will sum each number together in a given list

def sumList(nums):
    v = 0
    for i in nums:
       v = v + i
    print("all of the numbers sumed is:", v)
sumList([1,2,3,4,5,6,7,8,9,10])