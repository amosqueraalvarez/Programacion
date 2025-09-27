# boletin 4.1
'''
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

'''

print('''
[1] Superficie de triangulo
[2] Superficie de cuadrado
[3] Superficie del circulo
[4] Salir''')
'''
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
'''

# 3. Utiliza o operador ternario para calcular o valor absoluto dun número que se solicita o usuario por teclado.


def valorAbsoluto(x):
    valor = abs(x)
    return valor


valor = (int(input('Introduce un numero: ')))
