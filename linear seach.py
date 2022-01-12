print("This is linear search")
def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr=["y", "a", "a", "g", "t", "v", "m", "-", "n", "s", "k"]
x=input("Enter the element to search")
print("element found at index "+str(linearsearch(arr,x)))