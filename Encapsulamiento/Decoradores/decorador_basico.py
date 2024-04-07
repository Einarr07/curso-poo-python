# Definimos un decorador básico que añade funcionalidad antes de llamar a la función original
def decorardor(funcion):
    # Definimos una nueva función que envuelve la función original
    def funcion_modificada():
        # Agregamos lógica antes de llamar a la función original
        print("Antes de llamar a la función")
        # Llamamos a la función original
        funcion()

    # Devolvemos la nueva función modificada
    return funcion_modificada


# Definimos una función saludo y aplicamos el decorador
@decorardor
def saludo():
    print("Hola Dalto ¿Cómo andas?")


# Llamamos a la función decorada
saludo()
