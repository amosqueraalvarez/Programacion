#lista y tupla

#en lista necesitamos marcas la lista entre []
l=[10, 20, 30, 40, 50]
#como acceder a los datos:
# los indices (orden) empiezas desde 0 de izq a derecha
#de derecha a izquierda van de -1 a x

#solo se separan por comas y van entre parentesis(no necesarias)
t= (10, 20, 30, 40, 50)

l=[10, 20, 30, 40, 50]
t= (10, 20, 30, 40, 50)

#asi llamo al indice numero 2 de la lista
print(l[2])
# en las tuplas se llama igual entre []
print(t[1])

print(l[-3])

# una lista puede ser compuesta y contener una lista dentro de ella

l=[10, 20, ['XXX', 'Treinta', 30],30, 40, 50]
#busco dentro de la lista que hay en la lista
print(l[2][1])

#si quiero extraer solo una parte de la lista o de la tupla
#utilizo los : entre inicio y final 1:3 coge el indice 1 y 2, el 3 no lo coge(en su defecto seria 1:4 para incluir el indice 3)

print(t[1:3])

t=(10,20,30,40,50,60,70,80,90,100)
#asi marco inicio y final de lo que busca y que saque los pares
print(t[1:10:2])