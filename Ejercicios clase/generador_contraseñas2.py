import random


def generar_contrasinal(n):
    caracteres = (
        '1234567890'
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        '.,_-!"·$%&/()'
    )
    return ''.join(random.choice(caracteres) for _ in range(n))


while True:
    n = int(input('Introduce la longitud del contrasinal (0 para salir): '))

    if n == 0:
        break
    elif 6 <= n <= 12:
        print('Contrasinal xerado:', generar_contrasinal(n))
    else:
        print('La longitud válida es entre 6 y 12.')
