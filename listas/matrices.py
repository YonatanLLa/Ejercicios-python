# Ejercicio 5: Matrices y multiplicación
# Escribe una función que realice la multiplicación de dos matrices representadas como listas de listas. Asegúrate de validar que las matrices sean compatibles para la multiplicación.

def multiplicar_matrices(matriz1, matriz2):
    # validamos compatibilidad
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("Las matrices no son compatibles para la multiplicaxion")
    
    # Iniciar la matriz resultado con ceros
    filas_resultado = len(matriz1)
    columnas_resultado = len(matriz2[0])
    
    resultado = [[0 for _ in range(columnas_resultado)] for _ in  range(filas_resultado)]
    
    
    print(resultado)
    
    return

matriz1 = [[1,2],[3,4]]
matriz2 = [[5,6],[7,8]]

multiplicar_matrices(matriz1,matriz2)
