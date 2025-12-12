# creamos un punto en POO

# definimos una clase con la palabra reservada class y su nombre a continuacion
# el nombre de la clase se escribe en mayusculas
import math


class Punto:
    def __init__(self, x, y):  # las clases necesitan un inicializador y siempre tiene que llevar el parametro self y los parametros que necesito
        self.x = x  # self dice que es una propiedad propia del objeto y x es la variable temporal
        self.y = y

# metodo
    def toString(self):
        cadeaPunto = 'As coordenadas do punto son: \n x = ' + \
            str(self.x) + '\n y = ' + \
            str(self.y)  # \n es un salto de linea \t hace una tabulacion
        return cadeaPunto

    def __str__(self):
        return self.toString()

# este metodo me vale para comparar un objeto con otro
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

    def distanciaEntreDosPuntos(self, outroPunto):
        return math.sqrt((self.x - outroPunto.x)**2 + (self.y - outroPunto.y)**2)
