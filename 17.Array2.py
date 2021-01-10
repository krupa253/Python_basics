from array import *

vals = array('i',[5,2,6,8,3])
for i in range(5):
    print(vals[i])

#         OR
# for i in range(len(vals)):
#     print(vals[i])
#
#         OR
# for e in vals:
#     print(e)

values = array('i',[5,9,8,4,3])
newArr = array(values.typecode,(a*a for a in values))
for e in newArr:
    print(e)

# i = 0
# while i<len(newArr):
#     print(newArr[i])
#     i += 1