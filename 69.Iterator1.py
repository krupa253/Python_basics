# Iterator is used for iteration
# Normal iterater function(inbuite iterator)
# __next__() will give you the next value

nums = [7,9,3,6]
it = iter(nums)
print(it.__next__())
print(next(it))
for i in nums:
    print(i)