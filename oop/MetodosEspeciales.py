class Coche:
    def __init__(self, marca, kilometros, anio ):
        self.marca = marca
        self.kilometros = kilometros
        self.anio = anio
        print(f"Se Creaó el auto {self.marca}")
        
    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        if self.enmarcha:
            return "auto ensendido"
        else:
            return "Auto apagado"
        
    def __del__(self):
        print(f"Se ha vendido el auto {self.marca}")
    
    def __str__(self):
        return 'El auto es un {}, tiene {}, y es del año {}'.format(self.marca, self.kilometros, self.anio)
    

miCoche = Coche("Audi", 200, 1995)

print(str(miCoche))