# Todo lo que hace la clase principal lo debe poder hacer la subClase
"""
class Ave:
    def volar(self):
        return "Estoy volando"


class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"


def hacer_volar(ave = Ave):
    return ave.volar()

print(hacer_volar(Pinguino()))
"""


class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "Estoy Volando"


class AveNoVoladora(Ave):
    pass