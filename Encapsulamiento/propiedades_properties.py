# Esta es la forma correcta de usar los setters y los getters
class Animal:
    def __init__(self, nombre, especie):
        self.__nombre = nombre
        self.__especie = especie

    # Getter
    @property
    def nombre(self):
        return f"El animal es un: {self.__nombre} de la especie {self.__especie}"

    # Setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre


animal1 = Animal("Loro", "ave")

nombre = animal1.nombre
print(nombre)

animal1.nombre = "Pinguino"

# del animal1.nombre

nombre = animal1.nombre
print(nombre)