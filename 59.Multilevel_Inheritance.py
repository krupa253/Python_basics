class A:
    def feature1(self):
        print("Feature 1 Working")

class B(A):
    def feature2(self):
        print("Feature 2 Working")

class C(B):
    def feature3(self):
        print("Feature 3 Working")

a1 = A()
b1 = B()
c1 = C()
a1.feature1()
b1.feature2()
b1.feature1()
c1.feature3()
c1.feature2()
c1.feature1()