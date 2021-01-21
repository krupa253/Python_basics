# Size of the object depends on the no. of variables and size of each variable
# Constructor allocates size to object

class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 28

c1 = Computer()
c2 = Computer()
c1.name = "Rashi"
print(c1.name)
print(c2.name)
print(id(c1))
print(id(c2))