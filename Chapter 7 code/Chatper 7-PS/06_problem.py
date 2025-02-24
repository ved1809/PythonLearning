# 5! = 5 X 4 X 3 X 2 X 1
n = int(input("Enter the number for factorial: "))
product = 1
for i in range(1 , n+1):
    product = product * i

print(f"The factorial of {n} is {product}")