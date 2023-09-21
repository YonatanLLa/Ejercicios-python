texto = input("Ingrese cadena de tezto: ")

texto = texto.lower()

vocales = "aeiou"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1
        
print(f"El numero de vocales en la cadena es: {contador}")

