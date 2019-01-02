def squareEach(nums):
  for i in nums:
       v = i * i
  return v
    
def sumList(nums):
    v = 0
    for i in nums:
       v = v + i
    return v

def toNumber(strList):
  for i in range(len(strList)):
    strList[i] = eval(strList[i])

def main():
    
    fileIn = input("Enter filename: ")
    infile = open(fileIn,"r")
    fileContents = infile.read()
    list = fileContents.split()
    toNumber(list)
    squareEach(list)

    print("This is your output:", sumList(list))
main()
