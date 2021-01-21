class A:
    def feature1(self):
        print("Feature 1 working")

class B:
    def feature2(self):
        print("Feature 2 working")

class C(A,B):
    def feature3(self):
        print("Feature 3 working")

a1 = A()
b1 = B()
c1 = C()
a1.feature1()
b1.feature2()
c1.feature3()
c1.feature2()
c1.feature1()