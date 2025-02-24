def greatest(a1,a2,a3):
    if a1>a2 and a1>a3:
        print(f"{a1} is the greatest")
    elif(a2>a3 and a2>a1):
        print(f"{a2} is the greatest")
    if a3>a1 and a3>a1:
        print(f"{a3} is the greatest")

a1 = int(input("Enter the 1st number: "))
a2 = int(input("Enter the 2st number: "))
a3 = int(input("Enter the 3st number: "))

biggest = greatest(a1,a2,a3)
print(biggest)
