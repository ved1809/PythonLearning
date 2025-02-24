def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

n = int(input("Enter the number of for sum of natural"))    
sum = sum(n)
print(f"The sum sum of 1st {n} natural number is {sum}")
    