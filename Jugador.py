from Carta import Carta

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas_en_mano = []

    def tomar_cartas_iniciales(self, cartas):
        self.cartas_en_mano.extend(cartas)

    def tomar_carta(self, carta):
        self.cartas_en_mano.append(carta)

    def jugar_carta(self, indice):
        return self.cartas_en_mano.pop(indice)

    def __str__(self):
        return f"{self.nombre}, Cartas en mano: {', '.join(map(str, self.cartas_en_mano))}"
    
