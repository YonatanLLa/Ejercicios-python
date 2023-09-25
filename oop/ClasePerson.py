class Persona: 
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def datosPersonales(self):
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"El nombre de la edad es: {self.edad}")
        print(f"El nombre de la sexo es: {self.sexo}")
        
persona1 = Persona('Yonatan', 24, "Masculino")
persona2 = Persona('juan', 23, "Masculino")
persona3 = Persona('Karen', 21, "Femenino")

persona1.datosPersonales()
print()
persona2.datosPersonales()
print()
persona3.datosPersonales()
print()

