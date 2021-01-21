class Student:
    school = 'My Channel'               # class variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1                # Instance variable
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

s1 = Student(34,47,32)
s2 = Student(68,39,54)
print(s1.avg())


# In instance there are two types of methods:
# 1. Accessor Methods -> getter : It is used for access the value
# 2. Mutator Methods -> setter : It is used for modified value
#
# def get_m1(self):          # getter methods
#     return self.m1
#
# def set_m1(self,value):            # setter methods
#     self.m1 = value