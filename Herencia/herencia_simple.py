# Clase padre o super_clase
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


# Clase hija o sub_clase
# Dentro del parentecis colocamos el nombre de la clase que queremos que herede
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, salario, trabajo):
        # En esta linea le decimos lo que va a heredar de la clase padre
        super().__init__(nombre, edad, nacionalidad)
        self.salario = salario
        self.trabajo = trabajo

    # Sobre escribimos el método de la clase padre Persona
    def hablar(self):
        print("Estoy ocupado")


juan = Persona("Juan",33,"peruano")
roberto = Empleado("Roberto", 25, "colombiano", 2000000, "futbolista")

roberto.hablar()
