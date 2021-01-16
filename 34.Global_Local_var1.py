a = 10      # Global Variable

def something():
    a = 15          # Local Variable
    print("In Function:",a)
something()
print("Outside Function:",a)