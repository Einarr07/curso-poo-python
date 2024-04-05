class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # Un getter es un método que permite obtener el valor de un atributo privado de una clase desde fuera de la clase.
    # En este ejemplo estamos obteniendo el valor del atributo __nombre de la clase persona
    def get_nombre(self):
        return self.__nombre

    # Un setter es un método que permite modificar el valor de un atributo privado de una clase desde fuera de la clase.
    # En este ejemplo estamos modificando el valor del atributo __nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


dalto = Persona("Lucas", 21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Anthonio")

nombre = dalto.get_nombre()
print(nombre)
