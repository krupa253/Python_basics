def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return  even,odd
lst = [20,25,46,97,65,78,94]
even, odd = count(lst)
print("Even : {} and odd : {}".format(even,odd))