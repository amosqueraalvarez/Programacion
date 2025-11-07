# herencia

from punto_1 import Punto
import math


class Circulo(Punto):
    def __init__(self, x, y, radio):
        super(). __init__(x, y)  # llamamos con super los datos de punto
        self.radio = radio  # definimos la variable nueva que aparece en circulo

    def obterDiametro(self, radio):
        diametro = radio*2
        return diametro

    def calcularPerimetro(self, radio):
        perimetro = 2*radio*math.pi
        return perimetro

    def calcularArea(self, radio):
        area = math.pi * (radio**2)
        return area

    def aCadea(self):
        cadea = super().toString() + '\n Radio : ' + str(self.radio)
        return cadea
