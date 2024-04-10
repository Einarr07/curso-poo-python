"""
Esto NO es correcto debido a que la clase CorretorOrtografico depende de Diccionario y diccionario es una clase
más pequeña que CorrectorOrtografico

class Diccionario:
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras
        pass


class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        # Usamos el diccionario para corregir el texto
        pass
"""
from abc import ABC, abstractmethod

# En este ejemplo no estamos dependiendo de Diccionario, ahora depende de la implementación del verificador


class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass


class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si está en el diccionario
        pass


class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras desde el servicio web
        pass


class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # Usamos el verificador para corregir el texto NO usamos el diccionario como antes
        pass


# Depende de una interfaz, no de un método en especifico
corrector = CorrectorOrtografico(Diccionario())
corrector_online = CorrectorOrtografico(ServicioOnline)