class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Leptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Leptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Navin',2)
s2 = Student('Jenny',3)
s1.show()