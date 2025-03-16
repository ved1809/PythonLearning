try:
    a = int(input("Hey, enter a number: "))
    print(a)

except ValueError as v:
    print("Hey")

else:
    print("I am inside else")