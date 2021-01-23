a = 5
b = 2
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a Number:"))
    print(k)

except ZeroDivisionError as e:
    print("Number divide by zero",e)

except ValueError as e:
    print("Invalide Input")

except Exception as e:
    print("Something went wrong...")

finally:
    print("Resource closed")