from Baraja import Baraja
from Carta import Carta
from Jugador import Jugador

class JuegoUno:
    def __init__(self, jugadores):
        self.baraja = Baraja()
        self.baraja.mezclar()
        self.jugadores = jugadores
        self.cartas_jugadas = []

    def repartir_cartas_iniciales(self, cantidad):
        for jugador in self.jugadores:
            cartas_iniciales = self.baraja.repartir_cartas(cantidad)
            jugador.tomar_cartas_iniciales(cartas_iniciales)


    def jugar(self):
        self.repartir_cartas_iniciales(7)

        carta_actual = self.baraja.cartas.pop()
        self.cartas_jugadas.append(carta_actual)

        turno = 0
        sentido_del_juego = 1  # 1 para adelante, -1 para atrás

        while True:
            jugador_actual = self.jugadores[turno]
            print("\n" + "=" * 40)
            print(f"Carta actual: {carta_actual}")
            print(jugador_actual)

            # Buscamos una carta válida para jugar
            carta_valida = False
            while not carta_valida:
                indice = int(input("Elige el índice de la carta que deseas jugar (0-6): "))
                if indice >= 0 and indice < len(jugador_actual.cartas_en_mano):
                    carta_jugada = jugador_actual.jugar_carta(indice)
                    if carta_jugada.color == carta_actual.color or carta_jugada.valor == carta_actual.valor \
                            or carta_jugada.color == "Negro":
                        carta_actual = carta_jugada
                        self.cartas_jugadas.append(carta_actual)
                        carta_valida = True
                    else:
                        print("Carta no válida. Inténtalo de nuevo.")
                else:
                    print("Índice inválido. Inténtalo de nuevo.")

            # Verificamos si el jugador ganó
            if len(jugador_actual.cartas_en_mano) == 0:
                print(f"¡{jugador_actual.nombre} ha ganado!")
                break

            # Aplicamos efectos especiales de las cartas
            if carta_actual.valor == "Saltar":
                turno = (turno + 1 * sentido_del_juego) % len(self.jugadores)
            elif carta_actual.valor == "Reversa":
                sentido_del_juego *= -1
                turno = (turno + sentido_del_juego) % len(self.jugadores)
            elif carta_actual.valor == "Toma2":
                siguiente_jugador = self.jugadores[(turno + sentido_del_juego) % len(self.jugadores)]
                cartas_tomar = self.baraja.repartir_cartas(2)
                siguiente_jugador.tomar_cartas_iniciales(cartas_tomar)
                turno = (turno + 1 * sentido_del_juego) % len(self.jugadores)
            elif carta_actual.valor == "Toma4":
                siguiente_jugador = self.jugadores[(turno + sentido_del_juego) % len(self.jugadores)]
                cartas_tomar = self.baraja.repartir_cartas(4)
                siguiente_jugador.tomar_cartas_iniciales(cartas_tomar)
                turno = (turno + 1 * sentido_del_juego) % len(self.jugadores)
                nuevo_color = input("Elige un color para continuar (Rojo, Verde, Azul o Amarillo): ")
                carta_actual.color = nuevo_color
            elif carta_actual.valor == "CambioDeColor":
                nuevo_color = input("Elige un nuevo color (Rojo, Verde, Azul o Amarillo): ")
                carta_actual.color = nuevo_color

            turno = (turno + sentido_del_juego) % len(self.jugadores)
