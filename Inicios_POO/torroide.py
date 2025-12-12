from circulo import Circulo
from punto_1 import Punto
import math


class Torroide(Circulo):
    def __init__(self, x, y, radio, centro):
        super().__init__(x, y, radio)
        self.centroToroX = centro.x
        self.centroToroY = centro.y

    def calculoRadioMaior(self):
        return self.distanciaEntreDosPuntos(
            Punto(self.centroToroX, self.centroToroY))

    def calcularSuperficieTorroide(self):
        # R = distancia centro circunferencia e centro toroide
        # radio toroide= R - radio circunferencia
        radioMaior = self.calculoRadioMaior()
        radioMenor = radioMaior - self.radio
        return 4 * math.pi**2*self.calculoRadioMaior()*radioMenor

    def volumeTorroide(self):
        return 2 * math.pi * self.calculoRadioMaior() * self.calcularArea()
