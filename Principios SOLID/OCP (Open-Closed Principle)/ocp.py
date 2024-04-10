"""
Este principio se trata de que este abierto a nueva funcionalidades pero este cerrado a modificaciones
como se potra apreciar en el ejemplo utilizamos la clase principal Notificador para crear nievas subClases
como email, sms, whatsapp, tiwtter eso quiere decir que esta abierto a nuevas funcionalidades, si quisieramos enviar
posteriormente una notificación por facebook lo podemos hacer agregando otra clase y todo esto sin alterar la clase
principal
"""


class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por email a: {self.usuario.email}")


class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando sms a: {self.usuario.sms}")


class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando whatsapp a: {self.usuario.whatsapp}")


class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando twit a: {self.usuario.twitter}")
