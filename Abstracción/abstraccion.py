# La abstracción en la programación orientada a objetos consiste en ocultar los detalles internos de un objeto
# y mostrar solo la información y funcionalidad relevante para su uso.

class Auto:
    def __init__(self):
        # Atributo privado que representa el estado del auto
        self.__estado = "apagado"

    def encender(self):
        # Método para encender el auto
        self.__estado = "encendido"
        print("El auto está encendido")

    def conducir(self):
        # Método para conducir el auto
        if self.__estado == "apagado":
            self.encender()  # Si el auto está apagado, se enciende antes de conducir
        print("Conduciendo el auto")


mi_auto = Auto()  # Creamos una instancia de la clase Auto
mi_auto.conducir()  # Llamamos al método conducir del objeto mi_auto
