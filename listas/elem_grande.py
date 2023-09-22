# Ejercicio 2: Encontrar el elemento más grande en una lista
# Escribe una función que encuentre el elemento más grande en una lista de números.

elemt = [2,3,5,12,1,5,6,8]

result = None

def elemento(elemt):
    result = None
    for elem in elemt:
        if result is None or elem > result:
            result = elem
    return result            
print(elemento(elemt))    

# DE UNA FORMA MAS SENCILLA

# def newElemnt(elemt):
#     return max(elemt)

# resultado = newElemnt(elemt)

# print(resultado)