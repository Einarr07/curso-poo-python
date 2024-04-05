# El encapsulamiento se refiere a proteger los métodos y atributos de una clase

"""
En python no existen como tal los modificadores de acceso: private y public
En su lugar python utilzia un convención para indicar que un atributo o método es considerado como privado.
Esta convención consiste en utilizar un guion bajo (_) al principio del nombre del atributo o método para indicar que no
debería ser accedido directamente desde fuera de la clase,

NOTA: Aunque es posible acceder a estos elementos desde fuera de la clase, la convención es no hacerlo para mantener
la encapsulación y proteger la integridad de la clase. Es importante destacar que esta convención es solo eso,
una convención, y no impide el acceso directo a los atributos o métodos privados.
"""


class MiCalse:
    def __init__(self):
        self._atributo_privado = "valor"
        # Existen tambien los atributos muy privados o enmascaramiento de nombres, que no nos permitira acceder
        # desde afuera y tendremos un error, esto se utiliza con dos guines bajo
        self.__atributo_mas_privado = 10
    def __hablar(self):
        print("Hola ¿Cómo estas?")

objeto = MiCalse()
objeto_2 = MiCalse()

# print(objeto._atributo_privado)

print(objeto_2.__atributo_mas_privado)