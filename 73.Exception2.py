a = 5
b = 2
try:
    print("Resource open")
    print(a/b)

except Exception as e:
    print("Hey, You cannot divide a number by zero",e)

finally:
    print("Resource closed")