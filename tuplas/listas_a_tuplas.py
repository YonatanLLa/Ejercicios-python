# Ejercicio 5: Combinar Dos Listas en una Lista de Tuplas
# Dadas dos listas, lista1 y lista2, crea una lista de tuplas donde cada tupla contenga un elemento de lista1 y un elemento correspondiente de lista2.

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

#Tu codigo aqui
resultado = []

if len(lista2) == len(lista2):
    for i in range(len(lista1)):
        tupla = (lista1[i], lista2[i])
        resultado.append(tupla)
else:
    print("No se pueden convinar por la diferencia en su longitud")

print(f"la lista es: {resultado}")


# Debería imprimir [(1, 'a'), (2, 'b'), (3, 'c')]
