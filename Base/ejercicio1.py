# Creamos una clase estudiante
class Estudiante:
    # Creamos el constructor con 3 atributos
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    # Creamos un método (una acción que puede realizar el estudiante)
    def estudiar(self):
        print(f"El estudiante {self.nombre} está repasando para el examen")


# Creamos un bucle while para que el código se mantenga así haya errores
while True:
    # Manejamos los errores con un try-except
    try:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break

        edad = int(input("Ingrese la edad del estudiante: "))

        # Utilizamos otro bucle while para manejar el grado
        while True:
            grado = input("Ingrese el grado del estudiante: ")
            if grado.strip():  # Verificar que la cadena no esté vacía
                break
            else:
                print("Por favor, ingrese un grado válido.")

        # Creamos nuestra instancía
        estudiante = Estudiante(nombre, edad, grado)

        print("----------------------------------")
        print(" DATOS DEL ESTUDIANTE:          ")
        print(f" Nombre: {estudiante.nombre}    ")
        print(f" Edad: {estudiante.edad}        ")
        print(f" Grado: {estudiante.grado}      ")
        print("----------------------------------")

        # Le enviamos un mensaje al usuario y veridicamos que este se cumpla
        estudiar = input("Si quieres que el estudiante se ponga a repasar para el examen,"
                         " escribe: 'Estudia' o 'Estudiar': ")

        if (estudiar.lower() == "estudiar") or (estudiar.lower() == "estudia"):
            estudiante.estudiar()
            break
        else:
            print("No es la palabra correcta")

    # Manejo de excepciones
    except ValueError:
        print("Error: La edad debe ser un número entero.")
    except Exception as e:
        print(f"Error: {e}")
