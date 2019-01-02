# 9.py
#by John Slattery on January 1, 2019
#This script will show you your grade
def grade(score):
    values = ["F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F", "D","D","D","D","D","D","D","D","D","D", "C","C","C","C","C","C","C","C","C","C","C","B","B","B","B","B","B","B","B","B","B", "A","A","A","A","A","A","A","A","A","A","A","A",]
    gradestr = values[score]
    print("your grade is: ", gradestr)
grade(20)