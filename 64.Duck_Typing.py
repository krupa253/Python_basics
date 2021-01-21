# Polymorphism -> Many Form
# There are four way that we are implement this:
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method overriding

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Leptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()
lap1 = Leptop()
lap1.code(ide)