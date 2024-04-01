# Una clase es un elemento que actúa como una plantilla y va a definir las caracteristicas y comportamientos
# de una entidad o un objeto
class Celular():
    # Atributos estaticos (Cada ves que construimos un objeto tendrá estos atributos por defecto)
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"


# Los objetos representan una entidad (instancias de una clase) de la vida real, en este ejemplo un celular
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

print(celular1.marca)