from numpy import *

# array()
arr1 = array([1,2,3,4,5],float)
print(arr1.dtype)
print(arr1)

# linespace()
arr2 = linspace(0,15,16)
print(arr2)

# arange()
arr3 = arange(1,15,2)
print(arr3)

# logspace()
arr4 = logspace(1,40,5)
print('%2f' %arr4[0])

# zeros()
arr5 = zeros(5)
print(arr5)

# ones()
arr6 = ones(5,int)
print(arr6)

# add two Array
arr7 = array([1,2,3,4,5])
arr8 = array([6,7,8,9,5])
arr9 = arr7 + arr8
print(arr9)

# concate two Array
print(concatenate([arr7, arr8]))
