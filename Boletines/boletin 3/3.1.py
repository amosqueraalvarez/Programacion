# boletin 3.1


numero = float(input('Ingrese un numero: '))
while numero < 0:
    print('Ingrese un numero positivo')
    numero = float(input('Ingrese un numero: '))
else:
    print('Su numero es: ' + str(numero))
