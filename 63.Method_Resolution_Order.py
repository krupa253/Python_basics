class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1-A working")

class B:
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("Feature 1-B working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

a1 = C()
a1.feature1()