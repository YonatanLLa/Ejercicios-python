import random

def jugar_juego():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10  # Límite de intentos
    record = obtener_record()

    print(f"¡Bienvenido al juego de adivinanza! Adivina el número secreto entre 1 y 100.")
    print(f"Tu récord actual es de {record} intentos.")

    while intentos < max_intentos:
        try:
            intento = int(input("Ingresa tu intento: "))
            intentos += 1

            if intento < numero_secreto:
                print("El número secreto es mayor. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("El número secreto es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
                if intentos < record:
                    establecer_record(intentos)
                else:
                    print(f"No has superado tu récord actual de {record} intentos.")
                break

        except ValueError:
            print("Por favor, ingresa un número válido.")

    if intentos == max_intentos:
        print(f"¡Agotaste tus {max_intentos} intentos! El número secreto era {numero_secreto}.")

def obtener_record():
    try:
        with open("record.txt", "r") as archivo:
            record = int(archivo.read())
    except FileNotFoundError:
        record = float('inf')
    return record

def establecer_record(intentos):
    with open("record.txt", "w") as archivo:
        archivo.write(str(intentos))
        print(f"¡Nueva marca récord establecida: {intentos} intentos!")

while True:
    opcion = input("Elige una opción:\n1. Jugar\n2. Salir\n")
    if opcion == "1":
        jugar_juego()
    elif opcion == "2":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")