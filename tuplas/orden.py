# Ejercicio 5: Ordenar una lista de tuplas por el segundo elemento
# Dada una lista de tuplas en la que cada tupla contiene dos elementos, ordena la lista de tuplas en función del segundo elemento de cada tupla en orden ascendente. Por ejemplo, si tienes la lista [(3, 5), (1, 2), (2, 4)], deberías obtener [(1, 2), (2, 4), (3, 5)] como resultado.

lista_de_tuplas = [(3, 5), (1, 2), (2, 4)]

lista_de_tuplas_ordenada = sorted(lista_de_tuplas, key=lambda x:x[1])

print(lista_de_tuplas_ordenada)
