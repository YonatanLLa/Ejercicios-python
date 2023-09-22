# Ejercicio 3: Eliminar duplicados
# Escribe una función que tome una lista y elimine los elementos duplicados, devolviendo una nueva lista sin duplicados.

newLista = [1,2,3,3,2,4,5,6,5]


def delete(newLista):
    lista_sin_duplicados = []
    for dato in newLista:
        if dato not in lista_sin_duplicados:
            lista_sin_duplicados.append(dato)
            print(lista_sin_duplicados)
    return

resultado = delete(newLista)