class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre}, (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round((self.fuerza + otro_pj.fuerza)/2)**1.34
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 99,99)
jiren = Personaje("Jiren", 130, 130)

gogeta = goku + vegeta
jireta = gogeta + jiren

print(jireta)
print(gogeta)
print(goku)
print(jiren)