def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except Exception as e:
        return str(e)

filenames = ["1.txt", "2.txt", "3.txt"]

for filename in filenames:
    print(read_file(filename))

print("Thank You!")