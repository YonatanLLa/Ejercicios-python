n = int(input("Ingrese un numero: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i
    
print(f"El factorial de {n} es {factorial}")