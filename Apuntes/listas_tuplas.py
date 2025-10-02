# en lista necesitamos marcas la lista entre []
l = [10, 20, 30, 40, 50]
# como acceder a los datos:
# los indices (orden) empiezas desde 0 de izq a derecha
# de derecha a izquierda van de -1 a x

# solo se separan por comas y van entre parentesis(no necesarias)
t = (10, 20, 30, 40, 50)

l = [10, 20, 30, 40, 50]
t = (10, 20, 30, 40, 50)

# asi llamo al indice numero 2 de la lista
print(l[2])
# en las tuplas se llama igual entre []
print(t[1])

print(l[-3])

# una lista puede ser compuesta y contener una lista dentro de ella

l = [10, 20, ['XXX', 'Treinta', 30], 30, 40, 50]
# busco dentro de la lista que hay en la lista
print(l[2][1])

# si quiero extraer solo una parte de la lista o de la tupla
# utilizo los : entre inicio y final 1:3 coge el indice 1 y 2, el 3 no lo coge(en su defecto seria 1:4 para incluir el indice 3)

print(t[1:3])

t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# asi marco inicio y final de lo que busca y que saque los pares
print(t[1:10:2])
# recorre la lista hacia atras
print(t[::-1])

# las tuplas son inmutables
# las listas si se pueden cambiar

# lista y tupla continuacion

l = [1, 2, 3, 4, 6, 7, 8]
t = ['a', 'v']

# constructores

l2 = list([1, 2, 3, 4, 5])  # llamar a una lista

t2 = tuple((1, 2, 3, 45, 67, 0))  # llamar a una tupla

print(len(l))  # longitud de una lista
print(len(l2))
print(len(t2))

# añadir elementos a una lista

l2.append('a')
print(l2)

# añadir varios elementos

l2.extend(['a', 'd', 'c'])
print(l2)


# otro metodo de añadir pero necesita parametros de indice donde se coloca

l2.insert(0, 'z')  # indico donde tiene que ir concretamente
print(l2)

# borrar un elemento de la lista
# va a borrar la primera que encuentra igual

l2.remove('z')
print(l2)

# eliminar un valor y mirar cual quito

print(l2.pop(4))

# contabiliza cuantas veces aparece el valor en la lista

print(l2.count('d'))

# da la vuelta a la lista de forma permanente

# l2.reserve()
