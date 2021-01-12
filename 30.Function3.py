def update(x):
    x = 10
    print("x ",x)

a = 12
update(a)
print("a ",a)


def update(y):
    print(id(y))
    y = 20
    print(id(y))
    print("y ",y)

b = 22
print(id(b))
update(b)
print("b ",b)