import random


def xeradorContrasinais(n):
    l = ['1234567890',
         'abcdefghijklmnopqrstuvwxyz',
         'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ',
         '.,_-!"·$%&/()']

    contrasinal = ''
    i = 0

    while i < n:
        tipo = random.randint(0, 3)
        iSimbolo = random.randint(0, len(l[tipo]) - 1)
        contrasinal += l[tipo][iSimbolo]
        i += 1  # incrementar el contador

    return contrasinal


while True:
    n = int(input('Introduce a lonxitude do contrasinal (0 para sair): '))

    if n == 0:
        break
    elif 6 <= n <= 12:
        print('Contrasinal xerado:', xeradorContrasinais(n))
    else:
        print('A lonxitude válida é entre 6 e 12.')
