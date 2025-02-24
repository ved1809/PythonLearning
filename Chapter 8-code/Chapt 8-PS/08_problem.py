def multiply(n):
    for i in range(1,11):
        print(f"|{i} X {n}= {n*i}|")

n = int(input("Enter the number for multipliaction table"))
print(multiply(n))