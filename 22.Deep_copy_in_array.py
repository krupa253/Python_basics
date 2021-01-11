from  numpy import *

arr1 = array([3,5,7,4,5,9])
arr2 = arr1.copy()
arr1[1] = 1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))