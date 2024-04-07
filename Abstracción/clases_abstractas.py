from abc import ABC, abstractclassmethod  # Importa las clases ABC y abstractclassmethod del módulo abc


# Definición de la clase abstracta Persona
class Persona(ABC):
    @abstractclassmethod  # Decorador para definir un método abstracto
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre  # Inicializa el atributo nombre
        self.edad = edad  # Inicializa el atributo edad
        self.sexo = sexo  # Inicializa el atributo sexo
        self.actividad = actividad  # Inicializa el atributo actividad

    @abstractclassmethod  # Decorador para definir un método abstracto
    def hacer_actividad(self):
        pass  # No implementa la lógica, ya que es un método abstracto

    def presentarse(self):
        # Método concreto que muestra un saludo con el nombre y la edad de la persona
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")


# Definición de la clase concreta Trabajador que hereda de Persona
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)  # Llama al constructor de la clase base

    def hacer_actividad(self):
        # Implementación específica para Trabajador del método hacer_actividad
        print(f"Actualmente estoy trabajando en: {self.actividad}")


# Definición de la clase concreta Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)  # Llama al constructor de la clase base

    def hacer_actividad(self):
        # Implementación específica para Estudiante del método hacer_actividad
        print(f"Estoy estudiando: {self.actividad}")


# Creación de instancias de las clases concretas
martin = Estudiante("Martin", 24, "Masculino", "Musica")  # Crea un estudiante llamado Martin
martin.hacer_actividad()  # Llama al método hacer_actividad de Martin
gaby = Trabajador("Gabriela", 35, "Femenino", "Educación inicial")  # Crea un trabajador llamado Gabriela
gaby.hacer_actividad()  # Llama al método hacer_actividad de Gabriela
