a = 10
print(id(a))

def something():
    a = 22
    x = globals()['a']
    print(id(a))
    print("In Function:",a)
    globals()['a'] = 15
something()
print("Outside Function:",a)