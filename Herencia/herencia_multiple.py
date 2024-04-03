# Clase padre o super_clase
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")


# Clase hija o sub_clase
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    # Creamos el constructor
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        # Le decimos de que clases va a heredar los atributos en este caso tenemos las clases Persona y Artista
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        # Definimos los nuevos atributos
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        # Cuando colocamos super() le decimos que va a heredar el método
        print(f"Hola mi nombre es {self.nombre} y {super().mostrar_habilidad()}"
              f" y trabajo en: {self.empresa}")


jaime = EmpleadoArtista("Jaime", 27, "chileno", "tocar el piano", 700,
                        "Music Golden")

jaime.presentarse()

# En esta parte decimos que si EmpleadoArtista es una sub_clase de Artista
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

# Le decimos si una instancia en este caso Jaime es una instancia de la clase EmpleadoArtista
# Esto tambien funcionaria si colocaramos que jaime es una instancia de persona y de artista (Nos retorna True)
instacia = isinstance(jaime, EmpleadoArtista)
print(instacia)