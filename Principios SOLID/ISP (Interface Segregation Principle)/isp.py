# Ningun cliente debe depender de interfaces que no se utilizán

from abc import ABC, abstractmethod


""" ESTO ESTA MAL, PORQUE NO APLICA EL PRINCIPIO ISP
class Trabajador(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass
"""


class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass


class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass


class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")


robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
