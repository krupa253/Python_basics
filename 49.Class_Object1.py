# class -> design
# object -> Instance

# In class there is two things included,
# 1. Attributes -> Variables
# 2. Behaviour -> Methods[Function]

class Computer:
    def config(self):
        print("i5,16gh,1TB")
com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()