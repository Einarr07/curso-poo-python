from textblob import TextBlob

# Clase para representar un sentimiento con un nombre y un color asociado
class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)


# Clase para analizar sentimientos
class AnalizadorDeSentimientos:
    def __init__(self):
        pass

    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0.5:
            return Sentimiento("Too positive", 32)  # Color verde
        elif 0.3 < analisis.sentiment.polarity <= 0.5:
            return Sentimiento("Very positive", 32)  # Color verde
        elif 0.1 < analisis.sentiment.polarity <= 0.3:
            return Sentimiento("Positive", 32)  # Color verde
        elif -0.1 <= analisis.sentiment.polarity <= 0.1:
            return Sentimiento("Neutral", 33)  # Color amarillo
        elif -0.3 <= analisis.sentiment.polarity < -0.1:
            return Sentimiento("Negative", 31)  # Color rojo
        elif -0.5 <= analisis.sentiment.polarity < -0.3:
            return Sentimiento("Very negative", 31)  # Color rojo
        else:
            return Sentimiento("Too negative", 31)  # Color rojo


def main():
    # Crear una instancia del analizador de sentimientos
    analizador = AnalizadorDeSentimientos()

    # Bucle que se ejecuta continuamente hasta que se escriba 'exit'
    while True:
        # Imprimir un mensaje para indicar al usuario cómo salir del chat
        print("if you want to exit, only write 'exit' and our chat will end\n")

        # Pedir al usuario que escriba algo
        texto = input("Tell me something: ")

        # Comprobar si el usuario quiere salir
        if texto.lower() == 'exit':
            break  # Salir del bucle si se escribe 'exit'

        # Analizar el sentimiento del texto ingresado por el usuario
        resultado = analizador.analizar_sentimiento(texto)

        # Imprimir el resultado del análisis de sentimiento
        print(resultado)


# Ejecutar la función main si el script se ejecuta directamente
if __name__ == "__main__":
    main()
