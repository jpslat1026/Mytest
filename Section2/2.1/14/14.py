def main():
    filea = input("Enter a file name: ")
    fileb = open(filea, "r")
    S = fileb.read()
    c = len(S)
    w = len(S.split())
    l = len(S.splitlines())
    print(l,"lines,",w,"words",c,"characters")
main()
