lista_de_personas = [("Alice", 25), ("Bob", 30), ("Charlie", 25), ("David", 30), ("Eve", 35)]

diccionario_de_edades = {}

for nombre, edad in lista_de_personas:
    if edad in diccionario_de_edades:
        diccionario_de_edades[edad] += 1
    else:
        diccionario_de_edades[edad] = 1
    
    

print(diccionario_de_edades)