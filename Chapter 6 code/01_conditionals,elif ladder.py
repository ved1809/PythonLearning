age = int(input("Enter the age: "))
if age >= 18:
    print("You are an adult")
    print("You can also vote")
elif age<0:
    print("You are entering invalid age")
elif age==0:
    print("You are a new born")

else:
    print("You are not adult")

print("End of prog")