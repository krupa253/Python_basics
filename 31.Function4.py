# In list if we update the value than both the values are update

def update(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print("x ", lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print("lst ",lst)