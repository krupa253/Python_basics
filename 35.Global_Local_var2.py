a = 10
def something():
    global a
    a = 15
    print("In Function:",a)
something()
print("Outside Function:",a)