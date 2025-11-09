# calcular dun cono volume, superficie e calcular seneratriz

from cilindro import Cilindro
import math


class Cono(Cilindro):
    def __init__(self, x, y, radio, longitud):
        super().__init__(x, y, radio, longitud)

    def calcularVolumenCono(self):
        volumen = 1/3*math.pi*self.radio**2*self.longitud
        return 'O volume do cono e: ', volumen

    def calcularGeneratrizCono(self):
        generatriz = math.sqrt(self.longitud**2*self.radio**2)
        return 'A generatriz do cono e: ', generatriz

    def calcularSuperficieCono(self):
        superficie = math.pi * self.radio * \
            (math.sqrt(self.longitud**2*self.radio**2) + self.radio)
        return 'A superficie do cono e: ', superficie
