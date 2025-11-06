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


# metodos


colores = {'verde': 'green',
           'vermello': 'red',
           'azul': 'blue'}


# se usa para imprimir el valor en el diccionario, se utilaza sobre todo por si el valor no existe
print(colores.get('vermello'))
# y pone un valor por defecto

print(colores['vermello'])

# saber cales son as claves de un diccionario

print(colores.keys())

for k in colores.keys():
    print(colores[k])

for color in colores.values():
    print(color)


# items nos da los pares
print(colores.items())

for clave, valor in colores.items():
    print(clave, valor)


for clave, valor in colores.items():
    print('a clave e: ', clave, ' o valor e: ', valor)


for clave_valor in colores.items():
    print(clave_valor)

# separa los elementos en una tupla, despues pide el indice en el print para dar cada dato de la tupla.

for clave_valor in colores.items():
    print('a clave e: ', clave_valor[0], 'o valor e: ', clave_valor[1])
