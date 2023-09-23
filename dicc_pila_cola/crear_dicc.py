mi_diccionario = {
    "nombre": "juan",
    "edad": 30
}

mi_diccionario["nombre"] = "pedro"

mi_diccionario["lastname"] = "ortiz"

# del mi_diccionario["nombre"]
# print(mi_diccionario.pop("lastname"))

# for valor in mi_diccionario:
    # print(valor)
    
# for valor in mi_diccionario.values():
    # print(valor)

for clave, valor in mi_diccionario.items():
    print(clave, valor)
    
# print(mi_diccionario)