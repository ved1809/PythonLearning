try:
    a = int(input("Hey, enter a number: "))
    print(a)

except ValueError as v:
    print("Hey")
except Exception as e:
    print(e)
    
print("Thanks")