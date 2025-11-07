from circulo import Circulo
import math


class Cilindro(Circulo):
    def __init__(self, x, y, radio, longitud):
        super(). __init__(x, y, radio)  # llamamos con super los datos de punto
        self.longitud = longitud  # definimos la variable nueva que aparece en circulo

    def calcularVolume(self,  longitud):
        perimetro = longitud*(self.radio**2)*math.pi
        return 'O perimitro e: ', perimetro

    def calcularAreaCil(self, longitud):
        area = (2 * math.pi * self.radio) + \
            (2 * math.pi * self.radio * self.longitud)
        return 'A area e: ', area

    def aCadea2(self):
        cadea = super().aCadea() + '\n longitud : ' + \
            str(self.longitud)
        return cadea
