class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__prestado = False

    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor

    def esta_prestado(self):
        return self.__prestado

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            return True
        else:
            return False

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            return True
        else:
            return False

    def __str__(self):
        estado = "disponible" if not self.__prestado else "prestado"
        return f"{self.__titulo} de {self.__autor} ({estado})"


class Biblioteca:
    def __init__(self):
        self.__libros = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.__libros:
            if libro.obtener_titulo() == titulo:
                return libro
        return None

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            return libro.prestar()
        else:
            return False

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            return libro.devolver()
        else:
            return False

    def listar_libros(self):
        for libro in self.__libros:
            print(libro)

# Crear algunos libros y una biblioteca
libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez")
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Listar los libros disponibles en la biblioteca
print("Libros disponibles en la biblioteca:")
biblioteca.listar_libros()

# Prestar un libro
if biblioteca.prestar_libro("1984"):
    print("Libro prestado con éxito.")
else:
    print("El libro no está disponible para préstamo.")

# Listar los libros después del préstamo
print("\nLibros disponibles en la biblioteca después del préstamo:")
biblioteca.listar_libros()

# Devolver un libro
if biblioteca.devolver_libro("1984"):
    print("Libro devuelto con éxito.")
else:
    print("No se pudo devolver el libro.")

# Listar los libros después de la devolución
print("\nLibros disponibles en la biblioteca después de la devolución:")
biblioteca.listar_libros()