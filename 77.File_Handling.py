f = open('Mydata','r')
print(f.readline(),end="")
print(f.read())

# Copy content of one file and move to another file
# f = open('Mydata','r')
# f1 = open('abc','w')
# for data in f:
#     f1.write(data)

# Copy one picture to another .jpg file
# f = open('IMG_123.jpg','rb')            # read binary
# f1 = open('IMG_456.jpg','wb')           # write binary
# for i in f:
#     f1.write(i)