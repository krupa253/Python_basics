# If you create object of sub class it will first try find init of sub class if it is not found then it will call init of super class

class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 Working")

class B(A):
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("Feature 1 wprking")

a1 = B()