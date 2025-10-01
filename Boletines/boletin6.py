# boletin 6.5.1
'''
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(abecedario[2:27:3])
'''
# boletin 6.5.2
'''
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista = []
for i in range(0, 27):
    if i % 3 == 0:
        lista.append
        print(i)
    else:
        print('El numero no es multiplo de 3')
'''

# boletin 6.5.3
'''
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(abecedario)):
    if i % 3 == 0:
        print(i, abecedario[i])
    else:
        print(abecedario[i], 'El numero no es multiplo de 3')

'''

# boletin 6.1

curso = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lingua']

'''
for i in range(len(curso)):
    print(curso[i])
    nota = int(input('Que nota sacache en: '))
    print('Saquei un:', nota, 'en', curso[i])
'''
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

