# 3.py
#by John Slattery on December 11, 2018
#This will tell you your grade

def main():
    values = ["F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F", "D","D","D","D","D","D","D","D","D","D", "C","C","C","C","C","C","C","C","C","C","C","B","B","B","B","B","B","B","B","B","B", "A","A","A","A","A","A","A","A","A","A","A","A",]
    grade = eval(input("How many points did you get 0-100: "))
    gradestr = values[grade]
    print(gradestr)
main()