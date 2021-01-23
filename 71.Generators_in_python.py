# Generators will give you iterators.
# If we fetch entire list from database then generator fetch one by one value from database
# return will terminate the function but yield can't so we have to use it at generators

def topten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1

values = topten()
for i in values:
    print(i)