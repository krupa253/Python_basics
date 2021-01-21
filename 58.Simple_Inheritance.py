class A:
    def feature1(self):
        print("Feature 1 Working")

class B(A):
    def feature2(self):
        print("Feature 2 Working")

a1 = A()
b1 = B()
a1.feature1()
b1.feature2()
b1.feature1()