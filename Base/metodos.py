# Una clase es un elemento que actúa como una plantilla y va a definir las caracteristicas (atributos) y comportamientos
# (métodos) de una entidad o un objeto
class Celular:
    # Método Constructor
    # __inir__ : Este es un método especial en Python que se llama cuando se crea un nuevo objeto de una clase
    # self : Es una forma de hacer referencia al objeto mismo
    # Los atributos o propiedades son: marca, modelo, camara
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Los métodos son las acciones que puede realizar el objeto
    # En los métodos siempre se debe pasar el parametro self
    def llamar(self):
        print(f"Estas haciendo una llamada desde un: {self.modelo}")

    def colgar(self):
        print(f"Cortaste la llamada desde un: {self.modelo}")


# Le pasamos los atributos del constructor, también se las conoce como: "propiedades de instancia".
# Tenemos 4 instancias que son: celular1,2,3,4 es decir, tenemos 4 objetos
celular1 = Celular("Samsung","S23", "45MP")
celular2 = Celular("Apple","Iphone 15 Pro", "96MP")
celular3 = Celular("Xiaomi","Poco X5 Pro", "85MP")
celular4 = Celular("Honor", "Honor X7", "75MP")

print(celular1.marca)