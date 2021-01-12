# There are two types of arguments we are passes
# 1.Formal arguments
# 2.Actual arguments

# There are four types of Actual Arguments:
# 1.Position
# 2.Keyword
# 3.Default
# 4.Variable Length

# Position
def add(a,b):       # Formal Argument
    c = a + b
    print(c)
add(50,30)          # Actual Argument

# Keyword
def person(name,age):
    print(name)
    print(age)
person(age=28,name='Nanin')

# default
def person(name,age=18):         # Here age is default
    print(name)
    print(age)
person('Krupa')

# Variable Length
def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)
sum(5,76,45,23)