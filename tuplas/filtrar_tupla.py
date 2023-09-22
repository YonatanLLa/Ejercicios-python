tupla_original = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tupla_pares = ()

for pares in tupla_original:
    if pares%2 == 0:
        tupla_pares += (pares,)

print(tupla_pares)