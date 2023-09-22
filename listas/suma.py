# Ejercicio 1: Sumar elementos de una lista
# Dada una lista de números, escribe una función que calcule la suma de todos los elementos de la lista.

elem1 = [1,2,3,4]


def suma(elem1):
    sum = 0
    for result in elem1:
        sum += result
    return sum
        
print(suma(elem1))