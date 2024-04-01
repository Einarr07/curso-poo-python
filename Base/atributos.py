# Una clase es un elemento que actúa como una plantilla y va a definir las caracteristicas (atributos) y comportamientos
# (métodos) de una entidad o un objeto
class Celular:
    # Constructor
    # __inir__ : Este es un método especial en Python que se llama cuando se crea un nuevo objeto de una clase
    # self : Es una forma de hacer referencia al objeto mismo
    # Los atributos o propiedades son: marca, modelo, camara
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


# Le pasamos los atributos del constructor, también se las conoce como: "propiedades de instancia".
# Tenemos 1 instancia que es celular1, es decir, tenemos un objeto
celular1 = Celular("Samsung","S23", "45MP")

print(celular1.marca)