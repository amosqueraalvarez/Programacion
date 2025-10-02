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
