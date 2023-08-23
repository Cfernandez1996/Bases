from Jugador import Jugador
from JuegoUno import JuegoUno

class Main:
    def __init__(self):
        self.jugadores = []
        self.crear_jugadores()
        self.juego = JuegoUno(self.jugadores)

    def crear_jugadores(self):
        num_jugadores = 2  # Puedes cambiar este número según la cantidad de jugadores que desees
        for i in range(num_jugadores):
            nombre = input(f"Ingresa el nombre del jugador {i + 1}: ")
            self.jugadores.append(Jugador(nombre))

    def iniciar_juego(self):
        self.juego.jugar()

if __name__ == "__main__":
    main = Main()
    main.iniciar_juego()

