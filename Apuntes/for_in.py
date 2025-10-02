# for se usa para los indeterminados
'''
'''
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
suma = 0

for elemento in t:  # elemento la acabo de crear y solo se puede usar dentro del for
    print(elemento)
    suma = suma + elemento
print(suma)

# defino la funcion len en el tamaño de la tupla
suma = 0
i = 0
while i < len(t):  # si no quiero definir el tamaño concreto de la tupla y simplemento uso len para ver la longitud de la tupla
    suma = suma + t[i]
    i += 1  # incremento de 1 en 1
    print(suma)

for i in range(0, 8):  # recorre por el rango que nosotros definamos
    print(i)
    print(t[i])

for i in range(7, 0, -1):  # hace una secuencia hacia atras
    print(i)
    print(t[i])


t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# ojo estoy declarando dos variables dentro y la i me recoge una cosa y numero otra
for i, numero in enumerate(t):
    print(i)  # me enumera los elementos de la tupla
    print(numero)  # me da el valor del elemento correspondiente de la tupla
