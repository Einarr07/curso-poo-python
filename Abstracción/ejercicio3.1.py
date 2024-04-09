class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        """
        Inicializa un nuevo Personaje con un nombre, fuerza y velocidad dados.

        Args:
        nombre (str): El nombre del personaje.
        fuerza (float): La fuerza del personaje.
        velocidad (float): La velocidad del personaje.
        """
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        """
        Retorna una representación en cadena del Personaje, mostrando su nombre, fuerza y velocidad.
        """
        return f"{self.nombre}, (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def fusionar(self, otro_pj):
        """
        Fusiona este personaje con otro personaje dado, creando un nuevo personaje con un nombre combinado
        y valores de fuerza y velocidad promediados.

        Args:
        otro_pj (Personaje): El otro personaje con el que se fusionará.

        Returns:
        Personaje: El nuevo personaje resultado de la fusión.
        """
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) / 100 * 100, 2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) / 100 * 100, 2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


personajes = []


def crear_personaje():
    """
    Crea un nuevo personaje pidiendo al usuario que ingrese un nombre, fuerza y velocidad.

    Returns:
    Personaje: El nuevo personaje creado.
    """
    nombre = input("Ingrese el nombre del personaje: ")
    fuerza = float(input("Ingrese la fuerza del personaje: "))
    velocidad = float(input("Ingrese la velocidad del personaje: "))
    return Personaje(nombre, fuerza, velocidad)


def mostrar_personajes(personajes):
    """
    Muestra todos los personajes en la lista de personajes dada.

    Args:
    personajes (list): La lista de personajes a mostrar.
    """
    if not personajes:
        print("Aun no existe ningun personaje")
    else:
        print("Personajes desponibles: ")
        for i, personaje in enumerate(personajes):
            print(f"{i + 1}. {personaje}")


while True:
    print("-------------------------------")
    print("|           Menú              |")
    print("| 1.- Crar personaje          |")
    print("| 2.- Fusionar personajes     |")
    print("| 3.- Mostrar personajes      |")
    print("| 4.- Salir                   |")
    print("-------------------------------")
    try:
        op = int(input("Seleccione una opción: "))
        if op == 1:
            personaje_nuevo = crear_personaje()
            personajes.append(personaje_nuevo)
            print("Personaje creado con éxito")
        elif op == 2:
            if len(personajes) < 2:
                print("No hay suficientes personajes para fusionar.")
            else:
                print("---------------------------")
                mostrar_personajes(personajes)
                print("---------------------------")
                num_1 = int(input("Ingresa el número del 1er personaje: "))
                num_2 = int(input("Ingresa el número del 2do personaje: "))
                if 1 <= num_1 <= len(personajes) and 1 <= num_2 <= len(personajes) and num_1 != num_2:
                    personaje1 = personajes[num_1 - 1]
                    personaje2 = personajes[num_2 - 1]
                    nuevo_personaje = personaje1.fusionar(personaje2)
                    personajes.append(nuevo_personaje)
                    print(f"El nuevo personaje es: {nuevo_personaje}")
                else:
                    print("Selección no valida, ingrese personajes existentes")
        elif op == 3:
            mostrar_personajes(personajes)
        elif op == 4:
            print("Gracias, vuelva pronto")
            break
        else:
            print("Ingrese una opción válida")
    except Exception as e:
        print(f"Opción no válida\nError: {e}")
