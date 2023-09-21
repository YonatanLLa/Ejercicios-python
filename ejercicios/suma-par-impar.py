# Suma de números pares e impares:
# Escribe un programa que solicite al usuario un número entero y luego calcule la suma de todos los números pares y la suma de todos los números impares desde 1 hasta ese número.

n = int(input("Ingrese un numero entero: "))
suma_pares = 0
suma_impares = 0

for i in range(1, n+1):
    if i%2 == 0:
        suma_pares += i
    else:
        suma_impares += i
        
print(f"Suma de nùmeros pares: {suma_pares}")
print(f"Suma de nùmeros impares: {suma_impares}")