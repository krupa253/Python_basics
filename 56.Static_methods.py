class Student:
    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class")

s1 = Student(34,25,75)
print(s1.avg())
print(Student.getschool())
Student.info()