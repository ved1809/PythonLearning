def divi5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,5,45,67,90,87,85]
f= list(filter(divi5, a))
print(f)
