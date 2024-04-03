# Método de resolución de orden (MRO)

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")


class C(B):
    def hablar(self):
        print("Hola desde C")


class D(C):
    def hablar(self):
        print("Hola desde D")


class E(D):
    def hablar(self):
        print("Hola desde E")


class F(D, C):
    def hablar(self):
        print("Hola desde F")


instancia = F()

# Si quiseiramos llamar un método desde otra clase que no pertenesca al orden de herencia colocamos:
C.hablar(instancia)

# Con el método especial mro() nos devuelve una lista en el orden de resolución de métodos
print(F.mro())
