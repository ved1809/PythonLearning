def CeltoFar(C):
    return (C - 32) * 5 / 9

C = float(input("Enter the temperature in Celcius"))
F = CeltoFar(C)
print("The temperature in Fahrenheit is", F)