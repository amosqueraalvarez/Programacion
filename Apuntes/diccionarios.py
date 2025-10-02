# diccionarios

# conjunto clave : valor
colores = {'verde': 'green',
           'vermello': 'red',
           'azul': 'blue'}

# al hacer el print le paso la clave y me devulve el valor
print(colores['vermello'])

# con el metodo .keys me imprime todas las claves
print(colores.keys())

# con el metodo .values me imprime todos los valores
print(colores.values())


# utilizar el for para recorrer un diccionario

for color in colores.values():
    print(color)


for clave in colores.keys():
    print(colores[clave])
