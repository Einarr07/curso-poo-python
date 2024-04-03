class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} años y estoy en {self.grado} grado")


bartolomeo = Persona("Bartolomeo", 45)
henrique = Estudiante("Henrique", 13, "8vo")

bartolomeo.presentarse()
henrique.presentarse()
