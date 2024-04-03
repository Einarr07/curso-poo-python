class Animal:
    def comer(self):
        print("El animal está comiendo")


class Ave(Animal):
    def volar(self):
        print("El animal está volando")


class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")


class Murcielago(Mamifero,Ave):
    pass


ave = Murcielago()

# Al ser un murciélago este puede heredar los 3 métodos
ave.comer()
ave.amamantar()
ave.volar()

# En este caso nuestra instancia solo puede heredar dos métodos el de comer y el de volar
# ave = Ave()
# ave.comer()
# ave.volar()

print(Murcielago.mro())