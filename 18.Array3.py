from array import *
arr = array('i',[])
n = int(input("Enter the length of Array:"))
for i in range(n):
    x = int(input("Enter the value:"))
    arr.append(x)
print(arr)