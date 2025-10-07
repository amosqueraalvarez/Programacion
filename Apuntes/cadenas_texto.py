# cadenas de texto

c = 'esto es una cadena de texto'

# se puede poner comilla simple o doble
# pero se puede resaltar un texto dentro de otro usando el caracter contrario

d = 'estoy es un "texto" resaltado'


# se puede tratar una cadena de texto como una coleccion y sacar cualquier valor

for caracter in c:
    print(caracter)

print(d[3])

# esto da error, las cadenas de caracteres son inmutables
'''
c[5] = '6'
print(c)
'''

# metodos con cadenas

print(c.count('a'))

# en este caso cuenta tambien el espacio

print(c.count('a '))

print(c.count('a', 2, 10))

# longitud

print(len(c))

# find, encuentra caracteres o subsecuencias de caracteres

print(c.find('a', 5, 9))

# join,invalido

# print(c.join('diuhdaiushihdas'))

# concatenar cadenas

print(c+d)

# partition

print(c.partition(" "))

# replace, remplaza un caracter por el que le diga

print(c.replace(' ', '_'))

# split,separa cada palabra entre lo que yo defina

print(c.split(' '))

animal = 'chanCHito feliz'

# metodo .upper pone todo en mayusculas
print(animal.upper())

# .lower todo minusculas
print(animal.lower())

# .capitalize la primera letra de cada palabra en mayusculas
print(animal.capitalize())

# .title parecido a .capitalize pero pasa la primera a mayuscula y el resto a minuscula de cada palabra
animal = 'ChAnchitO fELIZ'
print(animal)
print(animal.title())
