n = int(input("Enter Number:"))

for i in range(2,n):
    if n%i==0:
        print("Not Found")
        break
else:
    print("Prime")