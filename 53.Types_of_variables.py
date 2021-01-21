# There are two types of variable:
# 1. Instance Variable : When we are declare variable inside init method then it is called as instance variable
# 2. Class(Static) Variable : If we are declare variable outside init but in class is called as class variable
#
# Namespace : Namespace is an area where you create and store object/variable.
# 1. class namespace : Where you store all the class variable
# 2. object / Instance namespace : Where you will create instance variable

class Car:
    wheels = 4              # Class Variable
    def __init__(self):
        self.mil = 10           # Instance Variable
        self.com = "BMW"

c1 = Car()
c2 = Car()
c1.mil = 8
Car.wheels = 5
