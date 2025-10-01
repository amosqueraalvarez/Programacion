# boletin 3.1


numero = float(input('Ingrese un numero: '))
while numero < 0:
    print('Ingrese un numero positivo')
    numero = float(input('Ingrese un numero: '))
else:
    print('Su numero es: ' + str(numero))


# boletin 3.2


numero = float(input('Ingrese un numero: '))
numero2 = float(input('Ingrese otro numero: '))
while numero >= numero2:
    resta = (numero - numero2)
    print('Los numeros se restan' + str(resta))
    break
else:
    numero < numero2
    suma = (numero + numero2)
    print('Los numeros se suman' + str(suma))


# boletin 3.3


numero_masomenos = float(input('Ingrese un numero: '))
if numero_masomenos < 0:
    print('-')
else:
    numero_masomenos >= 0
    print('+')


# boletin 3.4

nombre_1 = str(input('Primer usuario, ingrese su nombre: '))
peso_1 = float(input('Ingrese su peso: '))
nombre_2 = str(input('Segundo usuario, ingrese su nombre: '))
peso_2 = float(input('Ingrese su peso: '))

if peso_1 > peso_2:
    diferencia_peso = peso_1 - peso_2
    print('El primer usuario pesa mas y tiene una diferencia de peso de: ' +
          str(diferencia_peso) + 'kg.')
else:
    if peso_1 < peso_2:
        diferencia_peso_2 = peso_2 - peso_1
        print('El segundo usuario pesa mas y tiene una diferencia de peso de: ' +
              str(diferencia_peso_2) + 'kg.')
    else:
        pesos_iguales = peso_1 == peso_2
        print('Los dos usuarios tienen el mismo peso')

# boletin 3.5


numero1 = 8
numero2 = 2
numero3 = 0

if numero1 >= numero2 and numero1 >= numero3:
    print(numero1)
else:
    if numero2 >= numero1 and numero1 >= numero3:
        print(numero2)
    else:
        numero3 >= numero1 and numero1 >= numero2
        print(numero3)
