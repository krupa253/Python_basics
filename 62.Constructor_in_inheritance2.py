# When you create object of sub class it will call init of sub class first, if you have call super class then it will
# first call init of super class then call init of sub class

class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 Working")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature1(self):
        print("Feature 1 Working")

a1 = B()