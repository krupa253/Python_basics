from numpy import *

arr1 = array([
    [1,2,3,4,5,6],
    [3,6,2,7,5,8]
])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3)
print(arr3)