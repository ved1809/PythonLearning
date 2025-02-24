f= open("file.txt")
print(f.read())
f.close()

# The same can be done using with statement like this
with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file