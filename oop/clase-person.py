# Ejercicio 1: Crear una clase

# Crea una clase llamada Persona con atributos nombre y edad. Luego, crea un objeto de tipo Persona e imprime sus atributos.

class Persona: 
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

persona1 = Persona("yonatan", 24)

persona1.saludar()