
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

m = int(input("ingrese un numero entero: "))

if es_primo(m):
    print(f"{m} es un numero primo")
else:
    print(f"{m} no un numero primo")
    