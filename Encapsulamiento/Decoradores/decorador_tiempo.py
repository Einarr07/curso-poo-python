import time


# Definimos un decorador que calcula el tiempo de ejecución de una función
def calcular_tiempo(funcion):
    # El wrapper que se ejecuta antes y después de la función original
    def wrapper(*args, **kwargs):
        # Registra el tiempo de inicio
        inicio = time.time()
        # Ejecuta la función original con los argumentos recibidos
        resultado = funcion(*args, **kwargs)
        # Registra el tiempo de finalización
        fin = time.time()
        # Imprime el tiempo de ejecución de la función
        print(f"Tiempo de ejecución de {funcion.__name__}: {fin - inicio} segundos")
        # Devuelve el resultado de la función original
        return resultado

    # Devuelve el wrapper que contiene la lógica de cálculo del tiempo de ejecución
    return wrapper


# Definimos una función que suma dos números y aplicamos el decorador calcular_tiempo
@calcular_tiempo
def suma(a, b):
    return a + b


# Imprimimos el resultado de llamar a la función decorada
print(suma(1, 2))
