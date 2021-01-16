def is_even(n):
    return n%2==0
nums = [4,2,6,7,3,8,46]
evens = list(filter(is_even,nums))
print(evens)