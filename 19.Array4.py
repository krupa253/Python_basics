# Search in Array
from array import *

arr = array('i',[])
n = int(input("Enter the length of Array:"))
for i in range(n):
    x = int(input("Enter the value:"))
    arr.append(x)
print(arr)
val = int(input("Enter the value that you want to search:"))
k = 0
for e in arr:
    if e==val:
       print(k)
       break
    k += 1

# print(arr.index(val))

# It will give the index of the number that you want to search