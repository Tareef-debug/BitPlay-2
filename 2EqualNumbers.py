#Program to check if user given numbers are equal without using any comparism
def checkifsame(n1,n2):
    if ((n1^n2)!=0):
        print("Both Numbers are not equal")

    else:
        print("Both Numbers are equal")
n1 = int(input("Enter the first number to compare"))
n2 = int(input("Enter the second number to compare"))
checkifsame(n1,n2)