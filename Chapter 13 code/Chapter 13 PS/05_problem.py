from functools import reduce
a = [1,5,45,67,90,87,85]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))