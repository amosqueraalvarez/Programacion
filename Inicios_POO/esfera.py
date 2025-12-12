from circulo import Circulo
import math


class Esfera(Circulo):
    def __init__(self, x, y, radio):
        super().__init__(x, y, radio)

    def obtenerVolumenEsfera(self):
        return 4 * super().calcularArea()

    def obtenerSuperficieEsfera(self):
        supercifie = 4*super().calcularArea(self.radio)  # importante
        return 'A superficie da esfera e: ', supercifie
