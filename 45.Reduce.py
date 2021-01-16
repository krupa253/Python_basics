from  functools import reduce
def add_all(a,b):
    return  a + b
doubles = [4,12,16,8,12,4]
# sum = reduce(lambda a,b : a + b,doubles)
sum = reduce(add_all,doubles)
print(sum)


