'''
palabra = 'coche'
palabra2 = ('_'*(len(palabra)))

contador = 9
while contador > 0:
    print(palabra2)
    letra = str(input('Escribe un letra: '))
    if letra in palabra:
        palabra.find(letra)
    if letra not in palabra:
        print(' no esta')
        contador -= 1
        print('Te quedan', contador, 'vidas')
'''

fallos = 0
palabra = 'frigorifico'
palabraGuions = '_' * len(palabra)
acertado = False

while acertado == False and fallos <= 6:
    print('A palabra a acertar e: ', palabraGuions)
    palabraLetra = input('Introduce a palabra ou a letra: ')
    if len(palabraLetra) != 0:
        if len(palabraLetra) != 1:
            if palabraLetra == palabra:
                acerto = True
                print('Felicidades a palabra era: ', palabra)
            else:
                fallos += 1
        else:
            acertado = False
            # se usa enumerate para ver en que posicion esta la letra que tiene que cambiar
            for i, caracter in enumerate(palabra):
                if palabraLetra == caracter:
                    palabraGuions = palabraGuions[:i] + \
                        caracter + palabraGuions[i+1:]
                    encontrado = True

            if encontrado == True:
                if palabraGuions == palabra:
                    print('Enhorabuena, acertaste la palabra: ', palabra)
                    acerto = True
            else:
                fallos += 1
