class Student:
    school = 'Telusko'              # class variable

    @classmethod
    def info(cls):
        return cls.school

print(Student.info())