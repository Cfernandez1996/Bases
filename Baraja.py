import random
from Carta import Carta

class Baraja:
    def __init__(self):
        colores = ["rojo", "verde", "azul", "amarillo"]
        valores = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Saltar", "Reversa", "Toma2"]

        self.cartas = []
        for color in colores: 
            for valor in valores: 
                self.cartas.append(Carta(valor, color) )

        self.cartas += [Carta("CambioDeColor", "Negro") for _ in range(4)]
        self.cartas += [Carta("Toma4", "Negro") for _ in range(4)]

    def mezclar(self):
        random.shuffle(self.cartas)  ##Mezcla las cartas colores y valores

    def repartir_cartas(self, cantidad):
        return [self.cartas.pop() for _ in range(cantidad)]