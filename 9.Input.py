x = int(input("Enter 1st Number:"))
y = int(input("Enter 2nd Number:"))
z = x + y
print("Sum:", z)

# We want only single character from string
ch = input("Enter String:")[0]
print(ch)

# Use eval
result = eval(input("Enter the expretion:"))
print(result)

# Command line execution enter input
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(z)
# for output write python 9.Input.py 2 3