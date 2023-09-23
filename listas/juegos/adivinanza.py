# Ejercicio 6: Juego de adivinanza
# Crea un juego en el que el programa elija un número aleatorio y el jugador tenga que adivinarlo. El programa debe proporcionar pistas sobre si el número a adivinar es mayor o menor que el intento del jugador. El juego debe continuar hasta que el jugador adivine el número correcto.

import random

# Genera un Número aleatorio entre 1 y 100

numero_secreto = random.randint(1,100)

intento = 0 
adivinando = False

print("!Bienvenido al juedo de adivinanza!, adivina tu numero.")

while not adivinando:
    try: 
        intento = int(input("Ingresa tu intento: "))
        intento += 1
        if intento < numero_secreto:
            print("El numero secreto es mayor")
        elif intento > numero_secreto:
            print("El numero secreto es menor")
        else:
            adivinando = True
            print(f"¡Felicidaddes!")
    except ValueError:
        print("Por favor, ingresa un número valido.")