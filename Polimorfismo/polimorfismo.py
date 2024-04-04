# El polimorfismo es la capacidad que tienen los diferentes objetos de recibir un mismo método y comportarse
# de forma distinta.
class Gato:
    def sonido(self):
        return "Miau"


class Perro:
    def sonido(self):
        return "Guau"


def hacer_sonido(animal):
    print(animal.sonido())


bigotes = Gato()
firulais = Perro()

# Polimorfismo de función: Es donde cambia el parametro, es decir, el objeto para reaccionar deacuerdo al método
hacer_sonido(bigotes)

# En este ejemplo de polimorfismo el mismo método funciona diferente para el tipo de objeto
print(firulais.sonido())