# importar funcion de clases que tengo

from persoa_clase import Persoa
from punto_1 import Punto  # from (archivo) import (objeto clase) Punto

p1 = Punto(2, 3)
p2 = Punto(9, 1)

# va a dar false porque apunta a direccion de memoria y no es la misma
# para compararlos tengo que definir un metodo en el objeto
print(p1 == p2)
p2.x = 2
p2.y = 3
print(p1 == p2)

# toString es el metodo que cree en la funcion dentro del objeto
print(p1.toString())
print(p2)

# si no me acuerdo del orden asigno el valor a la variable que tenia el objeto
adrian = Persoa('Adrian', dni='00000000T', nacionalidade='Española',
                direccion='Garcia Barbon 49', edade=33)
print(adrian)

# puedo acceder a la propiedad x del objeto
print(p1.x)

# puedo darle un valor a una propiedad del objeto
p1.x = 9999
print(p1.x)

print(p1 == p2)
p1 = p2
p3 = p1

# lo que va a hacer es que todas apunten a p1 y pierdan sus propiedades p2 y p3
# p1 pasa a tener el valor de p2 y p3 apunta a p1 que va a p2

print(p1 == p2)

mario = Persoa(dni='00000000T', nome='mario', edade=3,
               direccion='jsijs', nacionalidade='JSJ')

print(mario == adrian)

print(adrian < mario)
