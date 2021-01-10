available = 5
x = int(input("How many candies you want?"))
i = 1
while i <= x:
    if i > available:
        print("Out of Stock")
        break
    print("Candy")
    i += 1