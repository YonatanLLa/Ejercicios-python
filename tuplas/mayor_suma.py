# Ejercicio 3: Encontrar la Tupla con la Mayor Suma
# Dada una lista de tuplas que contienen pares de números, encuentra la tupla que tiene la mayor suma de sus elementos.

lista_de_tuplas = [(1, 2), (4, 5), (6, 7), (8, 9)]

# Tu codigo aqui:
numero_mayor = None

for lista in lista_de_tuplas:
    newlista = lista[0] + lista[1]
    if numero_mayor is None or newlista > numero_mayor:
        numero_mayor = newlista

print(numero_mayor)