from circulo import Circulo
import math


class Esfera(Circulo):
    def __init__(self, x, y, radio):
        super().__init__(x, y, radio)

    def obtenerVolumenEsfera(self):
        volumen = 4/3 * math.pi*self.radio ** 3
        return 'O volume da esfera e: ', volumen

    def obtenerSuperficieEsfera(self):
        supercifie = 4*super().calcularArea(self.radio)  # importante
        return 'A superficie da esfera e: ', supercifie
