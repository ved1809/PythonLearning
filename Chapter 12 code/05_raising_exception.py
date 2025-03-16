a = int(input("Enter a number"))
b = int(input("Enter second number"))

if(b==0):
    raise ZeroDivisionError("Our program is not meant to divide by zero")
else:
    print(f"THe division is {a/b}")

