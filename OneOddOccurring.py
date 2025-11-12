#program to find the element not in to compare
#Function to calculate the nuber of the odd occurring
def oddoccurring(arr):
    #Intialize result
    res = 0
    for element in arr:
        res = res^element
    return res
arr = []
n = int((input("Enter the array size")))
while n:
    num = int(input("Enter your number"))
    arr.append(num)
    n-=1
print("Odd occuring number is ", oddoccurring(arr))