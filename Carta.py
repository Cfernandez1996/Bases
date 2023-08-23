class Carta:
    def __init__(self, valor, color):
        self.valor = valor
        self.color = color

    def __str__(self):
        return f"{self.color} {self.valor}"