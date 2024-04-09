# Principio de responsabilidad única (Una clase debe existir para cumplir una tarea en especifico si una clase realiza
# dos o más tareas debemos separarlo en otras clases)

# Definición de la clase TanqueDeCombustible, que representa el tanque de combustible del auto
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100  # Inicializa el tanque con 100 unidades de combustible

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad  # Permite agregar combustible al tanque

    def obtener_combustible(self):
        return self.combustible  # Devuelve la cantidad actual de combustible en el tanque

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad  # Reduce la cantidad de combustible en el tanque


# Definición de la clase Auto, que representa un automóvil con un tanque de combustible
class Auto:
    def __init__(self, tanque):
        self.posicion = 0  # La posición inicial del auto es 0
        self.tanque = tanque  # El auto tiene un tanque de combustible dado

    def mover(self, distancia):
        # Verifica si hay suficiente combustible para moverse la distancia especificada
        if self.tanque.obtener_combustible() >= distancia / 2:
            # Si hay suficiente combustible, mueve el auto y usa combustible
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Haz movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion  # Devuelve la posición actual del auto


# Creación de una instancia de TanqueDeCombustible y una instancia de Auto con ese tanque
tanque = TanqueDeCombustible()
auto = Auto(tanque)

# Ejemplo de uso
print(auto.obtener_posicion())  # Imprime la posición inicial del auto
auto.mover(10)  # Intenta mover el auto 10 unidades
print(auto.obtener_posicion())  # Imprime la nueva posición del auto
auto.mover(20) # Intenta mover el auto 20 unidades
print(auto.obtener_posicion())  # Imprime la nueva posición del auto
auto.mover(60) # Intenta mover el auto 60 unidades
print(auto.obtener_posicion())  # Imprime la nueva posición del auto
auto.mover(100) # Intenta mover el auto 100 unidades
print(auto.obtener_posicion())  # Imprime la nueva posición del auto
auto.mover(100) # Intenta mover el auto 100 unidades, pero no hay suficiente combustible

