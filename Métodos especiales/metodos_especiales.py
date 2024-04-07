class Persona:
    def __init__(self, nombre, edad):
        # Método especial de inicialización. Crea una nueva instancia de Persona.
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        # Método especial para convertir la instancia en una cadena legible.
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __repr__(self):
        # Método especial para representar la instancia de manera formal.
        return f"Persona('{self.nombre}', {self.edad})"

    def __add__(self, otro):
        # Método especial para sumar las edades de dos instancias de Persona.
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)


gaby = Persona("Gabriela", 21)
katy = Persona("Katerine", 30)

nueva_persona = gaby + katy  # Se suma las edades y se concatena los nombres
print(nueva_persona.edad)

repre = repr(gaby)  # Se obtiene la representación formal de gaby
print(repre)

resultado = eval(repre)  # Se evalúa la representación formal de gaby
print(resultado.nombre)
