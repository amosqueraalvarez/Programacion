# boletin 6.2

def numeros_loteria():
    primero = int(input('Cuales es el primer numero de la loteria: '))
    segundo = int(input('Cuales es el segundo numero de la loteria: '))
    tercero = int(input('Cuales es el tercer numero de la loteria: '))
    cuarto = int(input('Cuales es el cuarto numero de la loteria: '))
    quinto = int(input('Cuales es el quinto numero de la loteria: '))
    return [primero, segundo, tercero, cuarto, quinto]


lista = []

numeros = numeros_loteria()
lista.append(numeros)

print(lista)
