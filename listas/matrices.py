# Ejercicio 5: Matrices y multiplicación
# Escribe una función que realice la multiplicación de dos matrices representadas como listas de listas. Asegúrate de validar que las matrices sean compatibles para la multiplicación.

def multiplicar_matrices(matriz1, matriz2):
    # validamos compatibilidad
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("Las matrices no son compatibles para la multiplicaxion")
    
    # Iniciar la matriz resultado con ceros
    filas_resultado = len(matriz1)
    print(filas_resultado)
    columnas_resultado = len(matriz2[0])
    print(columnas_resultado)
    
    resultado = [[0 for _ in range(columnas_resultado)] for _ in  range(filas_resultado)]
    
    print(resultado)
    # Realizar la multiplicacion de matrices
    for i in range(filas_resultado):
        for j in range(columnas_resultado):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

matriz1 = [[1,2],[3,4]]
matriz2 = [[5,6],[7,8]]

resultado = multiplicar_matrices(matriz1,matriz2)

for fila in resultado:
    print(fila)

