# boletin 4.1

articulo = 10000


if articulo <= 100:
    print('Articulo de bajo consumo')
else:
    if articulo > 100 and articulo <= 500:
        print('Articulo de consumo medio')
    else:
        if articulo > 500 and articulo <= 1000:
            print('Articulo de alto consumo')
        else:
            if articulo > 1000:
                print('Articulo de primera necesidad')


# 4.2

# print('''
# [1] Superficie de triangulo
# [2] Superficie de cuadrado
# [3] Superficie del circulo
# [4] Salir''')


opcion = (int(input('Elija una opcion: ')))

if opcion == 1:
    lado = (float(input('Lado del triangulo: ')))
    altura = (float(input('Altura del triangulo: ')))
    area_triangulo = (lado * altura)/2
    print('El area del triangulo es: ', area_triangulo)
else:
    if opcion == 2:
        lado_cuadrado = (float(input('Lado del cuadrado: ')))
        area_cuadrado = lado_cuadrado*lado_cuadrado
        print('El area del cuadrado es: ', area_cuadrado)
    else:
        if opcion == 3:
            radio = (float(input('Radio del circulo: ')))
            pi = 3.14
            area_circulo = (pi * (radio**2))
            print('El area del circulo es: ', area_circulo)
        else:
            if opcion == 4:
                print('Hasta otra')
            else:
                if opcion > 4:
                    print('No es una opcion valida')

# 3. Utiliza o operador ternario para calcular o valor absoluto dun número que se solicita o usuario por teclado.

numero = float(input('Ingrese un numero: '))

if numero < 0:
    calculo = numero * -1
    print(calculo)
else:
    calculo2 = numero * 1
    print(calculo2)


# boletin 4.4

numeros_a_letras = {
    0: 'cero',
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco',
    6: 'seis',
    7: 'siete',
    8: 'ocho',
    9: 'nueve',
    10: 'diez',
    11: 'once',
    12: 'doce',
    13: 'trece',
    14: 'catorce',
    15: 'quince',
    16: 'dieciséis',
    17: 'diecisiete',
    18: 'dieciocho',
    19: 'diecinueve',
    20: 'veinte',
    21: 'veintiuno',
    22: 'veintidós',
    23: 'veintitrés',
    24: 'veinticuatro',
    25: 'veinticinco',
    26: 'veintiséis',
    27: 'veintisiete',
    28: 'veintiocho',
    29: 'veintinueve',
    30: 'treinta',
    31: 'treinta y uno',
    32: 'treinta y dos',
    33: 'treinta y tres',
    34: 'treinta y cuatro',
    35: 'treinta y cinco',
    36: 'treinta y seis',
    37: 'treinta y siete',
    38: 'treinta y ocho',
    39: 'treinta y nueve',
    40: 'cuarenta',
    41: 'cuarenta y uno',
    42: 'cuarenta y dos',
    43: 'cuarenta y tres',
    44: 'cuarenta y cuatro',
    45: 'cuarenta y cinco',
    46: 'cuarenta y seis',
    47: 'cuarenta y siete',
    48: 'cuarenta y ocho',
    49: 'cuarenta y nueve',
    50: 'cincuenta',
    51: 'cincuenta y uno',
    52: 'cincuenta y dos',
    53: 'cincuenta y tres',
    54: 'cincuenta y cuatro',
    55: 'cincuenta y cinco',
    56: 'cincuenta y seis',
    57: 'cincuenta y siete',
    58: 'cincuenta y ocho',
    59: 'cincuenta y nueve',
    60: 'sesenta',
    61: 'sesenta y uno',
    62: 'sesenta y dos',
    63: 'sesenta y tres',
    64: 'sesenta y cuatro',
    65: 'sesenta y cinco',
    66: 'sesenta y seis',
    67: 'sesenta y siete',
    68: 'sesenta y ocho',
    69: 'sesenta y nueve',
    70: 'setenta',
    71: 'setenta y uno',
    72: 'setenta y dos',
    73: 'setenta y tres',
    74: 'setenta y cuatro',
    75: 'setenta y cinco',
    76: 'setenta y seis',
    77: 'setenta y siete',
    78: 'setenta y ocho',
    79: 'setenta y nueve',
    80: 'ochenta',
    81: 'ochenta y uno',
    82: 'ochenta y dos',
    83: 'ochenta y tres',
    84: 'ochenta y cuatro',
    85: 'ochenta y cinco',
    86: 'ochenta y seis',
    87: 'ochenta y siete',
    88: 'ochenta y ocho',
    89: 'ochenta y nueve',
    90: 'noventa',
    91: 'noventa y uno',
    92: 'noventa y dos',
    93: 'noventa y tres',
    94: 'noventa y cuatro',
    95: 'noventa y cinco',
    96: 'noventa y seis',
    97: 'noventa y siete',
    98: 'noventa y ocho',
    99: 'noventa y nueve',
    100: 'cien'
}
pedir_numero = int(input('Dime un numero: '))
for i in numeros_a_letras.keys():
    if pedir_numero == i:
        print(numeros_a_letras[i])


# boletin 4.5

letras = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B',
          12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'}

numero = int(input('Cual es tu numero de dni: '))
dni = numero % 23

for i in letras.keys():
    if i == dni:
        print(letras[i])
