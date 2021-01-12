def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,':',j)

person('Krupa',age=21,city='Ahmedabad',Mob=23948573)