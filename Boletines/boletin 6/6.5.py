# boletin 6.5.1

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(abecedario[2:27:3])

# boletin 6.5.2

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista = []
for i in range(0, 27):
    if i % 3 == 0:
        lista.append
        print(i)
    else:
        print('El numero no es multiplo de 3')


# boletin 6.5.3

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(abecedario)):
    if i % 3 == 0:
        print(i, abecedario[i])
    else:
        print(abecedario[i], 'El numero no es multiplo de 3')
