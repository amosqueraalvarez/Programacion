suma = 0
numero = int(input('Ingrese un numero: '))
for i in range(numero):
    if i % 2 == 0:
        suma += i
        print(suma)
print('El total es: ', suma)
